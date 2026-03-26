import glob
for f_path in glob.glob('CMS-webpage/wireframe_site/*-detail.html'):
    with open(f_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'if (btnPrimary && titleEl)' in content and 'const titleEl' not in content:
        # replace titleEl with pageTitle
        content = content.replace('if (btnPrimary && titleEl)', 'if (btnPrimary && pageTitle)')
        content = content.replace('titleEl.textContent', 'pageTitle.textContent')
        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed titleEl bug in {f_path}")
