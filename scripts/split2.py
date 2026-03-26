import io
import re

for fp, targets in [
    ('CMS-webpage/wireframe_site/product-editor.html', ['패키지 설정', '연결된 패키지', '시스템 메타데이터']),
    ('CMS-webpage/wireframe_site/package-editor.html', ['포함된 콘텐츠 구성', '시스템 메타데이터'])
]:
    with io.open(fp, 'r', encoding='utf-8') as f:
        html = f.read()

    for t in targets:
        match = re.search(r'<h2[^>]*>.*?'+t+'.*?</h2>', html, flags=re.DOTALL)
        if match:
            h2_idx = match.start()
            div_start = html.rfind('<div', 0, h2_idx)
            while div_start != -1 and 'box-shadow' not in html[div_start:div_start+150] and 'card' not in html[div_start:div_start+150]:
                div_start = html.rfind('<div', 0, div_start)

            if div_start != -1:
                stack = 0
                div_end = -1
                idx = div_start
                while idx < len(html):
                    if html.startswith('<div', idx): stack += 1; idx += 4
                    elif html.startswith('</div', idx):
                        stack -= 1; idx += 5
                        if stack == 0:
                            div_end = html.find('>', idx) + 1
                            break
                    else: idx += 1

                if div_end != -1:
                    html = html[:div_start] + html[div_end:]

    with io.open(fp, 'w', encoding='utf-8') as f:
        f.write(html)
print('Done!')