import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<button class="btn btn-primary">+ 신규 버전 등록</button>', '<button class="btn btn-primary" onclick="openNewVersionModal()">+ 신규 버전 등록</button>')
text = text.replace('<button class="btn btn-primary">+ 신규 버전 등록 (New Version)</button>', '<button class="btn btn-primary" onclick="openNewVersionModal()">+ 신규 버전 등록 (New Version)</button>')
text = text.replace('<button class="btn btn-primary">+ Register New Version</button>', '<button class="btn btn-primary" onclick="openNewVersionModal()">+ Register New Version</button>')

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Button patched.')
