import re

text = open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8').read()

print("1. Button calling openNewVersionModal:", 'openNewVersionModal()' in text)
print("2. Modal HTML block (id='newVersionModal'):", 'id="newVersionModal"' in text)
print("3. JS function openNewVersionModal:", 'function openNewVersionModal()' in text)

# Let's see the button itself
m = re.search(r'<button[^>]*>\+ New Version</button>', text)
print("Button match:", m.group(0) if m else 'Not found')

# The button in the header was originally `<button class="btn btn-primary" onclick="openModal()">+ New Version</button>`
# We might have not properly replaced `openModal()` with `openNewVersionModal()`. Let's check `openModal`.
print("Has openModal?", 'openModal()' in text)
