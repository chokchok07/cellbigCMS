import re

with open('CMS-webpage/wireframe_site/version-register.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Safe Extraction
style_start = orig.find('<style>') + 7
style_end = orig.find('</style>')
modal_style = orig[style_start:style_end] if style_start > 6 else ''

html_start = orig.find('<div class="modal-overlay">')
html_end = orig.find('<script>', html_start)
modal_html = orig[html_start:html_end] if html_start > -1 else ''

script_start = orig.find('<script>', html_end) + 8
script_end = orig.find('</script>', script_start)
modal_script = orig[script_start:script_end] if script_start > 7 else ''

# Fix CSS conflicting classes
modal_style = modal_style.replace('.modal-overlay', '.v-modal-overlay')
modal_style = modal_style.replace('.modal {', '.v-modal {')
modal_style = modal_style.replace('.modal-header', '.v-modal-header')
modal_style = modal_style.replace('.modal-close', '.v-modal-close')
modal_style = modal_style.replace('.modal-body', '.v-modal-body')
modal_style = modal_style.replace('.modal-footer', '.v-modal-footer')

# IMPORTANT FIX: .modal is defined as display: none in styles.css.
modal_html = modal_html.replace('class="modal-overlay"', 'class="v-modal-overlay" id="versionModal" style="display: none; align-items:center; justify-content:center; z-index:9999;"')
modal_html = modal_html.replace('class="modal"', 'class="v-modal" style="background:#fff; border-radius:8px; width:600px; max-width:90vw; box-shadow:0 4px 20px rgba(0,0,0,0.2);"')
modal_html = modal_html.replace('class="modal-header"', 'class="v-modal-header" style="flex-direction:row;"')
modal_html = modal_html.replace('class="modal-close"', 'class="v-modal-close"')
modal_html = modal_html.replace('class="modal-body"', 'class="v-modal-body"')
modal_html = modal_html.replace('class="modal-footer"', 'class="v-modal-footer"')

# Add download button to file-display 
modal_html = modal_html.replace(
    '<div class="file-display" id="fileDisplay">파일을 선택해 주세요.</div>',
    '<div class="file-display" id="fileDisplay">파일을 선택해 주세요.</div>\n                <button type="button" class="file-button" id="fileDownload" style="display:none; background:#10b981; color:white; border-color:#10b981;">다운로드</button>'
)

# Modal toggle functions
toggle_script = """
    function openModal() {
       document.getElementById('versionModal').style.display = 'flex';
    }
    function closeModal() {
       document.getElementById('versionModal').style.display = 'none';
    }
"""

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    target = f.read()

# remove previously injected styles if any
target = re.sub(r'<style>.*?\.v-modal-overlay.*?</style>', '', target, flags=re.DOTALL)

if '</head>' in target:
    target = target.replace('</head>', f'<style>\n{modal_style}\n</style>\n</head>')

# Ensure we rewrite the onclick
target = target.replace(
    "onclick=\"location.href='version-register.html?contentId=101'\"", 
    "onclick=\"openModal()\""
)
target = target.replace(
    "onclick=\"location.href='version-register.html'\"", 
    "onclick=\"openModal()\""
)

# clean old accidental injections
target = re.sub(r'<div class="(?:v-)?modal-overlay.*?<!-- Version Registration Modal.*?(?=</body>)', '', target, flags=re.DOTALL)
target = re.sub(r'<div class="v-modal-overlay" id="versionModal".*?</script>', '', target, flags=re.DOTALL)
target = re.sub(r'function openModal\(\).*?\}', '', target, flags=re.DOTALL)

injection = f"""
  {modal_html}
  <script>
    {modal_script}
    {toggle_script}
  </script>
"""
target = target.replace('</body>', f'{injection}\n</body>')

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(target)

print("INJECT DONE PROPERLY")
