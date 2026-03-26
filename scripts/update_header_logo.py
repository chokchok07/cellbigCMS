import os
import re

directory = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'

# Regex to find the header
# We look for the site-header and the specific inner div structure
# The original structure has a select element.
header_pattern = re.compile(
    r'<header class="site-header">\s*<div style="display:flex;align-items:center;gap:16px">\s*<select class="input" style="width:150px"><option>Product ▼</option></select>\s*<input class="input" placeholder="🔍 Search..." style="flex:1;max-width:300px">\s*</div>\s*<div style="display:flex;gap:16px;align-items:center">\s*<span style="cursor:pointer">🔔 \(3\)</span>\s*<span style="cursor:pointer">👤 Admin</span>\s*</div>\s*</header>',
    re.DOTALL
)

# New Header
new_header = """<header class="site-header">
    <div style="display:flex;align-items:center;gap:16px;">
      <h2 style="margin:0;cursor:pointer;font-size:20px;font-weight:bold;color:#1f2937;margin-right:20px;" onclick="location.href='index.html'">CellbigCMS</h2>
      <input class="input" placeholder="🔍 Search..." style="flex:1;max-width:300px">
    </div>
    <div style="display:flex;gap:16px;align-items:center">
      <span style="cursor:pointer">🔔 (3)</span>
      <span style="cursor:pointer">👤 Admin</span>
    </div>
  </header>"""

def update_headers():
    count = 0
    file_list = [f for f in os.listdir(directory) if f.endswith('.html')]

    for filename in file_list:
        filepath = os.path.join(directory, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if header_pattern.search(content):
                new_content = header_pattern.sub(new_header, content)
                
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"Updated header in {filename}")
                    count += 1
                else:
                    print(f"No changes needed for {filename}")
            else:
                print(f"Header pattern not found in {filename}")

        except Exception as e:
            print(f"Error processing {filename}: {e}")

    print(f"Finished. Updated {count} files.")

if __name__ == "__main__":
    update_headers()
