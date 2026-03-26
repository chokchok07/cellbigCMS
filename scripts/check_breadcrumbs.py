import re
import glob

files = glob.glob('CMS-webpage/wireframe_site/*-detail.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        t = file.read()
    print(f'--- {f} ---')
    match = re.search(r'(<main class="main-content">\s*<div class="container">\s*)(.*?)(<div class="page-header")', t, re.DOTALL)
    if match:
        print(match.group(2).strip())
    else:
        print('Not found')
