import re

with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
    text = f.read()

c1_start = text.find('<!-- Metadata Card -->')
if c1_start == -1: c1_start = text.find('<div class="card">')
c2_start = text.find('<!-- Configuration Card -->')
if c2_start == -1: c2_start = text.find('<div class="card"', c1_start + 1)
c3_start = text.find('<!-- Versions Section')
if c3_start == -1: c3_start = text.find('<div class="card" id="versionsSection"')
c4_start = text.find('<div class="card" id="initialUploadSection">')
c5_start = text.find('<div class="card" id="packagesSection"')
c6_start = text.find('<div class="card" id="systemMetadataSection"')

actions_start = text.find('<!-- Save/Cancel Actions -->')
if actions_start == -1: actions_start = text.find('<div class="form-actions"')

b1 = text[c1_start:c2_start]
b2 = text[c2_start:c3_start]
b3 = text[c3_start:c4_start]
b4 = text[c4_start:c5_start]
b5 = text[c5_start:c6_start]
b6 = text[c6_start:actions_start]

# b6 has closing </div> for the primary container. We need to leave it out or handle it properly.
temp_b6 = b6.rstrip()
if temp_b6.endswith('</div>'):
    b6 = temp_b6[:-6]

left_col = f"""
        <div style="display: flex; flex-direction: column; gap: 24px;">
            {b1}
            {b2}
            {b4}
            {b5}
            {b6}
        </div>
"""

right_col = f"""
        <div style="display: flex; flex-direction: column; gap: 24px; position: sticky; top: 24px; align-self: start;">
            {b3}
        </div>
"""

new_grid = f"""<div style="display: grid; grid-template-columns: minmax(auto, 1fr) minmax(auto, 1fr); gap: 24px; align-items: start;">
{left_col}
{right_col}
</div>
"""

container_start = '<div style="display: flex; flex-direction: column; gap: 24px;">'
replace_start = text.rfind(container_start, 0, c1_start)

if replace_start != -1:
    new_html = text[:replace_start] + new_grid + text[actions_start:]
    
    with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Success")
else:
    print("Could not find container start")
