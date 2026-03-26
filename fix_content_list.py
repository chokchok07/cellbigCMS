import re
with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('<button class="action-btn">View</button>', '<button class="action-btn" onclick="location.href=\'content-detail.html\'">View</button>')
with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(text)
