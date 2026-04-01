with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find button and see if it calls openModal or openNewVersionModal
m = re.search(r'<button class="btn btn-primary"[^>]*>\+ New Version</button>', text)
if m:
    print("Found button:", m.group(0))
else:
    print("Button not found")

has_modal = 'newVersionModal' in text
has_openModalFn = 'function openNewVersionModal' in text

print("Has newVersionModal:", has_modal)
print("Has function:", has_openModalFn)
