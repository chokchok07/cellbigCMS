import io

fp = "CMS-webpage/wireframe_site/device-editor.html"
with io.open(fp, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix MAC Address placeholder
html = html.replace(
    'class="input" style="width:100%; font-family:monospace" value=""',
    'class="input" style="width:100%; font-family:monospace" value="" placeholder="예: 00:1A:2B:3C:4D:5E"'
)

# Fix Name placeholder and value
html = html.replace(
    'class="input" style="width:100%" value="Device-A"',
    'class="input" style="width:100%" value="" placeholder="예: 강남 직영점 1번 모니터"'
)

with io.open(fp, 'w', encoding='utf-8') as f:
    f.write(html)

print("device-editor placeholders fixed")
