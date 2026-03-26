import os
import re
import glob

d = "CMS-webpage/wireframe_site"
html_files = glob.glob(f"{d}/*.html")

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Inline danger buttons -> btn-danger
    html = re.sub(
        r'class="btn btn-secondary"\s+style="color:#dc2626;\s*border-color:#fca5a5;"',
        r'class="btn btn-danger"',
        html
    )
    
    # 2. .action-btn on Cancel/Delete inside modals
    html = re.sub(
        r'class="action-btn"\s+onclick="closeDeleteModal\(\)"',
        r'class="btn btn-secondary" onclick="closeDeleteModal()"',
        html
    )
    html = re.sub(
        r'class="action-btn action-btn-danger"\s+onclick="deleteLocalArea\(\)"',
        r'class="btn btn-danger" onclick="deleteLocalArea()"',
        html
    )
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("Buttons fixed.")
