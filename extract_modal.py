import re

fname = 'CMS-webpage/wireframe_site/package-detail.html'
with open(fname, 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'(<div class="modal-overlay" id="manageModal".*?</form>\s*</div>\s*</div>)', text, re.DOTALL)
if m:
    with open('modal_extracted.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(1))
else:
    print("Modal not found")
