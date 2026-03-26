import codecs
import re

file_path = 'CMS-webpage/wireframe_site/device-editor.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    html = f.read()

# 1. Replace the "Package:" text input with a select dropdown
html = re.sub(
    r'<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">(?:Package|Product):</div>\s*<input type="text" class="input" style="width:100%" value=".*?">',
    r'<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Type:</div>\n                  <select class="input" style="width:100%">\n                    <option value="Product">Product</option>\n                    <option value="Package">Package</option>\n                  </select>',
    html,
    flags=re.IGNORECASE
)

# 2. Remove the "Hardware Specs" card
html = re.sub(
    r'<div class="card" style="margin-top: 24px;">\s*<h2 style="font-size: 18px;.*?Hardware Specs(?:.*?)</h2>.*?</div>\s*</div>',
    '',
    html,
    flags=re.DOTALL | re.IGNORECASE
)

# 3. Remove the "Installed Packages" / "Event Logs" right column. It starts with <!-- Right Column: Installed Packages -->
html = re.sub(
    r'<!-- Right Column: Installed Packages -->.*?(?=<!-- Metadata Section -->|</div>\s*</main>)',
    '',
    html,
    flags=re.DOTALL | re.IGNORECASE
)

# Also fix the grid layout to not have 2 columns if the right column is gone.
html = re.sub(
    r'<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 24px;">',
    r'<div style="display: grid; grid-template-columns: 1fr; gap: 24px;">',
    html
)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(html)

print("Updated device-editor.html successfully.")
