import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    text = f.read()

items = re.findall(r'<div class="list-group-item.*?</div>\s*</div>\s*</div>', text, re.DOTALL)
for i, item in enumerate(items):
    print(f"--- ITEM {i} ---")
    print(item)

