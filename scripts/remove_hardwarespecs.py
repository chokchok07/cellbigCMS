import codecs
import re

file_path = 'CMS-webpage/wireframe_site/device-editor.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    html = f.read()

# Remove the "Hardware Specs" card completely
html = re.sub(
    r'<div class="card">\s*<h2 style="font-size: 18px;.*?Hardware Specs\s*\(Meta Data\).*?</div>\s*</div>',
    '',
    html,
    flags=re.DOTALL | re.IGNORECASE
)

# Remove Right Column: Installed Packages and Event Logs
html = re.sub(
    r'<!-- Right Column: Installed Packages -->.*?(?=<!-- Metadata Section -->|</div>\s*</main>)',
    '',
    html,
    flags=re.DOTALL | re.IGNORECASE
)

# Fix double </div> from removing the second column to avoid breaking layout if any
html = html.replace(
    '<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 24px;">',
    '<div style="display: grid; grid-template-columns: 1fr; gap: 24px;">'
)


with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(html)

print("Card removed!")
