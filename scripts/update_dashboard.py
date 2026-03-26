import os
import glob
import re

def update_dashboard():
    base_dir = r"CMS-webpage\wireframe_site"
    
    # 1. Update index.html main content
    index_path = os.path.join(base_dir, 'index.html')
    with open(index_path, 'r', encoding='utf-8') as f:
        index_html = f.read()
    
    welcome_main = """    <main class="main-content" style="display:flex; justify-content:center; align-items:center; height:calc(100vh - 60px);">
      <div style="text-align:center;">
        <h1 style="font-size:32px; color:#1f2937; margin-bottom:10px;">👋 Welcome, 홍길동!</h1>
        <p style="color:#6b7280; font-size:16px;">셀빅 CMS 어드민 사이트에 오신 것을 환영합니다.</p>
      </div>
    </main>"""
    
    # Replace the existing main block
    index_html = re.sub(r'<main class="main-content">.*?</main>', welcome_main, index_html, flags=re.DOTALL)
    
    # Also if the overview page is a duplicate, we could do it too, or just leave it. 
    # The requirement said "dashboard", which is index.html.
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(index_html)
    
    # 2. Remove Report pages link from all HTML files
    html_files = glob.glob(os.path.join(base_dir, '*.html'))
    report_tag_pattern = re.compile(r'\s*<div class="sidebar-item"[^>]*data-page="report-content-usage\.html"[^>]*>.*?</div>', re.IGNORECASE)
    
    for f_path in html_files:
        with open(f_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        new_content = report_tag_pattern.sub('', content)
        
        if content != new_content:
            with open(f_path, 'w', encoding='utf-8') as f:
                f.write(new_content)

    # 3. Delete the report file itself to clean up
    report_path = os.path.join(base_dir, 'report-content-usage.html')
    if os.path.exists(report_path):
        os.remove(report_path)
        print("Deleted report-content-usage.html")

    print("Dashboard replaced and Report link removed.")

update_dashboard()
