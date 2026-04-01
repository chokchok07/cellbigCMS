import re

file_path = 'CMS-webpage/wireframe_site/device-editor.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

name_html1 = '''                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Name:</div>
                <input type="text" class="input" style="width:100%" value="" placeholder="예: 강남 직영점 1번 모니터">'''

name_html2 = '''<div class="form-group">\n                <label class="form-label required">Name</label>\n                <input type="text" class="input" style="width:100%" value="" placeholder="예: 강남 직영점 1번 모니터">\n              </div>'''

mac_html = '''<div class="form-group">
                <label class="form-label required">MAC Address</label>'''

if name_html1 in text:
    # Remove the old Name block (without form-group)
    text = text.replace(name_html1, "")
    
    # Prepend the properly formatted Name block before MAC Address
    text = text.replace(mac_html, name_html2 + '\n                \n                ' + mac_html)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Reordered device-editor successfully!")
else:
    print("Could not find the Name block as expected.")
