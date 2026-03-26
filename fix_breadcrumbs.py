import os, re

target_dir = 'CMS-webpage/wireframe_site'
files = [f for f in os.listdir(target_dir) if f.endswith('.html')]

def get_entity(filename):
    if filename.startswith('localarea'): return '🏢 LocalAreas', 'localarea-list.html'
    if filename.startswith('store'): return '🏪 Stores', 'store-list.html'
    if filename.startswith('device'): return '🖥️ Devices', 'device-list.html'
    if filename.startswith('log') or filename.startswith('report'): return '📊 Access Logs', 'log-content-access.html'
    if filename.startswith('product'): return '📦 Product', 'product-list.html'
    if filename.startswith('serial'): return '🔑 Licenses', 'serial-list.html'
    if filename.startswith('package'): return '🎒 Package', 'package-list.html'
    if filename.startswith('content') or filename.startswith('version'): return '🎬 Content', 'content-list.html'
    if filename.startswith('notice'): return '📢 Notice', 'notice-list.html'
    if filename.startswith('settings'): return '⚙️ Settings', 'settings.html'
    return '', ''

for file in files:
    if file in ['index.html', 'overview.html']:
        continue
        
    filepath = os.path.join(target_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()

    entity_name, list_link = get_entity(file)

    # Find the title (h1)
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html, flags=re.IGNORECASE | re.DOTALL)
    if not h1_match:
        continue
        
    page_title = h1_match.group(1).strip()
    page_title_text = re.sub(r'<[^>]+>', '', page_title).strip()
    
    # 1. Remove old breadcrumbs
    html = re.sub(r'<div class="breadcrumb".*?</div>\s*', '', html, flags=re.DOTALL)
    
    # 2. Build breadcrumb
    if file == list_link or not entity_name:
        display_name = entity_name if entity_name else page_title_text
        breadcrumb_html = f'''\n        <div class="breadcrumb" style="font-size: 13px; color: #6b7280; margin-bottom: 20px; display:flex; gap:8px; align-items:center;">
          <span style="cursor:pointer; padding: 4px 8px; border-radius: 4px; transition: background 0.2s; display: flex; align-items: center;" onmouseover="this.style.background='#e5e7eb'" onmouseout="this.style.background='transparent'" onclick="location.href='index.html'">🏠 Home</span> 
          <span style="color: #d1d5db;">/</span>
          <span style="color: #374151; font-weight: 600; padding: 4px 8px;">{display_name}</span>
        </div>\n'''
    else:
        breadcrumb_html = f'''\n        <div class="breadcrumb" style="font-size: 13px; color: #6b7280; margin-bottom: 20px; display:flex; gap:8px; align-items:center;">
          <span style="cursor:pointer; padding: 4px 8px; border-radius: 4px; transition: background 0.2s; display: flex; align-items: center;" onmouseover="this.style.background='#e5e7eb'" onmouseout="this.style.background='transparent'" onclick="location.href='index.html'">🏠 Home</span> 
          <span style="color: #d1d5db;">/</span>
          <span style="cursor:pointer; padding: 4px 8px; border-radius: 4px; transition: background 0.2s;" onmouseover="this.style.background='#e5e7eb'" onmouseout="this.style.background='transparent'" onclick="location.href='{list_link}'">{entity_name}</span> 
          <span style="color: #d1d5db;">/</span>
          <span style="color: #374151; font-weight: 600; padding: 4px 8px;">{page_title_text}</span>
        </div>\n'''
    
    # 3. Inject right after `<div class="container"[^>]*>` 
    # For robust matching, we look for '<div class="container">' specifically or similar
    container_match = re.search(r'(<div class="container"[^>]*>)', html)
    if container_match:
        container_tag = container_match.group(1)
        html = html.replace(container_tag, container_tag + breadcrumb_html, 1)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(html)
            
print("Breadcrumbs injected safely.")
