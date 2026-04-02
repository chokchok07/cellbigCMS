import re

fname = 'CMS-webpage/wireframe_site/package-detail.html'
with open(fname, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'(<div class="modal-overlay" id="manageModal"[\s\S]*</div>\s*</div>\s*</div>\s*</body>)', text)
if m:
    with open('temp_modal.txt', 'w', encoding='utf-8') as f:
        f.write(m.group(0))
    print("Exported to temp_modal.txt")
else:
    print("Manage modal not found")
