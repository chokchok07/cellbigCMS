import re

with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    html = f.read()

# remove max-height: 80vh so height gets maxed
html = re.sub(r'max-height: 80vh;', 'max-height: 95vh;', html)

with open('CMS-webpage/wireframe_site/package-detail.html', 'w', encoding='utf-8') as f:
    f.write(html)
