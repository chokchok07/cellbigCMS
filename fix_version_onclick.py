import re
with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the escaped quotes inside the onclick attribute
text = text.replace(r"\'content-versions.html?id=101\'", "'content-versions.html?id=101'")

with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Done fixing quotes.")
