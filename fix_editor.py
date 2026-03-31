from bs4 import BeautifulSoup
import os

filepath = 'CMS-webpage/wireframe_site/content-editor.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure we don't mess up JS or inline stuff if we don't have to, but BS4 is good.
soup = BeautifulSoup(text, 'html.parser')

# Update titles
for title in soup.find_all('title'):
    if 'Content Editor' in title.text:
        title.string = '콘텐츠 상세정보 — CellbigCMS'

for h1 in soup.find_all('h1', class_='page-title'):
    if 'Content Editor' in h1.text:
        h1.string = '🎬 콘텐츠 상세정보'

for p in soup.find_all('p', class_='page-desc'):
    if 'Create New Content' in p.text:
        p.string = '콘텐츠의 상세 정보를 확인하고 수정합니다'
        
for span in soup.find_all('span'):
    if 'Content Editor' in span.text or 'Create Content' in span.text:
        span.string = '🎬 콘텐츠 상세정보'

# Move versionsSection
versions = soup.find(id='versionsSection')
if versions:
    versions.extract()
    packages = soup.find(id='packagesSection')
    if packages and packages.parent:
        packages.parent.insert(0, versions)
    else:
        meta = soup.find(id='systemMetadataSection')
        if meta and meta.parent:
            meta.parent.insert(0, versions)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Fixed content-editor.html")
