import os
import re

content_file = r'CMS-webpage\wireframe_site\content-list.html'

with open(content_file, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace missing characters with standard emojis
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

# Thumbnails and Status Badges
html = re.sub(r'<div class="thumbnail">\?</div>', '<div class="thumbnail">🖼️</div>', html)
html = html.replace('<span class="status-badge status-published">?</span>', '<span class="status-badge status-published">✅</span>')
html = html.replace('<span class="status-badge status-staged">?</span>', '<span class="status-badge status-staged">⏳</span>')
html = html.replace('<span class="status-badge status-draft">?</span>', '<span class="status-badge status-draft">📝</span>')
html = html.replace('<span class="status-badge status-deprecated">?</span>', '<span class="status-badge status-deprecated">🚫</span>')

# Handle <title> and header texts
html = html.replace('Content List ? Wireframe', 'Content List 📄 Wireframe')

with open(content_file, 'w', encoding='utf-8') as f:
    f.write(html)

# Check for any remaining ?
with open('output3.txt', 'w', encoding='utf-8') as out_f:
    out_f.write('Verifying replacements...\n')
    
    with open(content_file, 'r', encoding='utf-8') as f2:
        text = f2.read()
        if '?' in text:
            out_f.write('Still contains ? characters:\n')
            lines = text.split('\n')
            for i, line in enumerate(lines):
                if '?' in line:
                    out_f.write(f'{i+1}: {line.strip()}\n')
        else:
            out_f.write('CLEAN\n')

