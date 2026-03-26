import os
import glob
import re

ws = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'
html_files = glob.glob(os.path.join(ws, '*.html'))

for file in html_files:
    if 'login.html' in file: 
        continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the logout button segment. Looking at previous output, it might look like:
    # onclick="alert('로그아웃 되었습니다. (Mock)'); location.href='index.html';" 
    # Or just onclick="location.href='index.html';" inside a button that says '로그아웃'
    
    # We will look for <button ...>로그아웃</button> and replace its onclick attribute.
    # regex to match: <button type="button" [^>]* onclick="[^"]*"[^>]*>로그아웃</button>
    
    def replacer(match):
        button_tag = match.group(0)
        # remove old onclick
        new_tag = re.sub(r'onclick="[^"]*"', '', button_tag)
        # remove old onclick with single quotes (just in case)
        new_tag = re.sub(r"onclick='[^']*'", '', new_tag)
        
        # Insert the new onclick right after <button
        new_onclick = ' onclick="if(confirm(\'로그아웃 하시겠습니까?\')) { location.href=\'login.html\'; }"'
        new_tag = new_tag.replace('<button', f'<button{new_onclick}')
        return new_tag

    new_content = re.sub(r'<button[^>]*>로그아웃</button>', replacer, content)
    
    if new_content != content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Updated {os.path.basename(file)}')
