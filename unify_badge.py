import re

with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace spans in content-list to use badge styling like package-list
text = re.sub(r'<span>✅ Published\s*</span>', '<span class=\"badge badge-published\">Published</span>', text)
text = re.sub(r'<span>🟡 Test\s*</span>', '<span class=\"badge badge-test\">Test</span>', text)
text = re.sub(r'<span>⚪ Unpublished\s*</span>', '<span class=\"badge badge-unpublished\">Unpublished</span>', text)

with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Let's also enforce it on content-detail.html table
with open('CMS-webpage/wireframe_site/content-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Find any stray '✅ Published' style in the product list if they exist there
text = re.sub(r'<span>✅ Published\s*</span>', '<span class=\"badge badge-published\">Published</span>', text)
text = re.sub(r'<span>🟡 Test\s*</span>', '<span class=\"badge badge-test\">Test</span>', text)
text = re.sub(r'<span>⚪ Unpublished\s*</span>', '<span class=\"badge badge-unpublished\">Unpublished</span>', text)

with open('CMS-webpage/wireframe_site/content-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)

# Let's enforce it on product-detail.html table too
with open('CMS-webpage/wireframe_site/product-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = re.sub(r'<span style="color:#10b981">🟢 Published</span>', '<span class=\"badge badge-published\">Published</span>', text)
text = re.sub(r'<span style="color:#f59e0b">🟡 Test</span>', '<span class=\"badge badge-test\">Test</span>', text)
text = re.sub(r'<span style="color:#6b7280">⚪ Unpublished</span>', '<span class=\"badge badge-unpublished\">Unpublished</span>', text)

with open('CMS-webpage/wireframe_site/product-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Unified status badge styling!")
