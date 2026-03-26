import io, re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    target = f.read()

m = re.search(r'<style>(.*?)</style>', target, flags=re.DOTALL)
if m:
    with open('output_style.txt', 'w', encoding='utf-8') as out:
        out.write(m.group(0))
