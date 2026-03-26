import re

fp = "CMS-webpage/wireframe_site/localarea-editor.html"
with open(fp, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace the inner grids with form-group
html = re.sub(
    r'<div style="display: grid; grid-template-columns: 140px 1fr; gap: 16px 24px; align-items: center; margin-bottom: 24px;">\s*<div class="info-label"[^>]*>LocalArea ID:</div>\s*<input([^>]*)>',
    r'<div class="form-group">\n                <label class="form-label required">LocalArea ID</label>\n                <input\1>',
    html
)
html = re.sub(
    r'<div style="display: grid; grid-template-columns: 140px 1fr; gap: 16px 24px; align-items: center; margin-bottom: 24px;">\s*<div class="info-label"[^>]*>Name:</div>\s*<input([^>]*)>',
    r'<div class="form-group">\n                <label class="form-label required">Name</label>\n                <input\1>',
    html
)
html = re.sub(
    r'<div style="display: grid; grid-template-columns: 140px 1fr; gap: 16px 24px; align-items: center; margin-bottom: 24px;">\s*<div class="info-label"[^>]*>Country:</div>\s*<select([^>]*)>\s*(.*?)\s*</select>\s*</div>',
    r'<div class="form-group">\n                <label class="form-label required">Country</label>\n                <select\1>\n                  \2\n                </select>\n              </div>',
    html, flags=re.DOTALL
)

with open(fp, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated localarea-editor form")
