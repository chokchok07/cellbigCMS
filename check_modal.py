import re

with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    html = f.read()

m = re.search(r'<div[^>]*id="manageModal"[^>]*>[\s\S]{0,1000}', html)
with open('debug_modal_real.txt', 'w', encoding='utf-8') as f:
    f.write(m.group(0) if m else "NOT FOUND manageModal")
