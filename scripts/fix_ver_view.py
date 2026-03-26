import re
import glob

for file in glob.glob("CMS-webpage/wireframe_site/*-list.html"):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = html.replace('>Ver</button>', '>View</button>')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("Ver replaced with View")
