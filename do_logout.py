import os, re
directory = 'c:/Users/user/Documents/VSCode/CellbigCMS/CellbigCMS/CMS-webpage/wireframe_site/'
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        replacement = r'\1\n      <button style="padding:4px 10px; font-size:12px; font-weight:500; color:#4b5563; background:#f9fafb; border:1px solid #d1d5db; border-radius:4px; cursor:pointer;" onclick="alert(\'로그아웃 되었습니다.\');">로그아웃</button>'
        new_content = re.sub(
            r'(<span[^>]*>[^<]*Admin\(SP\)</span>)',
            replacement,
            content
        )
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print('Updated ' + filename)
