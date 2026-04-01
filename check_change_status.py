from bs4 import BeautifulSoup
with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f, 'html.parser')

buttons = soup.find_all(string=lambda text: text and 'Change Status' in text)
for b in buttons:
    print(b.parent.prettify())
