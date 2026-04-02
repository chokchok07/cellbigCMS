import os
html = open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8').read()

print("Location:", html.find("function submitManageContentsNew"))
