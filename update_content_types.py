import re

def update_types(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    # 1. Update filter dropdowns
    text = text.replace('<option>Child</option>', '<option>Sensor</option>')
    text = text.replace('<option>Mixed</option>', '<option>Etc</option>')
    text = text.replace('<option value="child">Child</option>', '<option value="sensor">Sensor</option>')
    text = text.replace('<option value="mixed">Mixed</option>', '<option value="etc">Etc</option>')
    
    # 2. Update form dropdowns (modal and editor)
    text = text.replace('<option value="type-child">Child (다른 콘텐츠의 일부)</option>', '<option value="type-sensor">Sensor (센서 연동 콘텐츠)</option>')
    text = text.replace('<option value="type-child">Child</option>', '<option value="type-sensor">Sensor</option>')
    
    # In case there's an old mixed/child
    text = re.sub(r'<option value="type-[A-Za-z0-9]+">Mixed.*?</option>', r'<option value="type-etc">Etc (기타)</option>', text)
    
    # Add Etc option if it doesn't exist near container
    if 'type-etc' not in text and 'type-container' in text:
        text = text.replace('<option value="type-container">Container (서브 콘텐츠 포함)</option>', 
                            '<option value="type-container">Container (서브 콘텐츠 포함)</option>\n                  <option value="type-etc">Etc (기타)</option>')

    # 3. Update table cell data
    text = text.replace('<td>child</td>', '<td>sensor</td>')
    text = text.replace('<td>mixed</td>', '<td>etc</td>')
    text = text.replace('>Child<', '>Sensor<')
    text = text.replace('>Mixed<', '>Etc<')
    text = text.replace('>child<', '>sensor<')
    text = text.replace('>mixed<', '>etc<')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

update_types('CMS-webpage/wireframe_site/content-list.html')
update_types('CMS-webpage/wireframe_site/content-editor.html')
print("Content types updated successfully!")
