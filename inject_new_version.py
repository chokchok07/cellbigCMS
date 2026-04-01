from bs4 import BeautifulSoup
import re

with open('CMS-webpage/wireframe_site/content-editor.bak.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract script
m_js = re.search(r'// New Version Modal Logic\s+function openNewVersionModal\(\).*?function submitNewVersion\(\).*?\}[\s\n]*\}', text, re.DOTALL)
if not m_js:
    # fall back
    m_js = re.search(r'// New Version Modal Logic.*?// In a real scenario, this would update the version list UI dynamically\s*\}', text, re.DOTALL)

with open('extracted_modal.js', 'w', encoding='utf-8') as f:
    f.write(m_js.group(0) if m_js else "")
    
# Now, append modal and script to content-versions.html
with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    cv_html = f.read()

soup = BeautifulSoup(cv_html, 'html.parser')

if not soup.find(id='newVersionModal'):
    with open('extracted_modal.html', 'r', encoding='utf-8') as mf:
        soup.body.append(BeautifulSoup(mf.read(), 'html.parser'))

# Inject JS
js = open('extracted_modal.js', 'r', encoding='utf-8').read()
if js:
    scripts = soup.find_all('script')
    if scripts:
        scripts[-1].append("\n" + js + "\n")
    else:
        new_script = soup.new_tag('script')
        new_script.string = js
        soup.body.append(new_script)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(str(soup).replace('&times;', '×'))
