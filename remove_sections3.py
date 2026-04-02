import re
text = open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8').read()

text = re.sub(r'<div id="newVersionModal".*?</form>\n\s*</div>\n\s*</div>', '', text, flags=re.DOTALL)

with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("done")
