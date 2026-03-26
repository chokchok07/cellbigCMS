import re

def polish_html(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    # Redesign basic info grid inside cards to space out labels and values cleanly.
    # We will wrap it in a cleaner grid if it's currently hard to read.
    
    # Let's replace <div class="info-grid"> with <div style="display: grid; grid-template-columns: 140px 1fr; gap: 16px 24px; align-items: center;">
    html = str.replace(html, '<div class="info-grid">', '<div style="display: grid; grid-template-columns: 140px 1fr; gap: 16px 24px; align-items: start; margin-bottom: 24px;">')

    # Add subtle bottom borders to values or change typography for readability
    html = re.sub(r'<div class="info-label">(.*?)</div>', r'<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">\1</div>', html)
    html = re.sub(r'<div class="info-value">(.*?)</div>', r'<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;">\1</div>', html)
    
    # Store card designs in the right column
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
    
    html = re.sub(r'<button class="action-btn" (.*?)>(.*?)</button>', r'<button class="btn btn-outline" style="width: 100%; padding: 6px; font-size: 13px;" \1>\2</button>', html)

    # Make table labels (h2, h3) cleaner
    html = re.sub(r'<h2>(.*?)</h2>', r'<h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px;">\1</h2>', html)
    html = re.sub(r'<h3 style=".*?">(.*?)</h3>', r'<h3 style="font-size: 16px; color: #374151; margin: 24px 0 16px 0; border-bottom: 1px solid #f3f4f6; padding-bottom: 8px;">\1</h3>', html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

for file in ['localarea-detail.html', 'store-detail.html']:
    polish_html('CMS-webpage/wireframe_site/' + file)

print("Polished detail forms.")
