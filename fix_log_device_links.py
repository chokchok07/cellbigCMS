import re
import os

with open('CMS-webpage/wireframe_site/log-content-access.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find hrefs linking to device
links = re.findall(r'href=[\'"]([^\'"]*device[^\'"]*)[\'"]', text)

print("Current device links in log-content-access.html:")
for l in links: print(l)

# Fix replacing device-editor.html mapping to device-detail.html with a query param ID so it thinks it's editing/viewing 
# (Based on standard convention in this CMS, e.g. device-detail.html?deviceId=XYZ)

text = re.sub(
    r'href="device-editor\.html"',
    r'href="device-detail.html?deviceId=D123"',
    text
)
with open('CMS-webpage/wireframe_site/log-content-access.html', 'w', encoding='utf-8') as f:
    f.write(text)
    
print("Updated log-content-access.html to point to device-detail.html")
