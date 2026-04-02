import re

with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the modal content bigger
html = re.sub(
    r'class="modal-content" style="([^"]*)width: 900px([^"]*)"',
    r'class="modal-content" style="\1width: 1400px; max-width: 95vw; height: 90vh\2"',
    html
)

html = re.sub(
    r'class="modal-body" style="([^"]*)"',
    r'class="modal-body" style="\1 flex-grow: 1; min-height: 0;"',
    html
)

# And give the list part better height limit if necessary
html = re.sub(
    r'<div class="content-list" style="margin-top: 10px;">',
    r'<div class="content-list" style="margin-top: 10px; max-height: calc(90vh - 250px); overflow-y: auto;">',
    html
)

with open('CMS-webpage/wireframe_site/package-detail.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated HTML logic applied.")
