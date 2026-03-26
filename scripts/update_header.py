import os
import re

directory = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'

new_header_html = """
  <header class="site-header">
    <div style="display:flex;align-items:center;gap:16px">
      <span style="font-weight:700;font-size:20px;color:#1f2937;cursor:pointer" onclick="location.href='index.html'">CellbigCMS</span>
      <input class="input" placeholder="🔍 Search..." style="flex:1;max-width:300px">
    </div>
    <div style="display:flex;gap:16px;align-items:center">
      <span style="cursor:pointer">🔔 (3)</span>
      <span style="cursor:pointer">👤 Admin</span>
    </div>
  </header>
"""

# Pattern to capture the entire site-header block
# It assumes <header class="site-header"> ... </header>
# We use [\s\S]*? for non-greedy multiline matching
header_pattern = re.compile(r'<header class="site-header">[\s\S]*?</header>', re.IGNORECASE)

def update_headers():
    print("Forcing header update on all files...")
    count = 0
    file_list = [f for f in os.listdir(directory) if f.endswith('.html')]

    for filename in file_list:
        filepath = os.path.join(directory, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if header_pattern.search(content):
                # Replace existing header
                new_content = header_pattern.sub(new_header_html.strip(), content)
                
                # Check if change actually happened (ignore whitespace differences if possible? No, exact match is fine)
                # But new_header_html has newlines, so strip() is important.
                if new_content != content:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    print(f"  Updated header in {filename}")
                    count += 1
                else:
                    # check if the content is functionally the same (e.g. key string exists)
                    if 'onclick="location.href=\'index.html\'"' in content:
                         print(f"  Header already up-to-date in {filename}")
                    else:
                         # Should have been updated if not same
                         print(f"  No change despite match? {filename}")

            else:
                # Header missing! Insert before <div class="dashboard-layout">
                print(f"  Inserting missing header in {filename}...")
                if '<div class="dashboard-layout">' in content:
                    new_content = content.replace('<div class="dashboard-layout">', new_header_html + '\n  <div class="dashboard-layout">', 1)
                elif '<body>' in content:
                     new_content = content.replace('<body>', '<body>\n' + new_header_html, 1)
                else:
                    print(f"    Cannot find insertion point for {filename}")
                    continue

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                count += 1

        except Exception as e:
            print(f"  Error processing {filename}: {e}")

    print(f"Finished. Updated {count} files.")

if __name__ == "__main__":
    update_headers()
