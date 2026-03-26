import re

file_path = "CMS-webpage/wireframe_site/content-versions.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# First, let's fix the duplicated buttons and broken dates if they exist.
# Remove all our inserted buttons:
html_content = re.sub(
    r'\s*<button class="btn btn-outline" style="padding:4px 8px; font-size:12px;">✏️ 수정</button>',
    '', html_content
)
html_content = re.sub(
    r'\s*<button class="btn btn-outline" style="padding:4px 8px; font-size:12px; color:#ef4444; border-color:#ef4444;">🗑️ 삭제</button>',
    '', html_content
)
# Revert registration date modifications.
html_content = re.sub(
    r'<div>등록일:\s*(.*?)</div>\s*<div>수정일:\s*(.*?)</div>\s*<div>작성자:\s*(.*?)</div>',
    r'<div>Created: \1</div>\n                  <div>By: \3</div>',
    html_content
)

# Now apply fresh
# Pattern to find the created/by block
pattern = re.compile(
    r'(<div style="text-align:right; font-size:12px; color:.*?>\s*)'
    r'<div>Created:\s*(.*?)</div>\s*'
    r'<div>By:\s*(.*?)</div>\s*'
    r'(</div>)',
    re.DOTALL
)

def replace_dates(match):
    prefix = match.group(1)
    date = match.group(2)
    author = match.group(3)
    suffix = match.group(4)
    return (f"{prefix}"
            f"<div>등록일: {date}</div>\n"
            f"                  <div>수정일: {date}</div>\n"
            f"                  <div>작성자: {author}</div>\n"
            f"                {suffix}")

new_content = pattern.sub(replace_dates, html_content)


btn_pattern = re.compile(
    r'(<button class="btn [^>]+>⬇️ Download</button>)'
)

def add_buttons(match):
    download_btn = match.group(1)
    return (f'{download_btn}\n'
            f'                  <button class="btn btn-outline" style="padding:4px 8px; font-size:12px;">✏️ 수정</button>\n'
            f'                  <button class="btn btn-outline" style="padding:4px 8px; font-size:12px; color:#ef4444; border-color:#ef4444;">🗑️ 삭제</button>')

new_content = btn_pattern.sub(add_buttons, new_content)

print("Found date matches?", pattern.search(html_content) is not None)
print("Found button matches?", btn_pattern.search(new_content) is not None)

if new_content != html_content:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Cleaned up and reapplied replacements successfully!")
else:
    print("No changes needed or regex failed.")
