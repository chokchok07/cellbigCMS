import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    text = f.read()

# The button in the header was originally `<button class="btn btn-primary" onclick="openModal()">+ New Version</button>`
# but the JS function is named `openNewVersionModal()`.

text = text.replace('onclick="openModal()"', 'onclick="openNewVersionModal()"')

# Also delete any empty function openModal() { document.getElementById('versionModal').style.display = 'flex'; }
# in case it intercepts but fails.
m = re.search(r'function openModal\(\)\s*\{[^}]*\}', text)
if m:
    text = text.replace(m.group(0), '')
m2 = re.search(r'function closeModal\(\)\s*\{[^}]*\}', text)
if m2:
    text = text.replace(m2.group(0), '')

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed the + New Version button onclick handler.")
