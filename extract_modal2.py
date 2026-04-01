import re

with open('CMS-webpage/wireframe_site/content-editor.bak.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'<!-- New Version Modal -->.*?(<div id="newVersionModal".*?</form>\s*</div>\s*</div>)', text, re.DOTALL)
if not m:
    m = re.search(r'<div id="newVersionModal".*?</form>\s*</div>\s*</div>', text, re.DOTALL)

if m:
    print(len(m.group(0)))
    with open('extracted_modal.html', 'w', encoding='utf-8') as f:
        f.write(m.group(0))
else:
    print("still not found")
