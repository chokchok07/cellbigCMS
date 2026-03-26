import re

fp = "CMS-webpage/wireframe_site/styles.css"
with open(fp, 'r', encoding='utf-8') as f:
    css = f.read()

if ".action-btn-danger" not in css:
    css += "\n.action-btn-danger { color: #dc2626; border-color: #fecaca; }\n.action-btn-danger:hover { background: #fef2f2 !important; border-color: #ef4444 !important; color: #b91c1c !important; }\n"
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(css)

import glob
for file in glob.glob("CMS-webpage/wireframe_site/*-list.html"):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('btn-action btn-danger', 'action-btn action-btn-danger')
    html = html.replace('class="btn-secondary btn-danger"', 'class="action-btn action-btn-danger"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("done")
