import re

fname = 'CMS-webpage/wireframe_site/package-detail.html'
with open(fname, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace any manageContents() call in the Manage button with showing manageModal
html = re.sub(
    r'<button[^>]*onclick="manageContents\(\)"[^>]*>Manage</button>',
    r'<button class="btn btn-primary" style="padding: 4px 10px; font-size: 13px;" onclick="document.getElementById(\'manageModal\').style.display = \'flex\'">Manage</button>',
    html
)

with open(fname, 'w', encoding='utf-8') as f:
    f.write(html)
print("done")
