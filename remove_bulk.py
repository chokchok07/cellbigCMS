import re

with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Remove Bulk Actions HTML block
bulk_actions_pattern = re.compile(r'<div class="bulk-actions">.*?</div>', re.DOTALL)
text = bulk_actions_pattern.sub('', text)

# 2. Remove checkboxes from the header
text = re.sub(r'<th style="width:40px"><input type="checkbox"></th>', '', text)

# 3. Remove checkboxes from the rows
text = re.sub(r'<td><input type="checkbox"></td>', '', text)

# 4. Remove the JavaScript for Select All and Bulk Actions
js_pattern = re.compile(
    r"// Select All functionality.*?// Sidebar navigation", 
    re.DOTALL
)
text = js_pattern.sub('// Sidebar navigation', text)

js_bulk_pattern = re.compile(
    r"// Bulk Actions Apply button.*?\}\);", 
    re.DOTALL
)
text = js_bulk_pattern.sub('', text)

# 5. Clean up any lingering bulk action IDs if any
text = text.replace("document.getElementById('selectAll')", "null")

with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Bulk actions removed.")
