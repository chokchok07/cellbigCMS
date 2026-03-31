import re
from bs4 import BeautifulSoup
import bs4

html = open('CMS-webpage/wireframe_site/content-editor.html', encoding='utf-8').read()
soup = BeautifulSoup(html, 'html.parser')

cards = soup.find_all(lambda tag: tag.name == 'div' and 'card' in tag.get('class', []))

print(len(cards))

left_cards = []
right_cards = []

for c in cards:
    h2 = c.find('h2')
    if h2 and '릴리즈 버전' in h2.text:
        right_cards.append(c)
    else:
        left_cards.append(c)

print(len(left_cards), len(right_cards))

wrapper = soup.new_tag('div', style="display: grid; grid-template-columns: 1fr 1fr; gap: 24px; align-items: start;")
left_col = soup.new_tag('div', style="display: flex; flex-direction: column; gap: 24px;")
right_col = soup.new_tag('div', style="display: flex; flex-direction: column; gap: 24px; position: sticky; top: 24px;")

wrapper.append(left_col)
wrapper.append(right_col)

# We must replace them in place to not mess up the parent
parent = cards[0].parent
parent['style'] = "margin-bottom: 24px;" # replace flex

# Insert wrapper before the first card
cards[0].insert_before(wrapper)

# Move elements into columns
for c in left_cards:
    c.extract()
    left_col.append(c)

for c in right_cards:
    c.extract()
    right_col.append(c)

with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
    f.write(soup.decode(formatter="html"))

print("Done")