import os
import re
import glob

def process_file(filepath):
    print(f"Processing {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the input and button inside a form-group for ID
    # This is a general pattern. Let's look for `<div style="display:flex; gap:8px;">` and `<button... Generate ID/Auto Assign`
    # Replace it with simple disabled input
    
    # Let's use a simpler approach.
    # We want to replace:
    # <div style="display:flex; gap:8px;">
    #   <input type="text" class="input" style="flex:1" id="deviceId" placeholder="dev-" pattern="[a-z0-9-]+" value="">
    #   <button class="btn btn-outline" onclick="generateDeviceId()">Generate ID</button>
    # </div>
    # With:
    # <input type="text" class="input" style="width:100%; background-color:#f3f4f6;" id="deviceId" value="(서버에서 자동 생성됨)" disabled>
    
    pattern = re.compile(
        r'<div[^>]*display:\s*flex[^>]*>\s*<input[^>]*id="([^"]+)"[^>]*>\s*<button[^>]*>.*?(?:Generate|Auto Assign).*?</button>\s*</div>', 
        re.IGNORECASE | re.DOTALL
    )
    
    def replacer(match):
        id_val = match.group(1)
        # return the disabled input
        return f'<input type="text" class="input" style="width:100%; background-color:#f3f4f6;" id="{id_val}" value="(서버에서 자동 생성됨)" disabled>'

    new_content = pattern.sub(replacer, content)

    # In some files, maybe the button is not "Generate/Auto Assign" exactly but "Generate ID". It matches.
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  -> Modified")

if __name__ == "__main__":
    search_dir = r"c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site\*editor.html"
    files = glob.glob(search_dir)
    for f in files:
        process_file(f)
