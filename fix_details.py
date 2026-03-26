import os
import re

def fix_detail_header(html):
    # Remove the double page header mess and replace with a clean standard one
    pattern = r'<!-- Page Header -->\s*<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px">\s*<div>\s*<div class="page-header">\s*<div>\s*<h1 class="page-title">(.*?)</h1>\s*<p class="page-desc">(.*?)</p>\s*</div>\s*<div class="header-actions">\s*<!-- Actions -->\s*</div>\s*</div>\s*<div style="color:#666;font-size:14px">(.*?)</div>\s*</div>\s*<div style="display:flex;gap:8px">(.*?)</div>\s*</div>'
    
    def repl(m):
        title = m.group(1).strip()
        desc = m.group(2).strip()
        meta = m.group(3).strip()
        actions = m.group(4).strip()
        
        return f'''<!-- Page Header -->
        <div class="page-header" style="align-items: flex-start;">
          <div>
            <h1 class="page-title" style="margin-bottom: 8px;">{title}</h1>
            <div style="color:#6b7280; font-size:14px; display:flex; gap:12px; align-items:center;">
              {meta}
            </div>
          </div>
          <div class="header-actions" style="display:flex; gap:8px;">
            {actions}
          </div>
        </div>'''
        
    new_html = re.sub(pattern, repl, html, flags=re.DOTALL)
    
    # Let's also simplify .content-grid if it's too cramped, making it single column or stacked.
    # Actually, grid-template-columns: 2fr 1fr is better than 1fr 1fr for detail views.
    new_html = new_html.replace('<div class="content-grid">', '<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 24px;">')
    
    return new_html

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    if '<!-- Page Header -->' in html:
        html = fix_detail_header(html)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

process_file('CMS-webpage/wireframe_site/localarea-detail.html')
process_file('CMS-webpage/wireframe_site/store-detail.html')
print("Detail layout fixed.")
