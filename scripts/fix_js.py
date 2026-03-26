import os, glob

for file in glob.glob('CMS-webpage/wireframe_site/*-detail.html'):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to replace the later redeclaration
    content = content.replace("const deleteBtn = document.querySelector('.btn-secondary[onclick*=\"elete\"]');", "// previously old delete btn selection")
    content = content.replace("const deleteBtn = document.querySelector('.action-btn-danger');", "// old")
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)
