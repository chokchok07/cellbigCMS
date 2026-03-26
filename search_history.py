import os
import json

appdata = os.environ.get('APPDATA')
if appdata:
    history_dir = os.path.join(appdata, 'Code', 'User', 'History')
else:
    history_dir = os.path.expanduser('~/.config/Code/User/History')

target = None

if os.path.exists(history_dir):
    for d in os.listdir(history_dir):
        p = os.path.join(history_dir, d)
        if os.path.isdir(p):
            e_path = os.path.join(p, 'entries.json')
            if os.path.exists(e_path):
                try:
                    with open(e_path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    if data.get('resource', '').endswith('index.html'):
                        for entry in data.get('entries', []):
                            entry_path = os.path.join(p, entry.get('id', ''))
                            if os.path.exists(entry_path):
                                with open(entry_path, 'r', encoding='utf-8', errors='ignore') as ef:
                                    content = ef.read()
                                if '홍길동' in content or 'welcome' in content.lower():
                                    target = content
                                    break
                except Exception as e:
                    pass
            if target:
                break

with open('result.txt', 'w', encoding='utf-8') as f:
    if target:
        f.write(target)
    else:
        f.write('NOT FOUND')
