import os, glob

ws = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'
html_files = glob.glob(os.path.join(ws, '*.html'))

if not html_files:
    print("No files found!")
else:
    for file in html_files:
        with open(file, 'r', encoding='utf-8') as f:
            content = f.read()
        print(f"{os.path.basename(file)}: has 로그아웃 ? {'로그아웃' in content}")
