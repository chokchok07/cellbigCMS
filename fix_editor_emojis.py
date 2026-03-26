import os
import re

target_files = [
    r'CMS-webpage\wireframe_site\content-editor.html',
    r'CMS-webpage\wireframe_site\content-versions.html'
]

# Dictionary mapping common broken unicode patterns to corrected text with emojis
replacements = {
    '? LocalAreas': '🏢 LocalAreas',
    '? Stores': '🏪 Stores',
    '? Devices': '💻 Devices',
    '? Access Logs': '📊 Access Logs',
    '? Product': '📦 Product',
    '? Licenses (Serial)': '🔑 Licenses (Serial)',
    '? Package': '🎒 Package',
    '? Content': '🎬 Content',
    '? Settings': '⚙️ Settings',
    '? Overview': 'ℹ️ Overview',
    '? (3)': '🔔 (3)',
    '? Admin(SP)': '👤 Admin(SP)',
    '? Thumbnail': '🖼️ Thumbnail',
    '? Action': '⚡ Action',
    
    # Matching corrupted EUC-KR artifacts based on previous fix analysis
    '?몣 System Admin': '⚙️ System Admin',
    '?뫁 Users': '👥 Users',
    '?룫 Local Areas': '🏢 LocalAreas',
    '?룵 Stores': '🏪 Stores',
    '?뼢截?Devices': '💻 Devices',
    '?뱚 Content Admin': '🎬 Content Admin',
    '?벀 Products': '📦 Products',
    '?뵎 Serials': '🔑 Serials',
    '?럲 Packages': '🎒 Packages',
    '?뱞 Contents': '🎬 Contents',
    '?봽 Versions': '🔄 Versions',
    '?뱢 Access Logs': '📊 Access Logs',
    '?숋툘 Admin Settings': '⚙️ Admin Settings',
    'placeholder="? Search': 'placeholder="🔍 Search',
    '?뼹截?Thumbnail': '🖼️ Thumbnail',
    '?뱷 Draft': '📝 Draft',
    '?슟 Deprecated': '🗑️ Deprecated',
    # Other badges and emojis in forms
    '🌍 Base Configuration': '🌏 Base Configuration',
    '⚙️ System': '⚙️ System',
}

for file_path in target_files:
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # Store originally read length
    original_html = html
    
    # Apply exact string replacements
    for old, new in replacements.items():
        html = html.replace(old, new)
        
    # Apply regex replacements for lone question marks in tables/badges
    html = re.sub(r'<th[^>]*>\?</th>', r'<th><input type="checkbox"></th>', html)
    html = re.sub(r'<div class="thumbnail">\?</div>', '<div class="thumbnail">🖼️</div>', html)
        
    # Write back if changed
    if html != original_html:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(html)
        print(f"Applied fixes successfully to {file_path}")
    else:
        print(f"No broken emoji replacements were needed in {file_path}. Already clean.")

# Double-check validation
print("\nValidation Sweep:")
for file_path in target_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            # Searching for standard broken patterns still left in the file
            if re.search(r'\?\s[A-Z]', content) or '슟' in content or '룫' in content or '\ufffd' in content:
                print(f"[!] Warning: Remaining broken characters found in {file_path}")
            else:
                print(f"[*] Verified clean: {file_path}")
