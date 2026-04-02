import glob
from bs4 import BeautifulSoup
import os

files = [
    'CMS-webpage/wireframe_site/content-list.html',
    'CMS-webpage/wireframe_site/device-list.html',
    'CMS-webpage/wireframe_site/localarea-list.html',
    'CMS-webpage/wireframe_site/package-list.html',
    'CMS-webpage/wireframe_site/product-list.html',
    'CMS-webpage/wireframe_site/store-list.html'
]

for f in files:
    if not os.path.exists(f): continue
    
    html = open(f, 'r', encoding='utf-8').read()
    soup = BeautifulSoup(html, 'html.parser')
    entity = os.path.basename(f).replace('-list.html', '')
    
    # fix New buttons
    for btn in soup.find_all('button'):
        text = btn.get_text(strip=True).lower()
        if '+ new' in text or '신규' in text:
            # remove modal triggers
            if 'onclick' in btn.attrs:
                del btn['onclick']
            if 'data-toggle' in btn.attrs:
                del btn['data-toggle']
            if 'data-target' in btn.attrs:
                del btn['data-target']
                
            btn['onclick'] = f"location.href='{entity}-editor.html'"
            
        elif 'view' in text or '상세보기' in text:
            if 'onclick' in btn.attrs:
                del btn['onclick']
            btn['onclick'] = f"location.href='{entity}-detail.html'"
            
    with open(f, 'w', encoding='utf-8') as out:
        out.write(str(soup))
        
print("Updated all buttons safely!")
