import os
import glob
import re

def update_system_sidebar():
    base_dir = r"CMS-webpage\wireframe_site"
    html_files = glob.glob(os.path.join(base_dir, '*.html'))

    # Patterns to match and remove
    notice_pattern = re.compile(r'\s*<div class="sidebar-item[^>]*data-page="notice-list\.html"[^>]*>.*?</div>', re.IGNORECASE)
    users_pattern = re.compile(r'\s*<div class="sidebar-item[^>]*data-page="user-list\.html"[^>]*>.*?</div>', re.IGNORECASE)
    
    # Pattern to match Settings and replace with proper page link
    settings_pattern = re.compile(r'<div class="sidebar-item[^>]*>⚙️ Settings</div>', re.IGNORECASE)

    for f_path in html_files:
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # Step 1: Remove notice
        content = notice_pattern.sub('', content)
        # Step 2: Remove admin users
        content = users_pattern.sub('', content)
        # Step 3: Replace settings link
        # We need to make sure we don't duplicate data-page if it already has one, but currently it's just <div class="sidebar-item">⚙️ Settings</div>
        content = settings_pattern.sub('<div class="sidebar-item" data-page="settings.html">⚙️ Settings</div>', content)

        with open(f_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
    print("Sidebar updated: Notice removed, Users removed, Settings linked.")

update_system_sidebar()
