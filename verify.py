import re

content_file = r'CMS-webpage\wireframe_site\content-list.html'

with open(content_file, 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
for i, line in enumerate(lines):
    if '?' in line and '.html?' not in line:
        print(f'{i+1}: {line.strip()}')

print("DONE")
