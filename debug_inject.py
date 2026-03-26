import os

with open('CMS-webpage/wireframe_site/version-register.html', 'r', encoding='utf-8') as f:
    orig = f.read()

html_start = orig.find('<div class="modal-overlay">')
html_end = orig.find('<script>', html_start)
modal_html = orig[html_start:html_end] if html_start > -1 else ''

with open('debug_out.txt', 'w', encoding='utf-8') as f:
    f.write(f"html_start: {html_start}\n")
    f.write(f"html_end: {html_end}\n")
    f.write(f"modal_html_len: {len(modal_html)}\n")
