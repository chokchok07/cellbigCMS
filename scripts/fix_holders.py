import io
import re

def fix_editor(fp, id_label):
    with io.open(fp, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the ID div and replace with input disabled
    # ID block looks like:
    # <div class="info-label" ...>Product ID:</div>
    # <div class="info-value" ...>product-sandcraft</div>
    
    # We replace ID with `placeholder="(서버에서 자동 생성)" disabled`
    html = re.sub(
        r'<div class="info-label"([^>]*)>\s*' + id_label + r':\s*</div>\s*<div class="info-value"[^>]*>.*?</div>',
        r'<div class="info-label"\1>' + id_label + r':</div>\n                <input type="text" class="input" style="width:100%; background:#f3f4f6; color:#9ca3af;" value="" placeholder="(서버에서 자동 생성)" disabled>',
        html,
        flags=re.DOTALL
    )

    # Empty out standard inputs and textareas
    html = re.sub(r'(<input type="text"[^>]*?)value="[^"]*"', r'\1value="" placeholder="내용을 입력하세요"', html)
    html = re.sub(r'(<textarea[^>]*>).*?(</textarea>)', r'\1\2', html)
    
    # Remove Created / Updated
    # <div class="info-label"...>Created:</div> <div ...>...</div>
    html = re.sub(r'<div class="info-label"[^>]*>\s*Created:\s*</div>\s*<div class="info-value"[^>]*>.*?</div>', '', html, flags=re.DOTALL)
    html = re.sub(r'<div class="info-label"[^>]*>\s*Updated:\s*</div>\s*<div class="info-value"[^>]*>.*?</div>', '', html, flags=re.DOTALL)

    # Default Package should probably be a `<select>` or empty?
    # Leave it as an empty text or select. For now let's just make it a select.
    if 'Product' in fp:
        html = re.sub(
            r'<div class="info-label"([^>]*)>\s*Default Package:\s*</div>\s*<div class="info-value"[^>]*>.*?</div>',
            r'<div class="info-label"\1>Default Package:</div>\n                <select class="input" style="width:100%;"><option value="">-- 선택하세요 --</option></select>',
            html,
            flags=re.DOTALL
        )
    if 'Package' in fp:
        html = re.sub(
            r'<div class="info-label"([^>]*)>\s*Version:\s*</div>\s*<div class="info-value"[^>]*>.*?</div>',
            r'<div class="info-label"\1>Version:</div>\n                <input type="text" class="input" style="width:100%" value="" placeholder="예: 1.0.0">',
            html,
            flags=re.DOTALL
        )

    with io.open(fp, 'w', encoding='utf-8') as f:
        f.write(html)

fix_editor('CMS-webpage/wireframe_site/product-editor.html', 'Product ID')
fix_editor('CMS-webpage/wireframe_site/package-editor.html', 'Package ID')

print('Editors placeholders cleaned!')
