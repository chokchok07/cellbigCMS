import os
import re

def rewrite_file(filepath, is_localarea):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    # Replace header block
    header_start = html.find('<!-- Page Header -->')
    grid_start = html.find('<!-- Content Grid -->')
    
    if header_start != -1 and grid_start != -1:
        if is_localarea:
            new_header = """<!-- Page Header -->
        <div class="page-header" style="align-items: flex-start;">
          <div>
            <h1 class="page-title" style="margin-bottom: 8px;">🌏 LocalArea Detail: Seoul</h1>
            <div style="color:#6b7280; font-size:14px; display:flex; gap:12px; align-items:center;">
              <span>🌏 Active</span> • <span>8 Stores</span>
            </div>
          </div>
          <div class="header-actions" style="display:flex; gap:8px;">
            <button class="btn btn-secondary" onclick="location.href='localarea-editor.html'">Edit LocalArea</button>
            <button class="btn btn-secondary" style="color:#dc2626; border-color:#fca5a5;" onclick="showDeleteModal()">Delete LocalArea</button>
          </div>
        </div>

"""
        else:
            new_header = """<!-- Page Header -->
        <div class="page-header" style="align-items: flex-start;">
          <div>
            <h1 class="page-title" style="margin-bottom: 8px;">🏪 Store Detail: 강남 쇼룸</h1>
            <div style="color:#6b7280; font-size:14px; display:flex; gap:12px; align-items:center;">
              <span>🏢 Active</span> • <span>LocalArea: Seoul</span> • <span>3 Devices</span>
            </div>
          </div>
          <div class="header-actions" style="display:flex; gap:8px;">
            <button class="btn btn-secondary" onclick="location.href='store-editor.html'">Edit Store</button>
            <button class="btn btn-secondary" style="color:#dc2626; border-color:#fca5a5;" onclick="showDeleteModal()">Delete Store</button>
          </div>
        </div>

"""
        html = html[:header_start] + new_header + html[grid_start:]
        
    # Replace content-grid
    html = str.replace(html, '<div class="content-grid">', '<div style="display: grid; grid-template-columns: 2fr 1fr; gap: 24px;">')

    # Replace info-grid class to be a direct style grid
    html = re.sub(r'<div class="info-grid">', r'<div style="display: grid; grid-template-columns: 140px 1fr; gap: 16px 24px; align-items: start; margin-bottom: 24px;">', html)

    # Style the labels
    html = re.sub(r'<div class="info-label">(.*?)</div>', r'<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">\1</div>', html)
    
    # Style the values
    html = re.sub(r'<div class="info-value">(.*?)</div>', r'<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;">\1</div>', html)
    html = re.sub(r'<div class="info-value" style=".*?">(.*?)</div>', r'<div class="info-value" style="color: #111827; background: #f3f4f6; padding: 6px 12px; border-radius: 6px; min-height: 20px; font-family: monospace;">\1</div>', html, count=1) # Target the first specific one like ID if custom inline style was there, actually it's easier to just strip earlier inline styles if any

    # More table label styling
    html = re.sub(r'<h2>(.*?)</h2>', r'<h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px;">\1</h2>', html)
    html = re.sub(r'<h3 style=".*?">(.*?)</h3>', r'<h3 style="font-size: 16px; color: #374151; margin: 24px 0 16px 0; border-bottom: 1px solid #f3f4f6; padding-bottom: 8px;">\1</h3>', html)

    # Store cards / Device cards
    html = re.sub(
        r'<div class="store-card">', 
        r'<div style="padding: 16px; border: 1px solid #e5e7eb; border-radius: 8px; margin-bottom: 12px; background: #fafafa; transition: background 0.2s;" onmouseover="this.style.background=\'#f3f4f6\'" onmouseout="this.style.background=\'#fafafa\'">', 
        html
    )
    
    html = re.sub(
        r'<div class="store-title">(.*?)</div>', 
        r'<div style="font-weight: 600; color: #111827; font-size: 15px; margin-bottom: 8px; display:flex; align-items:center; gap:8px;">🏪 \1</div>', 
        html
    )

    html = re.sub(
        r'<div class="store-info">(.*?)</div>', 
        r'<div style="font-size: 13px; color: #4b5563; margin-bottom: 4px;">\1</div>', 
        html
    )

    html = re.sub(
        r'<div class="device-card">', 
        r'<div style="padding: 16px; border: 1px solid #e5e7eb; border-radius: 8px; margin-bottom: 12px; background: #fafafa; transition: background 0.2s;" onmouseover="this.style.background=\'#f3f4f6\'" onmouseout="this.style.background=\'#fafafa\'">', 
        html
    )

    html = re.sub(
        r'<div class="device-header">', 
        r'<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">', 
        html
    )

    html = re.sub(
        r'<div class="device-title">(.*?)</div>', 
        r'<div style="font-weight: 600; color: #1f2937; font-size: 14px;">💻 \1</div>', 
        html
    )

    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

rewrite_file('CMS-webpage/wireframe_site/localarea-detail.html', True)
rewrite_file('CMS-webpage/wireframe_site/store-detail.html', False)
print("Rewrote detail views thoroughly.")
