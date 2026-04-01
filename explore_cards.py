from bs4 import BeautifulSoup

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')
cards = soup.find_all('div', class_='card')
for i, card in enumerate(cards):
    print(f"--- Card {i} ---")
    btn_div = card.find('div', style=lambda s: s and 'display:flex; gap:8px;' in s)
    if btn_div:
        print("Found btn div:")
        print(btn_div.prettify())
    else:
        print("No btn div found, checking actions area...")
        # Check col 3
        col3 = card.find('div', style=lambda s: s and 'display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end;' in s)
        if col3:
            print("Col 3 found:")
            print(col3.prettify())
