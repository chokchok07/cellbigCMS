import re

file_path = 'CMS-webpage/wireframe_site/device-editor.html'
with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

name_pattern = re.compile(r'<div class="info-label"[^>]*>Name:</div>\s*<input type="text" class="input"[^>]*placeholder="예: 강남 직영점 1번 모니터">')
name_match = name_pattern.search(text)
if name_match:
    print('Found the name block!')
    text = text[:name_match.start()] + text[name_match.end():]
    
    mac_pattern = re.compile(r'<div class="form-group">\s*<label class="form-label required">MAC Address</label>')
    mac_match = mac_pattern.search(text)
    
    if mac_match:
        print('Found MAC block! Injecting Name before it...')
        formatted_name = '''<div class="form-group">
                <label class="form-label required">Name</label>
                <input type="text" class="input" style="width:100%" value="" placeholder="예: 강남 직영점 1번 모니터">
              </div>'''
        
        text = text[:mac_match.start()] + formatted_name + '\n                ' + text[mac_match.start():]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(text)
        print('Done!')
    else:
        print('Failed to find MAC block')
else:
    print('Failed to find Name block')
