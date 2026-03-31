from bs4 import BeautifulSoup
import os

filepath = 'CMS-webpage/wireframe_site/content-detail.html'
with open(filepath, 'r', encoding='utf-8') as f:
    text = f.read()
    
soup_c = BeautifulSoup(text, 'html.parser')

title = soup_c.find('title')
if title: title.string = '신규 콘텐츠 등록 - Cellbig CMS'
page_title = soup_c.find('h2', class_='text-gray-200')
if page_title: page_title.string = '신규 콘텐츠 등록'

for id in ['versionsSection', 'packagesSection', 'systemMetadataSection']:
    elem = soup_c.find(id=id)
    if elem:
        elem.decompose()

actions = soup_c.find('div', class_='flex justify-between items-center mt-6')
if actions:
    actions.clear()
    div = soup_c.new_tag('div')
    cancel = soup_c.new_tag('button', type='button', **{'class': 'btn btn-secondary mr-2'})
    cancel['onclick'] = "location.href='content-list.html'"
    cancel.string = '취소'
    btn = soup_c.new_tag('button', type='button', **{'class': 'btn btn-primary'})
    btn['onclick'] = "location.href='content-list.html'"
    btn.string = '등록'
    div.append(cancel)
    div.append(btn)
    actions.append(div)

for script in soup_c.find_all('script'):
    if script.string and 'urlParams.get' in script.string:
        script.string = 'document.addEventListener("DOMContentLoaded", () => { document.getElementById("initialUploadSection").classList.remove("hidden"); });'

with open('CMS-webpage/wireframe_site/content-create.html', 'w', encoding='utf-8') as f:
    f.write(str(soup_c))

# detail modifications
soup_d = BeautifulSoup(text, 'html.parser')

title_d = soup_d.find('title')
if title_d:
    title_d.string = '콘텐츠 상세정보 - Cellbig CMS'
page_title_d = soup_d.find('h2', class_='text-gray-200')
if page_title_d:
    page_title_d.string = '콘텐츠 상세정보'

up = soup_d.find(id='initialUploadSection')
if up: up.decompose()

for script in soup_d.find_all('script'):
    if script.string and 'urlParams.get' in script.string:
        script.string = 'document.addEventListener("DOMContentLoaded", () => { document.getElementById("systemMetadataSection").classList.remove("hidden"); document.getElementById("versionsSection").classList.remove("hidden"); document.getElementById("packagesSection").classList.remove("hidden"); });'

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(str(soup_d))

print('Done split')