import os
import re

html_list = open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8').read()
html_list = re.sub(r'location\.href=\'content-editor.html\?id=101\'', r'location.href=\'content-detail.html?id=101\'', html_list)
html_list = re.sub(r'location\.href=\"content-editor.html\?id=101\"', r'location.href=\"content-detail.html?id=101\"', html_list)

with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(html_list)

html_det = open('CMS-webpage/wireframe_site/content-detail.html', 'r', encoding='utf-8').read()
print("Updated content-list to point to content-detail.html!")
