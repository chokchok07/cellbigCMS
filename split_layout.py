import shutil
from bs4 import BeautifulSoup
import bs4

# 1. Backup
shutil.copy('CMS-webpage/wireframe_site/content-editor.html', 'CMS-webpage/wireframe_site/content-editor.bak2.html')

html = open('CMS-webpage/wireframe_site/content-editor.html', encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all('div', class_='card')
target_cards = []
for c in cards:
    if c.find('h2'):
        target_cards.append(c)

# find container
container = soup.find(lambda tag: tag.name == 'div' and 'display: flex' in tag.get('style', '') and 'flex-direction: column' in tag.get('style', ''))
if not container:
    container = target_cards[0].parent

# Extract the cards to rebuild them
left_cards = []
right_cards = []

for c in target_cards:
    h2 = c.find('h2').text
    if '릴리즈 버전' in h2:
        right_cards.append(c)
    else:
        left_cards.append(c)

# Create layout
wrapper = soup.new_tag('div', style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: start;")
left_col = soup.new_tag('div', style="display: flex; flex-direction: column; gap: 24px;")
right_col = soup.new_tag('div', style="display: flex; flex-direction: column; gap: 24px; position: sticky; top: 24px;")

for c in left_cards:
    c.extract()
    left_col.append(c)

for c in right_cards:
    c.extract()
    right_col.append(c)

wrapper.append(left_col)
wrapper.append(right_col)

# Append wrapper to container
container.append(wrapper)

# clean up container's old style
container['style'] = "margin-bottom: 24px;" # replacing the flex list with standard block

with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
print("Layout split done!")
