import os

# Configuration
directory = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'
styles_file = os.path.join(directory, 'styles.css')

# Sidebar CSS to add/ensure in styles.css
sidebar_css = """
/* Sidebar Styles */
.dashboard-layout{display:flex;min-height:100vh}
.sidebar{width:180px;background:#fff;border-right:1px solid #e6eef8;padding:16px;flex-shrink:0;}
.sidebar-header{font-weight:700;font-size:16px;margin-bottom:20px;color:#1f2937}
.sidebar-category{font-weight:600;font-size:11px;color:#6b7280;margin:20px 0 8px;text-transform:uppercase;letter-spacing:0.5px;}
.sidebar-item{padding:8px 10px;margin:2px 0;border-radius:6px;cursor:pointer;display:flex;align-items:center;gap:8px;font-size:14px;color:#374151;text-decoration:none;}
.sidebar-item:hover{background:#f3f4f6;color:#111827;}
.sidebar-item.active{background:#eff6ff;color:#2563eb;font-weight:500;}
.main-content{flex:1;background:#f6f8fa;overflow-x:hidden;}
"""

# New Sidebar HTML Template
sidebar_template = """
    <aside class="sidebar">
      
      <div class="sidebar-category">Infrastructure (Location)</div>
      <div class="sidebar-item {localarea_active}" data-page="localarea-list.html">🌏 LocalAreas</div>
      <div class="sidebar-item {store_active}" data-page="store-list.html">🏪 Stores</div>
      
      <div class="sidebar-category">Device & Monitoring</div>
      <div class="sidebar-item {device_active}" data-page="device-list.html">💻 Devices</div>
      <div class="sidebar-item {access_log_active}" data-page="log-content-access.html">📊 Access Logs</div>
      <div class="sidebar-item" data-page="report-content-usage.html">📈 Reports</div>

      <div class="sidebar-category">Contents & Product</div>
      <div class="sidebar-item {product_active}" data-page="product-list.html">🏢 Product</div>
      <div class="sidebar-item {serial_active}" data-page="serial-list.html">🔑 Licenses (Serial)</div>
      <div class="sidebar-item {package_active}" data-page="package-list.html">📦 Package</div>
      <div class="sidebar-item {content_active}" data-page="content-list.html">📝 Content</div>
      
      <div class="sidebar-category">System</div>
      <div class="sidebar-item {notice_active}" data-page="notice-list.html">📢 Notice</div>
      <div class="sidebar-item">⚙️ Settings</div>

      <div class="sidebar-category">Help</div>
      <div class="sidebar-item {overview_active}" data-page="overview.html">ℹ️ Overview</div>
    </aside>
"""

def update_styles():
    print(f"Updating {styles_file}...")
    try:
        with open(styles_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if '.sidebar-category' not in content:
            with open(styles_file, 'a', encoding='utf-8') as f:
                f.write("\n" + sidebar_css)
            print("  Added sidebar styles to styles.css")
        else:
            print("  Sidebar styles already present in styles.css")
    except Exception as e:
        print(f"  Error updating styles.css: {e}")

def get_active_mapping(filename):
    mapping = {
        'dashboard_active': '',
        'localarea_active': '',
        'store_active': '',
        'device_active': '',
        'product_active': '',
        'package_active': '',
        'content_active': ''
    }
    
    filename = filename.lower()
    if 'dashboard.html' in filename:
        mapping['dashboard_active'] = 'active'
    elif 'localarea' in filename:
        mapping['localarea_active'] = 'active'
    elif 'store' in filename:
        mapping['store_active'] = 'active'
    elif 'device' in filename:
        mapping['device_active'] = 'active'
    elif 'product' in filename:
        mapping['product_active'] = 'active'
    elif 'package' in filename:
        mapping['package_active'] = 'active'
    elif 'content' in filename:
        mapping['content_active'] = 'active'
        
    return mapping

def update_html_files():
    import re
    print("Updating HTML files...")
    
    # Regex for Sidebar - finding the aside block
    sidebar_pattern = re.compile(r'<aside class="sidebar">.*?</aside>', re.DOTALL)
    
    # Regex for Style block - looking for a style block that contains .sidebar definition
    # We use [^<]* instead of .* to ensure we don't cross into other tags if possible, 
    # but since inside style there are no tags, we mainly want to ensure we don't start at one <style> and end at another </style> with content in between?
    # Actually, simpler approach: Read the file, find the style block content that has .sidebar.
    # Pattern: <style[^>]*>(.*?)</style>
    style_pattern = re.compile(r'<style[^>]*>(.*?)</style>', re.DOTALL)

    count = 0
    file_list = [f for f in os.listdir(directory) if f.endswith('.html')]

    for filename in file_list:
        filepath = os.path.join(directory, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            
            # 1. Update Sidebar
            # Determine active state
            mapping = {
                'dashboard_active': '', 'localarea_active': '', 'store_active': '', 
                'device_active': '', 'product_active': '', 'package_active': '', 
                'content_active': '', 'overview_active': '', 'notice_active': '',
                'serial_active': '', 'access_log_active': ''
            }
            
            fn_lower = filename.lower()
            if 'index.html' in fn_lower or 'dashboard' in fn_lower: mapping['dashboard_active'] = 'active'
            elif 'overview' in fn_lower: mapping['overview_active'] = 'active'
            elif 'notice' in fn_lower: mapping['notice_active'] = 'active'
            elif 'log-content-access' in fn_lower: mapping['access_log_active'] = 'active'
            elif 'localarea' in fn_lower: mapping['localarea_active'] = 'active'
            elif 'store' in fn_lower: mapping['store_active'] = 'active'
            elif 'device' in fn_lower: mapping['device_active'] = 'active'
            elif 'product' in fn_lower: mapping['product_active'] = 'active'
            elif 'serial' in fn_lower: mapping['serial_active'] = 'active'
            elif 'package' in fn_lower: mapping['package_active'] = 'active'
            elif 'content' in fn_lower: mapping['content_active'] = 'active'

            # Build new sidebar string
            # We do this manually to avoid format() issues if the HTML somehow has unrelated braces (though unlikely in HTML outside script)
            # But sidebar_template has {} placeholders, so format is correct.
            # Double check sidebar_template doesn't have other braces. It has CSS classes usage? No, only placeholders.
            new_sidebar = sidebar_template.format(**mapping).strip()
            
            # Replace sidebar
            if sidebar_pattern.search(content):
                content = sidebar_pattern.sub(new_sidebar, content)
            else:
                print(f"    Warning: No <aside class='sidebar'> found in {filename}")

            # 2. Cleanup specific style block
            # logical approach: find all style blocks. if a block contains ".sidebar", remove the hole block.
            def replace_style(match):
                inner = match.group(1)
                if '.sidebar' in inner and '.dashboard-layout' in inner: # Be specific to avoid removing other styles
                    return '' # Remove the block
                return match.group(0) # Keep it
            
            content = style_pattern.sub(replace_style, content)

            # Write back if changed
            if content != original_content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"    Updated {filename}")
                count += 1
            else:
                print(f"    No changes needed for {filename}")

        except Exception as e:
            print(f"    Error processing {filename}: {e}")
    
    print(f"Finished. Updated {count} files.")

if __name__ == "__main__":
    update_styles()
    update_html_files()
