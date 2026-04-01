import re

def process():
    with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
        editor_text = f.read()
        
    # Find versionsSection
    # <div class="card" id="versionsSection"...> ... matching close div
    start_str = '<div class="card" id="versionsSection"'
    start_idx = editor_text.find(start_str)
    div_count = 0
    end_idx = start_idx
    for i in range(start_idx, len(editor_text)):
        if editor_text[i:i+4] == '<div': div_count += 1
        elif editor_text[i:i+5] == '</div':
            div_count -= 1
            if div_count == 0:
                end_idx = i + 6
                break
    versions_sec_html = editor_text[start_idx:end_idx]
    # To remove it properly, let's also remove the preceding comments:
    before_idx = editor_text.rfind('<!-- Versions Section', 0, start_idx)
    if before_idx != -1:
        editor_text_new = editor_text[:before_idx] + editor_text[end_idx:]
    else:
        editor_text_new = editor_text[:start_idx] + editor_text[end_idx:]
        
    # Modal
    modal_start = '<!-- New Version Modal -->'
    ms = editor_text_new.find(modal_start)
    if ms != -1:
        # find matching close div for <div id="newVersionModal"
        # It's an overlay modal, so let's use regex
        m = re.search(r'<!-- New Version Modal -->.*?<div id="newVersionModal".*?</form>\s*</div>\s*</div>', editor_text_new, re.DOTALL)
        if m:
            modal_html = m.group(0)
            editor_text_new = editor_text_new.replace(modal_html, '')
        else:
            m = re.search(r'<div id="newVersionModal".*?</form>\s*</div>\s*</div>', editor_text_new, re.DOTALL)
            modal_html = m.group(0) if m else ""
            editor_text_new = editor_text_new.replace(modal_html, '')
    else:
        modal_html = ""
        
    # JS
    m_js = re.search(r'// New Version Modal Logic\s+function openNewVersionModal\(\).*?// In a real scenario.*?\s+}', editor_text_new, re.DOTALL)
    if m_js:
        modal_js = m_js.group(0)
        editor_text_new = editor_text_new.replace(modal_js, '')
    else:
        modal_js = ""
        
    # Also clean up "document.getElementById('versionsSection').style.display = 'block';"
    editor_text_new = re.sub(r"document\.getElementById\('versionsSection'\)\.style\.display = 'block';", "", editor_text_new)

    # Clean up empty spaces nicely
    with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
        f.write(editor_text_new)
        
    print("Cleaned editor text, length=", len(editor_text_new))
    print("Modal length", len(modal_html))
    print("Versions Section length", len(versions_sec_html))

    # Now let's put it into content-versions.html
    # In content-versions.html, user has 
    # <!-- Versions List Area --> ... </div>
    # Let's replace the whole container with our versions_sec_html (minus the display:none part)
    with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
        vers_text = f.read()

    # Find <!-- Versions List Area --> inside vers_text
    va_start = vers_text.find('<!-- Versions List Area -->')
    if va_start != -1:
        # Find next <script> to know where footer/script boundary is
        scr_idx = vers_text.find('<script>', va_start)
        
        # We also need to get the header part. 
        # The user has `<div class="page-header" style="flex-direction: column; align-items: flex-start;">`
        # But versions_sec_html *is* the list.
        # Let's just modify versions_sec_html to remove `style="display:none;"`
        versions_sec_html_visible = versions_sec_html.replace('style="display:none;"', '')
        
        # In content-versions.html, let's inject modal right before </body>
        body_end = vers_text.rfind('</body>')
        
        # And inject JS right before </script>
        script_end = vers_text.rfind('</script>')
        if script_end == -1:
            # Need to create script tag
            vers_text = vers_text[:body_end] + f"\n<script>\n{modal_js}\n</script>\n" + vers_text[body_end:]
        else:
            vers_text = vers_text[:script_end] + f"\n{modal_js}\n" + vers_text[script_end:]
            
        # Re-fetch body_end because it changed
        body_end = vers_text.rfind('</body>')
        vers_text = vers_text[:body_end] + f"\n{modal_html}\n" + vers_text[body_end:]
        
        # Now replace the Versions List Area in content-versions.html
        # But wait, content-versions.html has a nicely styled 
        # <h1 class="page-title">📂 Version History</h1> etc. We should probably keep that.
        # I'll just save it separately and then we can review.
        
        # Let's write the outputs directly so the agent can see them.
        with open('extracted_versions.html', 'w', encoding='utf-8') as f:
            f.write(versions_sec_html)
        with open('extracted_modal.html', 'w', encoding='utf-8') as f:
            f.write(modal_html)
        with open('extracted_modal.js', 'w', encoding='utf-8') as f:
            f.write(modal_js)

process()
