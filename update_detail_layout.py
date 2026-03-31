from bs4 import BeautifulSoup

filepath = 'CMS-webpage/wireframe_site/content-detail.html'
with open(filepath, 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

# 1. Update Title / Breadcrumbs
for h1 in soup.find_all('h1', class_='page-title'):
    if 'Content Detail' in h1.text:
        h1.string = '🎬 콘텐츠 상세정보'

for p in soup.find_all('p', class_='page-desc'):
    if 'View or Edit Content' in p.text:
        p.string = '콘텐츠의 상세 정보를 확인하고 수정합니다'
        
for span in soup.find_all('span'):
    if 'Content Detail' in span.text:
        span.string = '🎬 콘텐츠 상세정보'

# 2. Find versionsSection
versions_section = soup.find(id='versionsSection')
if versions_section:
    # Remove it from its current parent
    versions_section.extract()
    
    # 3. Find the right column
    # It has packagesSection inside it, we can find the parent div of packagesSection
    packages_section = soup.find(id='packagesSection')
    if packages_section and packages_section.parent:
        right_column = packages_section.parent
        # Insert versionsSection at the beginning of the right column
        right_column.insert(0, versions_section)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(str(soup))

print('Updated content-detail.html')
