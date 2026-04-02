import os
import glob
import re

def process_step_1():
    base_dir = r"CMS-webpage\wireframe_site"
    html_files = glob.glob(os.path.join(base_dir, '*.html'))
    
    for idx, f in enumerate(html_files):
        with open(f, 'r', encoding='utf-8') as file:
            html = file.read()
        
        orig_html = html
        
        # Fixing pagination center alignment
        # Search for <div style="... justify-content: space-between; ..."><ul class="pagination">
        # Or <div class="pagination-wrapper" style="justify-content: flex-end;">
        # Let's use a simpler regex
        html = re.sub(r'(<div[^>]*style="[^"]*)justify-content:\s*(?:space-between|flex-end)([^"]*"[^>]*>\s*<ul class="pagination">)', r'\1justify-content: center\2', html)
        html = re.sub(r'(<div[^>]*style=\'[^\']*)justify-content:\s*(?:space-between|flex-end)([^\']*\'[^>]*>\s*<ul class="pagination">)', r'\1justify-content: center\2', html)
        
        # Add sidebar routing JS if completely missing (it usually exists inline)
        # Assuming most HTMLs already have document.querySelectorAll('.sidebar-item').forEach...
        
        if html != orig_html:
            with open(f, 'w', encoding='utf-8') as file:
                file.write(html)
            print(f"Step 1 Applied to {os.path.basename(f)}")

process_step_1()
