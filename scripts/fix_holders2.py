import io, re
for fp in ['CMS-webpage/wireframe_site/product-editor.html', 'CMS-webpage/wireframe_site/package-editor.html']:
    html = io.open(fp, 'r', encoding='utf-8').read()
    html = re.sub(r'<div[^>]*>\s*<span>Created: [^<]*</span>\s*</div>', '', html)
    html = re.sub(r'<div class="info-label"[^>]*>\s*Created:\s*</div>\s*<div class="info-value"[^>]*>.*?</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div class="info-label"[^>]*>\s*Updated:\s*</div>\s*<div class="info-value"[^>]*>.*?</div>', '', html, flags=re.DOTALL)
    io.open(fp, 'w', encoding='utf-8').write(html)
