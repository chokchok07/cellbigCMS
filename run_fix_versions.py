import re

file_path = "CMS-webpage/wireframe_site/content-versions.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

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
    # Adding line breaks and making sure it looks somewhat ok
    return f"{prefix}<div>등록일: {date}</div>\n        <div>수정일: {date}</div>\n        <div>작성자: {author}</div>\n      </div>"

new_content = pattern.sub(replace_dates, html_content)

btn_pattern = re.compile(
    r'(<button class="btn [^>]+>⬇️ Download</button>)'
)

def add_buttons(match):
    download_btn = match.group(1)
    return f'{download_btn}\n        <button class="btn btn-outline" style="padding:4px 8px; font-size:12px;">✏️ 수정</button>\n        <button class="btn btn-outline" style="padding:4px 8px; font-size:12px; color:#ef4444; border-color:#ef4444;">🗑️ 삭제</button>'

new_content = btn_pattern.sub(add_buttons, new_content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)

print(f"File updated. Registrations found: {new_content.count('등록일')}")
