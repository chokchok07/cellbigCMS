import re
import glob
import os

def fix_lists():
    patterns = [
        r'\s*<button class="btn-action"[^>]*?>Edit</button>',
        r'\s*<button class="btn-action"[^>]*?onclick="edit[^>]*?>Edit</button>',
        r'\s*<button class="btn-action"[^>]*?onclick="window.location.href=\'[^>]*?-editor.html\?id=[^>]*?\'">Edit</button>',
        r'\s*<button class="btn-action btn-danger"[^>]*?>Delete</button>',
        r'\s*<button class="btn-action"[^>]*?color:#dc2626;[^>]*?>Delete</button>',
        r'\s*<button class="btn-action"[^>]*?color:\s*#dc2626;[^>]*?>Delete</button>',
    ]
    
    for filepath in glob.glob('CMS-webpage/wireframe_site/*-list.html'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        for pattern in patterns:
            content = re.sub(pattern, '', content)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

fix_lists()
