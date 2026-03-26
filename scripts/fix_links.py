import io
import re

def fix_links():
    # 1. Product List
    fp = 'CMS-webpage/wireframe_site/product-list.html'
    html = io.open(fp, 'r', encoding='utf-8').read()
    # Find the "+ New Product" button JS block usually
    html = re.sub(r'location\.href\s*=\s*([\'"])product-detail\.html\1', r'location.href=\1product-editor.html\1', html)
    io.open(fp, 'w', encoding='utf-8').write(html)
    
    # 2. Package List
    fp = 'CMS-webpage/wireframe_site/package-list.html'
    html = io.open(fp, 'r', encoding='utf-8').read()
    html = re.sub(r'location\.href=([\'"])package-detail\.html\1', r'location.href=\1package-editor.html\1', html)
    io.open(fp, 'w', encoding='utf-8').write(html)

def fix_localarea():
    fp = 'CMS-webpage/wireframe_site/localarea-editor.html'
    html = io.open(fp, 'r', encoding='utf-8').read()
    
    # Let's fix that extra </div> before Description!
    # Currently it looks like:
    #              </div>
    #            </div>
    #            </div>
    #            <div class="form-group">
    #              <label class="form-label">Description</label>

    html = html.replace('</div>\n\n            </div>\n            <div class="form-group">\n              <label class="form-label">Description</label>',
                        '</div>\n\n            <div class="form-group">\n              <label class="form-label">Description</label>')
    # Fallback if whitespace differs
    html = re.sub(
        r'</div>\s*</div>\s*<div class="form-group">\s*<label class="form-label">Description</label>',
        r'</div>\n            <div class="form-group">\n              <label class="form-label">Description</label>',
        html
    )

    io.open(fp, 'w', encoding='utf-8').write(html)

fix_links()
fix_localarea()
print('Fixed links and localarea layout.')
