import re

def fix_file(target, source):
    with open(source, 'r', encoding='utf-8') as f:
        src_text = f.read()
    with open(target, 'r', encoding='utf-8') as f:
        tgt_text = f.read()

    header_match = re.search(r'(<header class="site-header">.*?</header>)', src_text, re.DOTALL)
    if header_match:
        tgt_text = re.sub(r'<header class="site-header">.*?</header>', header_match.group(1), tgt_text, flags=re.DOTALL)

    sidebar_match = re.search(r'(<aside class="sidebar">.*?</aside>)', src_text, re.DOTALL)
    if sidebar_match:
        sidebar_html = sidebar_match.group(1)
        sidebar_html = sidebar_html.replace('sidebar-item active', 'sidebar-item ')
        
        # Decide which one should be active based on target filename
        page_name = target.split('/')[-1]
        sidebar_html = sidebar_html.replace(f'sidebar-item " data-page="{page_name}"', f'sidebar-item active" data-page="{page_name}"')
        
        tgt_text = re.sub(r'<aside class="sidebar">.*?</aside>', sidebar_html, tgt_text, flags=re.DOTALL)

    tgt_text = tgt_text.replace('Content List ??Wireframe', 'Content List — Wireframe')
    tgt_text = tgt_text.replace('??/th>', '<input type="checkbox"></th>')
    tgt_text = tgt_text.replace('<div class="thumbnail">?</div>', '<div class="thumbnail">🖼️</div>')
    tgt_text = tgt_text.replace('<div class="thumbnail">?</div>', '<div class="thumbnail">🖼️</div>')
    
    with open(target, 'w', encoding='utf-8') as f:
        f.write(tgt_text)

fix_file('CMS-webpage/wireframe_site/content-list.html', 'CMS-webpage/wireframe_site/product-list.html')
