import io
import re

def process_file(in_fp, out_fp, targets):
    with io.open(in_fp, 'r', encoding='utf-8') as f:
        html = f.read()

    # Find the top-level cards (ones starting with <!-- ... --> usually or just having card)
    # The structure has <div class="card" or <div style="...background: #fff... padding: 24px..."
    # We will split the HTML by these top level container dividers.
    
    # Actually, the simplest way is to find <h2> tags
    for t in targets:
        match = re.search(r'<h2[^>]*>(?:|.*?)'+t+r'.*?</h2>', html, flags=re.DOTALL)
        if not match: continue
        
        h2_idx = match.start()
        # Find exactly where THIS card started
        # Find all `<div` before h2_idx
        div_start = -1
        idx = h2_idx
        while idx > 0:
            idx = html.rfind('<div', 0, idx)
            if idx == -1: break
            # Does this div have card class or padding: 24px?
            tag_end = html.find('>', idx)
            tag = html[idx:tag_end+1]
            if 'class="card"' in tag or ('background: #fff' in tag and 'box-shadow' in tag):
                div_start = idx
                break
                
        if div_start != -1:
            # find matching end div
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
                        # also consume trailing whitespace
                        while div_end < len(html) and html[div_end].isspace():
                            div_end += 1
                        break
                else:
                    i += 1
            
            if div_end != -1:
                html = html[:div_start] + html[div_end:]

    with io.open(out_fp, 'w', encoding='utf-8') as f:
        f.write(html)

process_file('CMS-webpage/wireframe_site/product-detail.html', 'CMS-webpage/wireframe_site/product-editor.html', ['패키지 설정', '연결된 패키지', '시스템 메타데이터', '포함된 콘텐츠'])

process_file('CMS-webpage/wireframe_site/package-detail.html', 'CMS-webpage/wireframe_site/package-editor.html', ['포함된 콘텐츠 구성', '시스템 메타데이터', '연결된 패키지'])

print("Done building clean editors")
