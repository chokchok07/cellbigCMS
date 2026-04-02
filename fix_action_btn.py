import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Change Status button clicks (broad regex to catch variations)
html = re.sub(
    r'<button[^>]*class="action-btn"[^>]*>Change Status</button>',
    r'<button class="action-btn" onclick="openChangeStatusModal(this)">Change Status</button>',
    html
)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done matching change status")