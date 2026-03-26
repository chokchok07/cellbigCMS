import glob, os, re

ws = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'

def replace_id_field(match):
    # This match is meant to cover: <input type="text" id="storeId" ...> (possibly with other attrs)
    # followed by optionally some whitespace/newlines, followed by <button ...>(Generate ID|Auto Assign|ID 중복확인)</button>
    full_str = match.group(0)
    input_tag = match.group(1)
    id_match = re.search(r'id=["\']([^"\']+)["\']', input_tag)
    
    if not id_match:
        return full_str
    
    id_val = id_match.group(1)
    # Return a completely disabled input and remove the button
    # If there was a flex container or gap, leaving it is fine, the button just disappears.
    return f'<input type="text" id="{id_val}" class="form-control" value="(서버에서 자동 생성됨)" disabled style="width: 100%; padding: 8px 12px; border: 1px solid #d1d5db; border-radius: 4px; font-size: 14px; background: #f3f4f6; color: #6b7280; font-style: italic;">'

for file in glob.glob(os.path.join(ws, '*-editor.html')):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex:
    # 1. (<input[^>]*type=["']text["'][^>]*id=["'][a-zA-Z0-9_]*[Ii]d["'][^>]*>|<input[^>]*id=["'][a-zA-Z0-9_]*[Ii]d["'][^>]*type=["']text["'][^>]*>)
    # 2. \s*
    # 3. <button[^>]*>(Generate ID|Auto Assign|ID 중복확인|아이디 생성|.*ID.*)</button>
    
    # Actually, a simpler pattern:
    # Match <input ... id="somethingId" ...>  followed by whitespace and <button ... (Generate ID|Auto Assign).*</button>
    pattern = r'(<input[^>]*id=["\'][a-zA-Z0-9_]*[Ii]d["\'][^>]*>)\s*<button[^>]*>[^<]*(?:Generate ID|Auto Assign|ID|아이디)[^<]*</button>'
    
    new_content = re.sub(pattern, replace_id_field, content, flags=re.IGNORECASE)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {os.path.basename(file)}')
    else:
        print(f'No match found in {os.path.basename(file)}')
