import re

def process_files():
    # 1. Read content-editor.html
    with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
        editor_html = f.read()

    # 2. Extract versionsSection block
    versions_sec_pattern = re.compile(r'<!--\s*Versions Section\s*\(Moved from right column\)\s*-->\s*<div\s+class="card"\s+id="versionsSection".*?</div>\s*</div>\s*</div>', re.DOTALL)
    
    # Wait, the structure in editor is:
    # <div class="card" id="versionsSection" style="display:none;"> ... (till after v1.1.0 block) ... </div>
    # Let's find it securely.
    start_str = '<div class="card" id="versionsSection"'
    start_idx = editor_html.find(start_str)
    if start_idx != -1:
        # Find matching closing div for the card
        div_count = 0
        end_idx = start_idx
        for i in range(start_idx, len(editor_html)):
            if editor_html[i:i+4] == '<div':  # very naive parsing
                div_count += 1
            elif editor_html[i:i+5] == '</div':
                div_count -= 1
                if div_count == 0:
                    end_idx = i + 6
                    break
        extracted_versions_html = editor_html[start_idx:end_idx]
    else:
        extracted_versions_html = ""

    # 3. Extract the New Version modal HTML
    modal_start_str = '<!-- New Version Modal -->'
    modal_start_idx = editor_html.find(modal_start_str)
    if modal_start_idx != -1:
        # It ends around the end of the form or before footer
        # let's look for '</form>\n  </div>\n</div>' or something similar
        end_str = '</form>\n    </div>\n  </div>'
        modal_end_idx = editor_html.find('  </div>\n</div>', modal_start_idx) + 15
        extracted_modal_html = editor_html[modal_start_idx:modal_end_idx]
    else:
        # Try a more forgiving search
        m = re.search(r'<!--\s*New Version Modal\s*-->.*?(</div>\s*</div>\s*</div>)', editor_html, re.DOTALL)
        if m:
            extracted_modal_html = m.group(0)
        else:
            extracted_modal_html = ""

    # 4. Extract Modal JS
    js_start_str = '// New Version Modal Logic'
    js_start_idx = editor_html.find(js_start_str)
    if js_start_idx != -1:
        js_end_str = '<!--' # ends before modal html? no, wait. It's inside <script>
        # Let's just use regex for the js block until a function ends
        m_js = re.search(r'// New Version Modal Logic.*?function submitNewVersion\(\).*?}', editor_html, re.DOTALL)
        extracted_modal_js = m_js.group(0) if m_js else ""
    else:
        extracted_modal_js = ""
    
    print(f"Extracted versions HTML length: {len(extracted_versions_html)}")
    print(f"Extracted modal HTML length: {len(extracted_modal_html)}")
    print(f"Extracted JS length: {len(extracted_modal_js)}")

process_files()
