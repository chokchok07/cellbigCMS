import re
import glob
import os

def fix_list_actions(filepath):
    if not os.path.exists(filepath):
        return
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Replace action columns that have View, Edit, Delete
    # We want to keep just View and maybe add a toggle if missing, or just View if status is elsewhere.
    # Actually, LocalArea used a switch. But let's just make sure "Edit" and "Delete" buttons are removed in the Actions td.
    
    # We will regex replace standard action tds
    new_content = re.sub(
        r'<button class="btn-action"[^>]*?onclick=".*?edit.*?".*?>\s*Edit\s*</button>',
        '',
        content,
        flags=re.IGNORECASE | re.DOTALL
    )
    new_content = re.sub(
        r'<button class="btn-action" style="color:\s*#dc2626;".*?>\s*Delete\s*</button>',
        '',
        new_content,
        flags=re.IGNORECASE | re.DOTALL
    )
    new_content = re.sub(
        r'<button class="btn-action"[^>]*?onclick=".*?delete.*?".*?>\s*Delete\s*</button>',
        '',
        new_content,
        flags=re.IGNORECASE | re.DOTALL
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

for filepath in glob.glob("CMS-webpage/wireframe_site/*-list.html"):
    fix_list_actions(filepath)

