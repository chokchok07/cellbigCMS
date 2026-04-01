import re

# Read content-editor.html
with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's extract the HTML sections that contain Version List or Registration
lines = text.split('\n')
for i, line in enumerate(lines):
    if '버전' in line or 'version' in line.lower() or 'Version' in line:
        print(f"Line {i}: {line.strip()[:100]}")