import os, re

target_dir = 'CMS-webpage/wireframe_site'
files = [f for f in os.listdir(target_dir) if f.endswith('.html')]

def get_category_and_entity(filename):
    if filename.startswith('localarea'): return 'Infrastructure', '🏢 LocalAreas', 'localarea-list.html'
    if filename.startswith('store'): return 'Infrastructure', '🏪 Stores', 'store-list.html'
    if filename.startswith('device'): return 'Device & Monitoring', '🖥️ Devices', 'device-list.html'
    if filename.startswith('log') or filename.startswith('report'): return 'Device & Monitoring', '📊 Access Logs', 'log-content-access.html'
    if filename.startswith('product'): return 'Contents & Product', '📦 Product', 'product-list.html'
    if filename.startswith('serial'): return 'Contents & Product', '🔑 Licenses', 'serial-list.html'
    if filename.startswith('package'): return 'Contents & Product', '🎒 Package', 'package-list.html'
    if filename.startswith('content') or filename.startswith('version'): return 'Contents & Product', '🎬 Content', 'content-list.html'
    if filename.startswith('notice'): return 'System', '📢 Notice', 'notice-list.html'
    return 'Home', '', 'index.html'

for file in files:
    if file in ['index.html', 'overview.html']:
        continue
    
    filepath = os.path.join(target_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    category, entity, list_link = get_category_and_entity(file)

    # Find the title (h1)
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, flags=re.IGNORECASE | re.DOTALL)
    if not h1_match:
        continue
        
    page_title = h1_match.group(1).strip()
    page_title_text = re.sub(r'<[^>]+>', '', page_title).strip()
    
    breadcrumb_html = f'''<div class="breadcrumb" style="font-size: 13px; color: #6b7280; margin-bottom: 20px; display:flex; gap:8px; align-items:center;">
          <span style="cursor:pointer; padding: 4px 8px; border-radius: 4px; transition: background 0.2s; display: flex; align-items: center;" onmouseover="this.style.background='#e5e7eb'" onmouseout="this.style.background='transparent'" onclick="location.href='index.html'">🏠 Home</span> 
          <span style="color: #d1d5db;">/</span>
          <span style="font-weight: 500;">{category}</span> 
          <span style="color: #d1d5db;">/</span>
          <span style="cursor:pointer; padding: 4px 8px; border-radius: 4px; transition: background 0.2s;" onmouseover="this.style.background='#e5e7eb'" onmouseout="this.style.background='transparent'" onclick="location.href='{list_link}'">{entity}</span> 
          <span style="color: #d1d5db;">/</span>
          <span style="color: #374151; font-weight: 600; padding: 4px 8px;">{page_title_text}</span>
        </div>'''
    
    # 1. Strip out older breadcrumb or back button snippets to avoid duplicates
    html = re.sub(r'<div class="breadcrumb".*?</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div[^>]*onclick="history\.back\(\)"[^>]*>.*?</div>', '', html, flags=re.DOTALL | re.IGNORECASE)
    
    # 2. Inject right after `<div class="container"...>` inside `<main class="main-content">`
    main_match = re.search(r'(<main[^>]*>.*?<div class="container"[^>]*>)', html, flags=re.DOTALL)
    if main_match:
        container_tag = main_match.group(1)
        # Using string replace strictly on the first match
        html = html.replace(container_tag, container_tag + '\n        ' + breadcrumb_html, 1)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
            
print("Breadcrumbs added to all applicable pages!")
