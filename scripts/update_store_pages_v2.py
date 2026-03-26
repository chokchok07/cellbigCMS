import codecs
import re

# 1. Update store-list.html
print("Updating store-list.html")
with codecs.open('CMS-webpage/wireframe_site/store-list.html', 'r', 'utf-8') as f:
    list_html = f.read()

list_html = list_html.replace(
    "window.location.href = 'store-detail.html';",
    "window.location.href = 'store-editor.html';"
)

# the view/edit buttons might have been replaced too.
# Let's cleanly just do store-editor replacement for anything related to Register
# Wait, actually for view/edit row action, we need it to go to store-detail!
list_html = list_html.replace(
    "if (action === 'View') {\n            window.location.href = 'store-editor.html';",
    "if (action === 'View') {\n            window.location.href = 'store-detail.html';"
)
list_html = list_html.replace(
    "if (action === 'Edit') {\n            window.location.href = 'store-editor.html';",
    "if (action === 'Edit') {\n            window.location.href = 'store-detail.html';"
)
with codecs.open('CMS-webpage/wireframe_site/store-list.html', 'w', 'utf-8') as f:
    f.write(list_html)

# 2. Update store-detail.html 
# - Remove Postal Code
print("Updating store-detail.html")
with codecs.open('CMS-webpage/wireframe_site/store-detail.html', 'r', 'utf-8') as f:
    detail_html = f.read()

detail_html = re.sub(
    r'<div class="info-label"[^>]*>Postal Code[^<]*</div>\s*<input type="text" class="input"[^>]*>',
    '',
    detail_html,
    flags=re.IGNORECASE | re.DOTALL
)

with codecs.open('CMS-webpage/wireframe_site/store-detail.html', 'w', 'utf-8') as f:
    f.write(detail_html)

# 3. Update store-editor.html
print("Updating store-editor.html")
with codecs.open('CMS-webpage/wireframe_site/store-editor.html', 'r', 'utf-8') as f:
    editor_html = f.read()

# Change title & breadcrumbs
editor_html = re.sub(r'Store Detail', r'Create New Store', editor_html)
editor_html = re.sub(r'<div class="page-title">\s*<h1>Store Detail[^<]*</h1>', r'<div class="page-title">\n            <h1 style="margin: 0; font-size: 24px; color: #111827; font-weight: 700; display: flex; align-items: center; gap: 8px;">\n              Create New Store\n            </h1>', editor_html)

# Remove Postal Code 
editor_html = re.sub(
    r'<div class="form-group" style="flex:1">\s*<label class="form-label">Postal Code(?:.*?)</div>',
    '',
    editor_html,
    flags=re.IGNORECASE | re.DOTALL
)

# Let's remove the "right column" which has Devices Section and System Metadata
# Or maybe Connected Devices only?
editor_html = re.sub(
    r'<!-- Devices Section.*?</div>\s*</div>',
    '',
    editor_html,
    flags=re.IGNORECASE | re.DOTALL
)

# And remove 'System Metadata' as well for editor
editor_html = re.sub(
    r'<!-- Metatdata -->.*?</div>\s*</div>',
    '',
    editor_html,
    flags=re.IGNORECASE | re.DOTALL
)

# Remove Location Info (map) if it exists
editor_html = re.sub(
    r'<!-- Location Info Section -->.*?</div>',
    '',
    editor_html,
    flags=re.IGNORECASE | re.DOTALL
)

# Fix grid layout if right column is fully empty
editor_html = re.sub(
    r'<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 24px;">',
    r'<div style="display: grid; grid-template-columns: 1fr; gap: 24px;">',
    editor_html
)


with codecs.open('CMS-webpage/wireframe_site/store-editor.html', 'w', 'utf-8') as f:
    f.write(editor_html)

print("Done")
