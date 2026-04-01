import re

file_path = 'CMS-webpage/wireframe_site/device-detail.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

name_block = '''                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Name:</div>
                <input type="text" class="input" style="width:100%" value="Device-A">'''

mac_block = '''                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">MAC Address:</div>'''

# First, remove the name block from the bottom
if name_block in text:
    text = text.replace(name_block, '')
    
    # Then insert it right before the mac address
    replacement = name_block + '\n                \n' + mac_block
    text = text.replace(mac_block, replacement)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Reordered successfully!")
else:
    print("Name block not found exactly as expected.")
