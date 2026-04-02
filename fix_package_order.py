import re

files = [
    'CMS-webpage/wireframe_site/package-detail.html',
    'CMS-webpage/wireframe_site/package-editor.html'
]

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()

    # We want to change the order to: Package Name, Package ID, Product, Status
    if 'package-detail' in fname:
        # It's inside <div style="display: grid; grid-template-columns: 140px 1fr; gap: 16px 24px; align-items: start;">
        # ...
        # </div>
        
        # Let's extract the pieces we need
        def extract_field(label_name):
            # Try to grab the block: <div class="info-label"...>label_name:</div>\n<element ...>...</element>
            pattern = r'<div class="info-label"[^>]*>' + label_name + r':?</div>\s*(?:<div[^>]*>.*?</div>|<input[^>]*>|<select[^>]*>.*?</select>|<textarea[^>]*>.*?</textarea>)'
            m = re.search(pattern, content, re.DOTALL)
            return m.group(0) if m else None

        prod_part = extract_field('Product')
        pkg_id_part = extract_field('Package ID')
        pkg_name_part = extract_field('Package Name')
        desc_part = extract_field('Description')
        status_part = extract_field('Status')

        old_order = f"{prod_part}\n                \n                {pkg_id_part}\n                \n                {pkg_name_part}\n                \n                {desc_part}\n                \n                {status_part}"
        
        if prod_part and status_part:
            new_order = f"{pkg_name_part}\n                \n                {pkg_id_part}\n                \n                {prod_part}\n                \n                {status_part}\n                \n                {desc_part}"
            
            # the original has some indents and spaces, we do a slightly broader replacement
            grid_pattern = r'(<h2[^>]*>📋 기본 정보</h2>\s*<div style="display: grid; grid-template-columns: 140px 1fr; gap: 16px 24px; align-items: start;">)(.*?)(</div>\s*</div>\s*<div class="card" id="metadataSection">)'
            m = re.search(grid_pattern, content, re.DOTALL)
            if m:
                # build the new inner content
                new_inner = f"\n                {pkg_name_part}\n                \n                {pkg_id_part}\n                \n                {prod_part}\n                \n                {status_part}\n                \n                {desc_part}\n              "
                content = content[:m.start(2)] + new_inner + content[m.end(2):]
                
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {fname}")
            else:
                print(f"Could not find grid pattern in {fname}")

    elif 'package-editor' in fname:
        # In package-editor, the structure is <div class="form-group"> ... </div>
        # Currently it has Package ID, Name, Version, Description
        def extract_form_group(label_name):
            pattern = r'<div class="form-group">\s*<label class="form-label[^"]*">' + label_name + r'</label>\s*(?:<input[^>]*>|<textarea[^>]*>.*?</textarea>)\s*</div>'
            m = re.search(pattern, content, re.DOTALL)
            return m.group(0) if m else None

        pkg_id_part = extract_form_group('Package ID')
        name_part = extract_form_group('Name')
        version_part = extract_form_group('Version')
        desc_part = extract_form_group('Description')

        if pkg_id_part and name_part:
            # User wants: Package Name, Package ID(자동), Product, Status
            # We need to create Product and Status if they don't exist
            prod_html = '''<div class="form-group">
              <label class="form-label required">Product</label>
              <select class="input" style="width:100%;">
                <option value="product-sandcraft" selected>SandCraft</option>
                <option value="product-fish">FishWorld</option>
              </select>
            </div>'''
            
            status_html = '''<div class="form-group">
              <label class="form-label required">Status</label>
              <select class="input" style="width:100%;">
                <option value="published" selected>Published</option>
                <option value="test">Test</option>
                <option value="unpublished">Unpublished</option>
              </select>
            </div>'''
            
            new_inner = f"\n            {name_part}\n            {pkg_id_part}\n            {prod_html}\n            {status_html}\n            {version_part}\n            {desc_part}\n          "
            
            # replace inside <div style="display: flex; flex-direction: column; gap: 16px;">
            flex_pattern = r'(<h2[^>]*>📋 기본 정보</h2>\s*<div style="display: flex; flex-direction: column; gap: 16px;">)(.*?)(</div>\s*</div>\s*</div>\s*</main>)'
            m = re.search(flex_pattern, content, re.DOTALL)
            if m:
                content = content[:m.start(2)] + new_inner + content[m.end(2):]
                with open(fname, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Updated {fname}")
            else:
                print(f"Could not find flex pattern in {fname}")
