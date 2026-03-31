with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace('<option value="child">Child (', '<option value="sensor">Sensor (')
text = text.replace('<option value="mixed">Mixed (', '<option value="etc">Etc (')

with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(text)

with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
    text2 = f.read()

text2 = text2.replace('<option value="child">Child (', '<option value="sensor">Sensor (')
text2 = text2.replace('<option value="mixed">Mixed (', '<option value="etc">Etc (')

with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
    f.write(text2)

print("Double checking labels")