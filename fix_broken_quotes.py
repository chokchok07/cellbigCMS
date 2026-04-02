import re

with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix the broken backslash escape in the onclick
text = text.replace(r"if(confirm(\'콘텐츠를 추가하시겠습니까?\'))", r"if(confirm('콘텐츠를 추가하시겠습니까?'))")
text = text.replace(r"if(confirm(\"콘텐츠를 추가하시겠습니까?\"))", r"if(confirm('콘텐츠를 추가하시겠습니까?'))")

# Just to be absolutely certain, let's just rewrite the onclick attribute entirely for that button
text = re.sub(
    r'onclick="[^"]*confirm[^"]*submitManageContentsNew\([^"]*"',
    r'onclick="if(confirm(\'콘텐츠를 추가하시겠습니까?\')) { submitManageContentsNew(); }"',
    text
)

with open('CMS-webpage/wireframe_site/package-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed Broken Quotes.")
