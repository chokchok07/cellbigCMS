import glob
import re

for file in glob.glob("CMS-webpage/wireframe_site/*-editor.html"):
    with open(file, 'r', encoding='utf-8') as f:
        html = f.read()

    # The previous regex failed because of the exact string match, we can just replace 'disabled' inputs where value contains '서버'
    html = re.sub(
        r'value="[^"]*"(\s*)disabled',
        lambda m: 'placeholder="(서버에서 자동 생성)" value="" disabled' if '?' in m.group(0) or '서버' in m.group(0) else m.group(0),
        html
    )

    with open(file, 'w', encoding='utf-8') as f:
        f.write(html)

print("fixed encoded text")
