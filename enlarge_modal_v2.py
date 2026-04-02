import re

with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make the modal huge and responsive
text = re.sub(
    r'<div class="modal" style="width: 900px; max-width: 90vw;">',
    r'<div class="modal" style="width: 1200px; max-width: 95vw; height: 90vh; display: flex; flex-direction: column;">',
    text
)
# Just in case it was already set to something else or missing style
text = re.sub(
    r'<div class="modal">\n\s*<form',
    r'<div class="modal" style="width: 1200px; max-width: 95vw; height: 90vh; display: flex; flex-direction: column;">\n          <form',
    text
)

# Ensure the form can grow and stretch
text = re.sub(
    r'<form id="manageContentsForm">',
    r'<form id="manageContentsForm" style="display: flex; flex-direction: column; h-100; flex-grow: 1;">',
    text
)

# Give the list container a dedicated scroll area instead of stretching infinitely
text = re.sub(
    r'<div class="border rounded px-3 py-2 bg-light">',
    r'<div class="border rounded px-3 py-2 bg-light" style="flex-grow: 1; overflow-y: auto; overflow-x: hidden; min-height: 400px; max-height: calc(90vh - 200px);">',
    text
)

with open('CMS-webpage/wireframe_site/package-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Check done.")
