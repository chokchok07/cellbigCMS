import io
import re

def process_file(in_fp, out_fp, targets):
    with io.open(in_fp, 'r', encoding='utf-8') as f:
        html = f.read()

    for t in targets:
        # Limit to the h2 tag inner content
        pattern = r'<h2[^>]*>.*?' + t + r'.*?</h2>'
        match = re.search(pattern, html)
        if not match: 
            print('Could not find', t, 'in', in_fp)
            continue
        
        h2_idx = match.start()
        div_start = -1
        idx = h2_idx
        while idx > 0:
            idx = html.rfind('<div', 0, idx)
            if idx == -1: break
            tag_end = html.find('>', idx)
            tag = html[idx:tag_end+1]
            if 'class="card"' in tag or ('background: #fff' in tag and 'box-shadow' in tag):
                div_start = idx
                break
                
        if div_start != -1:
            stack = 0
            div_end = -1
            i = div_start
            while i < len(html):
                if html.startswith('<div', i):
                    stack += 1
                    i += 4
                elif html.startswith('</div', i):
                    stack -= 1
                    i += 5
                    if stack == 0:
                        div_end = html.find('>', i) + 1
                        while div_end < len(html) and html[div_end].isspace():
                            div_end += 1
                        break
                else:
                    i += 1
            
            if div_end != -1:
                html = html[:div_start] + html[div_end:]

    # Title replacements
    if 'product' in in_fp:
        html = re.sub(r'Product 단건 조회/수정', 'Product 신규 등록', html)
        html = re.sub(r'Product 단건 조회', 'Product 신규 등록', html)
    if 'package' in in_fp:
        html = re.sub(r'Package 단건 조회/수정', 'Package 신규 등록', html)
        html = re.sub(r'Package 단건 조회', 'Package 신규 등록', html)
        
    html = re.sub(r'>\s*List\s*</button>', '>List</button>\n          <button class="action-btn action-btn-success">Save</button>', html)

    with io.open(out_fp, 'w', encoding='utf-8') as f:
        f.write(html)

process_file('CMS-webpage/wireframe_site/product-detail.html', 'CMS-webpage/wireframe_site/product-editor.html', ['연결된 패키지', '포함된 콘텐츠'])

process_file('CMS-webpage/wireframe_site/package-detail.html', 'CMS-webpage/wireframe_site/package-editor.html', ['Connected Contents', 'Metadata'])

print('Done building clean editors!')
