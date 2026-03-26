import os
import glob
import re

def fix_sidebar_nav():
    base_dir = r"CMS-webpage\wireframe_site"
    html_files = ["user-list.html", "user-editor.html"]

    script_block = """  <script>
    // Sidebar navigation
    document.querySelectorAll('.sidebar-item').forEach(item => {
      item.addEventListener('click', function() {
        const page = this.getAttribute('data-page');
        if (page) {
          window.location.href = page;
        }
      });
    });
  </script>"""

    for f_name in html_files:
        f_path = os.path.join(base_dir, f_name)
        if os.path.exists(f_path):
            with open(f_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Replace the wrong scripts or add the inline one
            if '<script src="app.js"></script>' in content:
                content = content.replace('<script src="app.js"></script>', script_block)
                with open(f_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    print(f"Fixed {f_name}")
            elif 'Sidebar navigation' not in content:
                content = content.replace('</body>', script_block + '\n</body>')
                with open(f_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                    print(f"Fixed {f_name}")

fix_sidebar_nav()
