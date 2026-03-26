import re

file_path = "CMS-webpage/wireframe_site/content-versions.html"

with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# First, ensure grid-template-columns has 4 distinct elements: Version/Notes, Artifact, Dates, Actions.
# Example from currently existing HTML:
# grid-template-columns: 2fr 1fr 1.2fr 1fr;
# Wait, let's fix it universally.
html = re.sub(r'grid-template-columns:\s*2fr 1fr 1fr(;|\s)', r'grid-template-columns: 2fr 1fr 1.5fr 1fr\1', html)
html = re.sub(r'grid-template-columns:\s*2fr 1fr 1\.2fr 1fr(;|\s)', r'grid-template-columns: 2fr 1fr 1.5fr 1fr\1', html)


# Second, split the Col 3 which might be named "Col 3: Actions & Meta" or "Col 3: Dates & Meta" now.
# Wait, in a previous step I already successfully outputted:
# <div>등록일...
# Meaning right now it might look like:
"""
    <!-- Col 3: Actions & Meta -->
    <div style="display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end;">
      <div style="text-align:right; font-size:12px; color:.*?>
        <div>등록일: 2026-03-10 14:00</div>
        <div>수정일: 2026-03-10 14:00</div>
        <div>작성자: admin@example.com</div>
      </div>
      <div style="display:flex; gap:8px;">
        ...
"""

pattern = re.compile(
    r'(<!-- Col 3.*?-->\s*)'
    r'<div style="display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end;">\s*'
    r'<div style="text-align:right; font-size:12px; color:[^>]+>\s*'
    r'<div>등록일:\s*(.*?)</div>\s*'
    r'<div>수정일:\s*(.*?)</div>\s*'
    r'<div>작성자:\s*(.*?)</div>\s*'
    r'</div>\s*'
    r'(.*?)'
    r'</div>',
    re.DOTALL
)

def build_split(match):
    prefix = match.group(1)
    date_reg = match.group(2)
    date_mod = match.group(3)
    author = match.group(4)
    buttons_raw = match.group(5).strip()
    
    return (
        f'<!-- Col 3: Dates -->\n'
        f'              <div style="font-size:13px; color:#4b5563; display:flex; flex-direction:column; gap:6px; justify-content:center; align-items:flex-start;">\n'
        f'                <div><strong>등록일:</strong> {date_reg}</div>\n'
        f'                <div><strong>수정일:</strong> {date_mod}</div>\n'
        f'                <div><strong>작성자:</strong> {author}</div>\n'
        f'              </div>\n\n'
        f'              <!-- Col 4: Actions -->\n'
        f'              <div style="display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end;">\n'
        f'                <div style="display:flex; gap:6px; justify-content:flex-end; width:100%;">\n'
        f'                  <button class="btn btn-secondary" style="padding:4px 8px; font-size:12px;">✏️ 수정</button>\n'
        f'                  <button class="btn" style="background:#ef4444; color:white; border:none; padding:4px 8px; font-size:12px; border-radius:4px;">🗑️ 삭제</button>\n'
        f'                </div>\n'
        f'                <div style="margin-top:8px; display:flex; gap:6px;">\n'
        f'                  {buttons_raw}\n'
        f'                </div>\n'
        f'              </div>'
    )

before_html = html
html = pattern.sub(build_split, html)

# And remove old edit/delete buttons if they were directly in the buttons raw block to avoid duplicates
html = re.sub(r'<button[^>]+>✏️ 수정</button>\s*', '', html)
html = re.sub(r'<button[^>]+>🗑️ 삭제</button>\s*', '', html)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)

print(f"File modified? {before_html != html}")
print(f"Col 3 splits found: {html.count('<!-- Col 3: Dates -->')}")
