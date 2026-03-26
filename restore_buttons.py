import re

file_path = "CMS-webpage/wireframe_site/content-versions.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# First we need to restore what got mangled
# Since the grid is already split to 4 cols, we are now trying to find the Actions block that is empty

pattern = re.compile(
    r'(<!-- Col 4: Actions -->\s*'
    r'<div style="display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end;">\s*'
    r'<div style="display:flex; gap:6px; justify-content:flex-end; width:100%;">\s*)'
    r'(</div>)',
    re.DOTALL
)

def inject_buttons(match):
    return (
        match.group(1) + 
        f'                  <button class="btn btn-secondary" style="padding:4px 8px; font-size:12px;">✏️ 수정</button>\n'
        f'                  <button class="btn" style="background:#ef4444; color:white; border:none; padding:4px 8px; font-size:12px; border-radius:4px;">🗑️ 삭제</button>\n'
        f'                </div>'
    )

html = pattern.sub(inject_buttons, html)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Restored deleted buttons!")
