import re

with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.findall(r'<script[^>]*>.*?</script>', text, re.DOTALL)
with open('debug_js_80.txt', 'w', encoding='utf-8') as f:
    f.write('\n\n---SCRIPT---\n\n'.join(m))
