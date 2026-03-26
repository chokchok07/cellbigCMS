import os
import re
import glob

workspace = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'
html_files = glob.glob(os.path.join(workspace, '*.html'))

for html_path in html_files:
    with open(html_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    sidebar_help = r'<div class="sidebar-category">Help</div>\s*<div class="sidebar-item([^>]*)" data-page="overview.html">(.*?)</div>'
    replacement = r'<div class="sidebar-category">Help</div>\n      <div class="sidebar-item\1" data-page="overview.html">\2</div>\n      <div class="sidebar-item" data-page="version-register.html">📢 Update</div>'
    
    if 'data-page="version-register.html"' not in html and 'Help</div>' in html:
        html = re.sub(sidebar_help, replacement, html)
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html)
