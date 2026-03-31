import os
import glob
import re

html_files = glob.glob('CMS-webpage/wireframe_site/*.html')

sidebar_pattern = re.compile(r'<div class="sidebar-item([^"]*)" data-page="overview\.html">.*?Overview</div>', re.DOTALL)
new_sidebar_html = r'<div class="sidebar-item\1" data-page="notice-list.html">📢 Notice</div>'

# 1. Replace in all HTML files
for file in html_files:
    if file.endswith('notice-list.html'):
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = sidebar_pattern.sub(new_sidebar_html, content)
    
    # Actually, overview might have been the active tab in index.html (which got renamed), let's just make sure.
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)

print("Sidebar updated to Notice.")
