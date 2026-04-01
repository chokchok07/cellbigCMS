import re

with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Clean the modal HTML block
m1 = re.search(r'<!-- New Version Modal -->.*?<div id="newVersionModal".*?</form>\s*</div>\s*</div>', text, re.DOTALL)
if m1:
    text = text.replace(m1.group(0), '')
else:
    # Try more forgiving search
    m2 = re.search(r'<div id="newVersionModal".*?</form>\s*</div>\s*</div>', text, re.DOTALL)
    if m2:
        text = text.replace(m2.group(0), '')
        # clear the leading comment if any
        text = text.replace('<!-- New Version Modal -->\n  ', '')

# 2. Clean the JS functions
m_js = re.search(r'// New Version Modal Logic\s+function openNewVersionModal\(\).*?function submitNewVersion\(\).*?}', text, re.DOTALL)
if m_js:
    text = text.replace(m_js.group(0), '')

with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
    f.write(text)
    
print("Cleaned remaining modal pieces from content-editor.html")
