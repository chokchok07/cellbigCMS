import re
with open('CMS-webpage/wireframe_site/version-register.html', 'r', encoding='utf-8') as f:
    text = f.read()
text = text.replace('onclick="openModal()"', 'onclick="location.href=\'version-editor.html\'"')
with open('CMS-webpage/wireframe_site/version-register.html', 'w', encoding='utf-8') as f:
    f.write(text)
