import re

# Read the HTML
with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern to find '<button class="action-btn" onclick="window.location.href='content-editor.html?id=XXX'">View</button>'
# and replace it with two buttons: View and Ver
def replacer(match):
    href = match.group(1)
    
    # Try to extract the ID, usually href is like 'content-editor.html?id=101'
    id_part = '101'
    if '?id=' in href:
        id_part = href.split('?id=')[1]
        
    return f"""<button class="action-btn" onclick="window.location.href='{href}'">View</button>
                    <button class="action-btn" style="background:#4b5563; border-color:#4b5563; color:#fff;" onmouseover="this.style.background='#374151'" onmouseout="this.style.background='#4b5563'" onclick="window.location.href='content-versions.html?id={id_part}'">Ver</button>"""

new_text = re.sub(r'<button class="action-btn" onclick="window\.location\.href=\'([^\']+)\'">View</button>', replacer, text)

with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated content-list.html")
