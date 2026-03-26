import os
import re

product_file = r'CMS-webpage\wireframe_site\product-list.html'
content_file = r'CMS-webpage\wireframe_site\content-list.html'

with open(product_file, 'r', encoding='utf-8') as f:
    product_html = f.read()

with open(content_file, 'r', encoding='utf-8') as f:
    html = f.read()

replacements = {
    '?터?인먼트': '엔터테인먼트',
    '? Overview': '📊 Overview',
    '? System Admin': '👑 System Admin',
    '? Users': '👥 Users',
    '? Local Areas': '🏢 Local Areas',
    '? Stores': '🏪 Stores',
    '? Devices': '🖥️ Devices',
    '? Content Admin': '📁 Content Admin',
    '? Products': '📦 Products',
    '? Serials': '🔑 Serials',
    '? Packages': '🎒 Packages',
    '? Contents': '📄 Contents',
    '? Versions': '🔄 Versions',
    '? Access Logs': '📈 Access Logs',
    '? Admin Settings': '⚙️ Admin Settings',
    'placeholder="? Search': 'placeholder="🔍 Search',
    '? Thumbnail': '🖼️ Thumbnail',
    '? Action': '⚡ Action',
    '>? Content Library': '>📄 Content Library',
    '>? Published': '>✅ Published',
    '>? Staged': '>⏳ Staged',
    '>? Draft': '>📝 Draft',
    '>? Deprecated': '>🚫 Deprecated',
    '<th style="width:40px">?</th>': '<th style="width:40px"><input type="checkbox"></th>',
}

for old, new in replacements.items():
    html = html.replace(old, new)

# Thumbnails in table
html = re.sub(r'<div class="thumbnail">\?</div>', '<div class="thumbnail">🖼️</div>', html)

with open(content_file, 'w', encoding='utf-8') as f:
    f.write(html)

print('Done applying replacements.')

# Verification step
with open(content_file, 'r', encoding='utf-8') as f:
    text = f.read()
    if '?' in text:
        print('Still contains ? characters:')
        lines = text.split('\n')
        for i, line in enumerate(lines):
            # check if there's a standalone ? or ? right before text
            if '?' in line:
                 print(f'{i+1}: {line.strip()}')
    else:
        print('CLEAN')
