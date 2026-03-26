import os, glob, re

ws = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'
html_files = glob.glob(os.path.join(ws, '*.html'))

for file in html_files:
    if 'login.html' in file:
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # The existing logout button might look like:
    # onclick="alert('로그아웃 되었습니다. (Mock)'); location.href='index.html';" >로그아웃</button>
    # or something similar.
    # Let's replace the whole header button matching <button ...>로그아웃</button>
    
    def replacer(m):
        btn = m.group(0)
        # New onclick
        new_btn = re.sub(r'onclick="[^"]*"', 'onclick="if(confirm(\'로그아웃 하시겠습니까?\')) { location.href=\'login.html\'; }"', btn)
        new_btn = re.sub(r"onclick='[^']*'", 'onclick="if(confirm(\'로그아웃 하시겠습니까?\')) { location.href=\'login.html\'; }"', new_btn)
        
        # If it didn't have onclick, add it
        if 'onclick' not in new_btn:
            new_btn = new_btn.replace('<button', '<button onclick="if(confirm(\'로그아웃 하시겠습니까?\')) { location.href=\'login.html\'; }"')
            
        return new_btn

    new_content = re.sub(r'<button[^>]*>로그아웃</button>', replacer, content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
