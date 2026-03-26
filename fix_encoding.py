import os
dir_path = 'c:/Users/user/Documents/VSCode/CellbigCMS/CellbigCMS/CMS-webpage/wireframe_site/'
for fn in os.listdir(dir_path):
    if fn.endswith('.html'):
        path = os.path.join(dir_path, fn)
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        try:
            fixed = content.encode('cp949').decode('utf-8')
            with open(path, 'w', encoding='utf-8') as f:
                f.write(fixed)
            print('Fixed', fn)
        except Exception as e:
            print('Failed to fix', fn, e)
            try:
                fixed = content.encode('cp949', errors='ignore').decode('utf-8', errors='ignore')
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(fixed)
                print('Fixed (with ignore)', fn)
            except Exception as e2:
                print('Double fail', e2)