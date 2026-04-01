with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

out = []
in_modal = False
in_js = False

for line in lines:
    if '<!-- New Version Modal -->' in line:
        in_modal = True
        
    if '// New Version Modal Logic' in line:
        in_js = True
        
    if not in_modal and not in_js:
        out.append(line)
        
    if in_modal and '</form>' in line:
        # read two more </div>
        # actually let's just close modal on <div class="page-footer"?
        pass
    
    if in_modal and '</div>' in line:
        # maybe we close when we hit the script tag or something? No, we need a counter.
        pass

# Instead of line by line, let's use bs4 now that it's installed.
from bs4 import BeautifulSoup
with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

modal = soup.find(id='newVersionModal')
if modal:
    modal.decompose()

# Clean JS using regex
import re
html = str(soup)
m = re.search(r'// New Version Modal Logic.*?function submitNewVersion\(\).*?\}[\s\n]*\}', html, re.DOTALL)
if m:
    html = html.replace(m.group(0), '')
else:
    # Try more generic regex
    m = re.search(r'// New Version Modal Logic.*?// In a real scenario, this would update the version list UI dynamically\s*\}', html, re.DOTALL)
    if m:
        html = html.replace(m.group(0), '')

with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
    f.write(html)
