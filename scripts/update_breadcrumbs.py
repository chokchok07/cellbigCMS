import glob
import re

template = '''<div class="breadcrumb" style="font-size: 13px; color: #6b7280; margin-bottom: 20px; display:flex; gap:8px; align-items:center;">
          <span style="cursor:pointer; padding: 4px 8px; border-radius: 4px; transition: background 0.2s; display: flex; align-items: center;" onmouseover="this.style.background='#e5e7eb'" onmouseout="this.style.background='transparent'" onclick="location.href='index.html'">🏠 Home</span>
          <span style="color: #d1d5db;">/</span>
          <span style="cursor:pointer; padding: 4px 8px; border-radius: 4px; transition: background 0.2s;" onmouseover="this.style.background='#e5e7eb'" onmouseout="this.style.background='transparent'" onclick="location.href='{list_file}'">{list_icon} {list_name}</span>
          <span style="color: #d1d5db;">/</span>
          <span style="color: #374151; font-weight: 600; padding: 4px 8px;">{detail_icon} {detail_name}</span>
        </div>'''

configs = {
    'localarea': ('localarea-list.html', '🏢', 'LocalAreas', '📍', 'LocalArea Detail: Seoul'),
    'store': ('store-list.html', '🏪', 'Stores', '🏪', 'Store Detail: 강남 쇼룸'),
    'product': ('product-list.html', '📦', 'Product', '📦', 'Product Detail: SandCraft'),
    'package': ('package-list.html', '🎒', 'Package', '🎒', 'Package Detail: SandCraft - 11 Items'),
    'device': ('device-list.html', '🖥️', 'Devices', '🖥️', 'Device Detail: Device-A (ID: 1234)'),
    'content': ('content-list.html', '🎬', 'Content', '🎬', 'Content Detail')
}

files = glob.glob('CMS-webpage/wireframe_site/*-detail.html')
for f in files:
    f_norm = f.replace(chr(92), '/')
    name = f_norm.split('/')[-1].replace('-detail.html', '')
    if name in configs:
        c = configs[name]
        bc = template.format(list_file=c[0], list_icon=c[1], list_name=c[2], detail_icon=c[3], detail_name=c[4])
        
        with open(f, 'r', encoding='utf-8') as file:
            t = file.read()
        
        # Remove any existing breadcrumbs
        t = re.sub(r'<div class="breadcrumb".*?</div>', '', t, flags=re.DOTALL)
        
        # Remove empty back link if it exists
        t = re.sub(r'<!--\s*Back Link\s*-->\s*<a\s+href="[^"]+"\s+class="back-link">[^<]+</a>', '', t)
        
        # Insert new breadcrumb before <div class="page-header"
        t = re.sub(r'(<div class="page-header"[^>]*>)', bc + r'\n\n        \1', t, count=1)
        
        with open(f, 'w', encoding='utf-8') as file:
            file.write(t)
        print('Updated', name)
