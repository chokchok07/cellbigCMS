import io, re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'class="[^"]*modal[^"]*"', text)
with open('debug_classes.txt', 'w', encoding='utf-8') as out:
    for m in matches:
        out.write(m + '\n')
