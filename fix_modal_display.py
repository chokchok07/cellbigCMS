import re

with open('CMS-webpage/wireframe_site/version-register.html', 'r', encoding='utf-8') as f:
    orig = f.read()

# Extract modal parts
style_match = re.search(r'<style>(.*?)</style>', orig, re.DOTALL)
html_match = re.search(r'(<div class="modal-overlay">.*?)<script>', orig, re.DOTALL)
script_match = re.search(r'<script>(.*?)</script>\s*</body>', orig, re.DOTALL)

modal_style = style_match.group(1) if style_match else ''
modal_html = html_match.group(1) if html_match else ''
modal_script = script_match.group(1) if script_match else ''

# Fix CSS conflicting classes
modal_style = modal_style.replace('.modal-overlay', '.v-modal-overlay')
modal_style = modal_style.replace('.modal {', '.v-modal {')
modal_style = modal_style.replace('.modal-header', '.v-modal-header')
modal_style = modal_style.replace('.modal-close', '.v-modal-close')
modal_style = modal_style.replace('.modal-body', '.v-modal-body')
modal_style = modal_style.replace('.modal-footer', '.v-modal-footer')

# IMPORTANT FIX: .modal is defined as `display: none` in styles.css.
# Change our modal classes to v-modal to avoid any clash.
modal_html = modal_html.replace('class="modal-overlay"', 'class="v-modal-overlay" id="versionModal" style="display: none;"')
modal_html = modal_html.replace('class="modal"', 'class="v-modal"')
modal_html = modal_html.replace('class="modal-header"', 'class="v-modal-header"')
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

# remove previously injected styles if any (to be safe)
# mostly we just append

if '<style>' in target:
    target = target.replace('</style>', f'{modal_style}\n</style>')
else:
    target = target.replace('</head>', f'<style>{modal_style}</style>\n</head>')

# Ensure we rewrite the onclick
target = target.replace(
    "onclick=\"location.href='version-register.html?contentId=101'\"", 
    "onclick=\"openModal()\""
)
target = target.replace(
    "onclick=\"location.href='version-register.html'\"", 
    "onclick=\"openModal()\""
)

# Append modal logic before </body>
injection = f"""
  {modal_html}
  <script>
    {modal_script}
    {toggle_script}
  </script>
"""
# clean old accidental injections
target = re.sub(r'<!-- Version Registration Modal -->.*?</script>', '', target, flags=re.DOTALL)

target = target.replace('</body>', f'{injection}\n</body>')

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(target)

print("INJECT DONE")
