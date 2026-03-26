import os
import re

TARGET_DIR = r"c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site"

def fix_layout(content):
    # Fix 1: Replace max-width:800px with container class
    modified = re.sub(
        r'<main class="main-content">\s*<div style="max-width:800px">',
        r'<main class="main-content">\n      <div class="container">',
        content
    )

    # Fix 2: Remove nested page-headers caused by bad automated edit
    # We look for the specific pattern seen in the files
    pattern = r'(<div class="page-header">\s*<div>\s*)\s*<div class="page-header">\s*<div>\s*<h1 class="page-title">([^<]+)</h1>\s*<p class="page-desc">([^<]+)</p>\s*</div>\s*<div class="header-actions">\s*<!-- Actions -->\s*</div>\s*</div>'
    
    def replacer(match):
        prefix = match.group(1) # <div class="page-header"><div>
        title = match.group(2)
        desc = match.group(3)
        # We reconstruct a clean header
        # The prefix already has one '<div>', so we just need to fill it
        return f'<div class="page-header">\n          <div>\n            <h1 class="page-title">{title}</h1>\n            <p class="page-desc">{desc}</p>\n          </div>\n          <div class="header-actions">\n            <!-- Actions -->\n          </div>\n        </div>'

    # The pattern in the files is slightly messy. Let's try to match the messy block specifically.
    # The messy block looks like:
    # <div class="page-header">
    #   <div>
    #     
    # <div class="page-header">
    #   <div>
    #     <h1 class="page-title">...</h1>
    #     <p class="page-desc">...</p>
    #   </div>
    #   <div class="header-actions">
    #     <!-- Actions -->
    #   </div>
    # </div>
    
    # We can try to match the outer div opening up to the inner div closing.
    
    messy_pattern = re.compile(
        r'(<!-- Page Header -->\s*<div class="page-header">\s*<div>\s*)'
        r'(<div class="page-header">.*?</div>\s*</div>)', # Inner block
        re.DOTALL
    )
    
    if messy_pattern.search(modified):
        print("Found messy header pattern, fixing...")
        # If we found the specific mess, replace it with just the inner block (which seems correct strictly speaking, though indentation might be off)
        # Actually, the outer block has `<div>` which is open.
        # Let's interactively fix. 
        # The inner block is the one we want to keep (it has the title etc). 
        # The outer block is wrapping it partially?
        
        # Let's simplify.
        # If we see:
        # <div class="page-header">
        #   <div>
        #     <div class="page-header">
        
        # We can replace `<div class="page-header">\s*<div>\s*<div class="page-header">` with `<div class="page-header">`
        # and then we probably have an extra `</div>` somewhere?
        
        # Let's try a strict text replacement for the specific breakage signature.
        
        broken_sig = (
            '<div class="page-header">\n          <div>\n            \n        <div class="page-header">'
        )
        
        if broken_sig in modified:
             modified = modified.replace(broken_sig, '<div class="page-header">')
             # Now we likely have an extra </div> or </div></div> mismatch later?
             # The original code was:
             # <div class="page-header">
             #   <div>
             #     ... content ...
             #   </div>
             # </div>
             
             # The bad code is:
             # <div class="page-header">
             #   <div>
             #     <div class="page-header"> 
             #        ... content ... 
             #     </div>
             #     ...
             #   </div>
             
             # If we replaced the top, we have:
             # <div class="page-header">
             #        ... content ... 
             #     </div>
             #     ...
             #   </div>
             
             # This means we have an extra closing div at the end of the block?
             # Let's look at the file content again.
             pass

    # Alternative strategy: 
    # Just replace the whole messy block if we can identify it clearly.
    # The messy block seems to be:
    # <div class="page-header">
    #   <div>
    #     
    # <div class="page-header">
    #   <div>
    #     <h1 class="page-title">TITLE</h1>
    #     <p class="page-desc">DESC</p>
    #   </div>
    #   <div class="header-actions">
    #     <!-- Actions -->
    #   </div>
    # </div>
    
    # We can use regex to capture title and desc and rebuild a clean block.
    
    clean_re = re.compile(
        r'<div class="page-header">\s*<div>\s*<div class="page-header">\s*<div>\s*<h1 class="page-title">([^<]+)</h1>\s*<p class="page-desc">([^<]+)</p>\s*</div>\s*<div class="header-actions">\s*<!-- Actions -->\s*</div>\s*</div>',
        re.DOTALL
    )
    
    def clean_replacer(m):
        t = m.group(1)
        d = m.group(2)
        return f'''<div class="page-header">
          <div>
            <h1 class="page-title">{t}</h1>
            <p class="page-desc">{d}</p>
          </div>
          <div class="header-actions">
            <!-- Actions -->
          </div>
        </div>'''
        
    modified = clean_re.sub(clean_replacer, modified)

    return modified

def process_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    new_content = fix_layout(content)
    
    if content != new_content:
        print(f"Updating {filepath}")
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
    else:
        print(f"No changes for {filepath}")

def main():
    files = [f for f in os.listdir(TARGET_DIR) if f.endswith(".html")]
    for filename in files:
        if "editor" in filename or "detail" in filename: # Focus on likely candidates, or just do all?
             process_file(os.path.join(TARGET_DIR, filename))
        else:
             # Check if we should process others too
             process_file(os.path.join(TARGET_DIR, filename))

if __name__ == "__main__":
    main()
