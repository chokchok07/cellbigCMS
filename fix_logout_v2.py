import os
import glob
import re

ws = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'
html_files = glob.glob(os.path.join(ws, '*.html'))

old_str = "onclick=\"alert('로그아웃 되었습니다. (Mock)'); location.href='index.html';\">로그아웃</button>"
new_str = "onclick=\"if(confirm('로그아웃 하시겠습니까?')) { location.href='login.html'; }\">로그아웃</button>"

old_str_2 = "onclick=\"alert('로그아웃 되었습니다. (Mock)'); location.href='index.html';\""
new_str_2 = "onclick=\"if(confirm('로그아웃 하시겠습니까?')) { location.href='login.html'; }\""

# Let's also do a general regex replace to ensure we catch any spacing differences
import importlib

count = 0
for file in html_files:
    if 'login.html' in file: continue
    
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Generic replace for any button that ends with ">로그아웃</button>"
    
    def r(m):
        raw = m.group(0)
        return re.sub(r'onclick="[^"]*"', 'onclick="if(confirm(\'로그아웃 하시겠습니까?\')) { location.href=\'login.html\'; }"', raw)

    new_content = re.sub(r'<button[^>]*>로그아웃</button>', r, content)

    # Some might use single quotes or without quotes? Not likely.
    # Just in case:
    new_content = new_content.replace(old_str, new_str)
    new_content = new_content.replace(old_str_2, new_str_2)
    
    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        count += 1
        print(f"Updated {file}")

print(f"Total updated: {count}")
# Let's write output to file so I can see it even if terminal swallows stdout
with open('debug_output.txt', 'w', encoding='utf-8') as f:
    f.write(f"Total updated: {count}")
