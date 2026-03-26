import re
import glob

fp = "CMS-webpage/wireframe_site/styles.css"
with open(fp, 'r', encoding='utf-8') as f:
    css = f.read()

if ".action-btn-success" not in css:
    css += "\n.action-btn-success { color: #059669; border-color: #a7f3d0; }\n.action-btn-success:hover { background: #ecfdf5 !important; border-color: #10b981 !important; color: #047857 !important; }\n"
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(css)

for file in glob.glob("CMS-webpage/wireframe_site/*-list.html"):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Replace invalid btn-action with action-btn
    html = html.replace('btn-action', 'action-btn')
    
    # For Active buttons with inline style
    html = re.sub(
        r'class="action-btn"\s+style="color:#059669;border-color:#059669"',
        r'class="action-btn action-btn-success"',
        html
    )

    # In case there are other inline styles for View/Active buttons
    html = re.sub(
        r'class="action-btn"\s+style="[^"]*?"',
        r'class="action-btn"',
        html
    )

    # For any remaining that might not have class added but are just missing styles:
    # (Checking standard)

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("styles and views/actives fixed")
