import os
import re

directory = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'

def normalize_layout():
    print("Normalizing layout...")
    count = 0
    file_list = [f for f in os.listdir(directory) if f.endswith('.html')]

    for filename in file_list:
        filepath = os.path.join(directory, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for the pattern: <div class="editor-header"> ... </div> <div class="container">
            # We want to identify the editor header content and move it inside container.
            
            # Pattern 1: Editor Header outside container
            if '<div class="editor-header">' in content and '<div class="container">' in content:
                print(f"  Fixing layout in {filename}...")
                
                # Extract content of editor-header
                # This is tricky with regex if nested divs exist.
                # But looking at content-editor.html, it seems straightforward.
                # However, simpler approach:
                # 1. Regex replace <div class="editor-header">(.*?)</div>\s*<div class="container">
                # with <div class="container">\n<div class="page-header... (but preserving inner content might be hard if classes differ)
                
                # Let's try to just find the block and move it.
                # Assuming the structure is consistent:
                # <main class="main-content">
                #   <div class="editor-header">
                #      ...
                #   </div>
                #   <div class="container">
                
                pattern = re.compile(
                    r'<div class="editor-header">\s*(.*?)\s*</div>\s*<div class="container">',
                    re.DOTALL
                )
                
                match = pattern.search(content)
                if match:
                    header_content = match.group(1)
                    
                    # If header content already has "page-header", good.
                    # We want to inject it at the start of container.
                    # But wait, editor-header styling included background and border.
                    # If we move it inside container, it loses full width background.
                    # But "Product Library" style means inside container, aligned with content.
                    
                    # Also, clean up the header content if it has extra wrappers.
                    # content-editor.html has <div class="page-header"> inside editor-header.
                    # So we just take that.
                    
                    # new_structure:
                    # <div class="container">
                    #   <div class="page-header">...</div> (from editor-header)
                    #   ... (existing container content)
                    
                    # Replace the whole match with: <div class="container">\n{header_content}
                    # But we need to make sure header_content is semantic.
                    
                    # Remove the old editor-header wrapper entirely.
                    replacement = f'<div class="container">\n{header_content}'
                    
                    new_content = pattern.sub(replacement, content)
                    
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    count += 1
                else:
                    print(f"    Pattern not matched in {filename} (maybe nested differently?)")

        except Exception as e:
            print(f"  Error processing {filename}: {e}")

    print(f"Finished. Updated {count} files.")

if __name__ == "__main__":
    normalize_layout()
