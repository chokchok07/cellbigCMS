import sys
html = open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8').read()

idx = html.find('function submitManageContentsNew')
print("INDEX:", idx)
with open('debug_script_location.txt', 'w', encoding='utf-8') as f:
    if idx > -1:
        f.write(html[idx-100:idx+300])
    else:
        f.write("NOT FOUND")
