import os
import re

content_file = r'CMS-webpage\wireframe_site\content-list.html'

with open(content_file, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

replacements = [
    (r'\?.*?터\?.*?인먼트', '엔터테인먼트'),
    (r'\?.*?\(\d+\)', '👥 (3)'),
    (r'\?.*?Admin\(SP\)', '👑 Admin(SP)'),
    (r'\?.*?LocalAreas', '🏢 LocalAreas'),
    (r'\?.*?Stores', '🏪 Stores'),
    (r'\?.*?Devices', '🖥️ Devices'),
    (r'\?.*?Access Logs', '📈 Access Logs'),
    (r'\?.*?Product', '📦 Products'),
    (r'\?.*?Licenses \(Serial\)', '🔑 Licenses (Serial)'),
    (r'\?.*?Package', '🎒 Packages'),
    (r'\?.*?Content<', '📄 Content<'),
    (r'\?.*?Settings', '⚙️ Settings'),
    (r'\?.*?Overview', '📊 Overview'),
    (r'\?.*?Content Library', '📄 Content Library'),
    (r'placeholder="\?.*?Search', 'placeholder="🔍 Search'),
    (r'<th style="width:40px">\?\?.*?/th>', '<th style="width:40px"><input type="checkbox"></th>'),
    (r'<title>.*?</title>', '<title>Content List 📄 Wireframe</title>'),
    (r'<div class="thumbnail">\?.*?</div>', '<div class="thumbnail">🖼️</div>'),
    (r'\?.*?Published', '✅ Published'),
    (r'\?.*?Staged', '⏳ Staged'),
    (r'\?.*?Draft', '📝 Draft'),
    (r'\?.*?Deprecated', '🚫 Deprecated'),
    (r'\?.*?Thumbnail', '🖼️ Thumbnail'),
    (r'\?.*?Action', '⚡ Action')
]

for pat, repl in replacements:
    html = re.sub(pat, repl, html)

with open(content_file, 'w', encoding='utf-8') as f:
    f.write(html)

with open('output_verify.txt', 'w', encoding='utf-8') as out_f:
    out_f.write('Checking for any remaining block characters...\n')
    with open(content_file, 'r', encoding='utf-8') as f2:
        text = f2.read()
        lines = text.split('\n')
        remaining = False
        for i, line in enumerate(lines):
            if '?' in line:
                out_f.write(f'{i+1}: {line.strip()}\n')
                remaining = True
        if not remaining:
            out_f.write('CLEAN\n')

