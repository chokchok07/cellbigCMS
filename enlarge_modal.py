import re

with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make the modal container wider
text = re.sub(r'<div class="modal"[^>]*>', r'<div class="modal" style="width: 1200px; max-width: 90vw; height: 90vh; display: flex; flex-direction: column;">', text)

# Find the content list container (the ul or div holding the items)
# We want to give it automatic scroll
text = re.sub(r'<ul class="list p-0 m-0"[^>]*>', r'<ul class="list p-0 m-0" style="overflow-y: auto; flex-grow: 1; min-height: 0; max-height: 500px;">', text)

with open('CMS-webpage/wireframe_site/package-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Modal enlarged successfully.")
