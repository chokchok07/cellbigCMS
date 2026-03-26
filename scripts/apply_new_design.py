import os
import re

TARGET_DIR = r"c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site"
STYLES_CSS = "styles.css"
REPORT_FILE = "report-content-usage.html"

def process_file(filepath, filename):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # 1. Remove inline styles block if it contains metric-card
    style_pattern = re.compile(r'<style>.*?\.metric-card.*?</style>', re.DOTALL)
    content = style_pattern.sub('', content)

    # 2. Update Header
    
    # Check if file already has the NEW structure (page-title + page-desc)
    # Be careful, we might want to update package-list.html even if it has "page-header" but lacks "page-title" class.
    if 'class="page-title"' in content and '<div class="page-header">' in content:
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
        return

    # Find the insertion point: usually inside <main class="main-content"> or <div class="container">
    main_match = re.search(r'<main[^>]*>', content)
    if not main_match:
         main_match = re.search(r'<div class="container">', content)
    
    start_pos = main_match.end() if main_match else 0
    
    # Search for H1 after main content starts
    h1_pattern = re.compile(r'<h1[^>]*>(?P<title>.*?)</h1>', re.DOTALL)
    h1_match = h1_pattern.search(content, pos=start_pos)
    
    header_updated = False

    if h1_match:
        # Check if H1 is inside a known header structure we want to replace
        
        # Type C: package-list.html style (div.page-header > div > h1 + p)
        # We look for <div class="page-header"> before H1
        pre_h1 = content[max(0, h1_match.start()-200):h1_match.start()]
        if 'class="page-header"' in pre_h1:
            # It's likely the package-list case. We want to replace the whole div.
            # Regex to capture the whole div is tricky, but let's try matching the specific structure around H1
            # <div class="page-header"> ... </div>
            # We'll use a regex that matches from <div class="page-header"> to the </div> that follows the button/action
            
            # Since we can't do balanced matching, let's assume the header ends after the button/action line or just look for the closing div.
            # But the closing div might be far away if we are wrong.
            
            # Let's try to match the specific content we know is in package-list.html
            pkg_header_regex = re.compile(
                r'<div class="page-header">\s*<div>\s*<h1>(?P<title>.*?)</h1>\s*<p class="subtitle">.*?</p>\s*</div>\s*(?P<actions>.*?)\s*</div>',
                re.DOTALL
            )
            match = pkg_header_regex.search(content)
            if match:
                title = match.group('title').strip()
                actions = match.group('actions').strip()
                new_header = f'''
        <div class="page-header">
          <div>
            <h1 class="page-title">{title}</h1>
            <p class="page-desc">Manage {title} and view details.</p>
          </div>
          <div class="header-actions">
            {actions}
          </div>
        </div>'''
                content = content.replace(match.group(0), new_header)
                header_updated = True
        
        if not header_updated:
            # Type A: <div style="display:flex...justify-content:space-between..."> ... <h1>...</h1> ... </div>
            # Find the div that wraps the H1 if it has that style
            
            # Search for the div before H1
            div_match = re.search(r'<div\s+style="display:flex;justify-content:space-between[^"]*"\s*>', pre_h1)
            if div_match:
                # This logic is complex to implement with regex searching backwards.
                # Let's just search the whole file for the Type A pattern and see if our H1 is inside it.
                pass 
            
            # Alternative: Search for Type A pattern generally
            flex_header_regex = re.compile(
                r'<div\s+style="display:flex;justify-content:space-between[^"]*"\s*>\s*'
                r'(?P<inner>.*?)'
                r'</div>', 
                re.DOTALL
            )
            
            for match in flex_header_regex.finditer(content):
                if match.start() >= start_pos and match.start() <= h1_match.start():
                    # This div likely wraps the H1
                    inner = match.group('inner')
                    if '<h1>' in inner or '<h1 ' in inner:
                        # Extract title from inner
                        t_match = re.search(r'<h1[^>]*>(.*?)</h1>', inner)
                        if t_match:
                            title = t_match.group(1).strip()
                            # Actions are everything else. Remove H1.
                            actions = inner.replace(t_match.group(0), '').strip()
                            
                            new_header = f'''
        <div class="page-header">
          <div>
            <h1 class="page-title">{title}</h1>
            <p class="page-desc">Manage {title} and view details.</p>
          </div>
          <div class="header-actions">
            {actions}
          </div>
        </div>'''
                            content = content.replace(match.group(0), new_header)
                            header_updated = True
                            break
        
        if not header_updated:
            # Type B: Bare H1
            # Replace just the H1
            # Check if H1 is inside a panel/card (heuristic: check indentation or parent div class)
            # We'll validly assume the FIRST H1 in main content is the page title.
            
            # Just verify it's the same H1 found earlier
            title = h1_match.group('title').strip()
            
            # Simple replacement
            new_header = f'''
        <div class="page-header">
          <div>
            <h1 class="page-title">{title}</h1>
            <p class="page-desc">Manage {title} and view details.</p>
          </div>
          <div class="header-actions">
            <!-- Actions -->
          </div>
        </div>'''
            
            content = content[:h1_match.start()] + new_header + content[h1_match.end():]
            header_updated = True

    if not header_updated:
        # No header found or updated?
        # Maybe Dashboard case (no H1)
        if 'dashboard' in filename.lower() and '<div class="page-header">' not in content:
             # Insert after <div class="container">
             insert_regex = re.compile(r'<div class="container">')
             match = insert_regex.search(content)
             if match:
                 title = "Dashboard"
                 new_header = f'''
        <div class="page-header">
          <div>
            <h1 class="page-title">?? {title}</h1>
            <p class="page-desc">Overview of your system status.</p>
          </div>
          <div class="header-actions">
          </div>
        </div>
'''
                 content = content[:match.end()] + new_header + content[match.end():]

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filename}")

def main():
    if not os.path.exists(TARGET_DIR):
        print(f"Directory not found: {TARGET_DIR}")
        return

    for filename in os.listdir(TARGET_DIR):
        if filename.endswith(".html") and filename != REPORT_FILE:
            filepath = os.path.join(TARGET_DIR, filename)
            try:
                process_file(filepath, filename)
            except Exception as e:
                print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    main()
