import re

with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern to find the content-cell block and replace it with just the title
# <div class="content-cell">\s*<div class="thumbnail">.*?</div>\s*<div class="content-info">\s*<div class="content-title">(.*?)</div>\s*<div class="content-category">.*?</div>\s*</div>\s*</div>

pattern = re.compile(
    r'<div class="content-cell">\s*<div class="thumbnail">.*?</div>\s*<div class="content-info">\s*<div class="content-title">(.*?)</div>\s*<div class="content-category">.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

def replacer(match):
    title = match.group(1)
    return f'<span style="font-weight: 500; color: #1f2937;">{title}</span>'

# Actually, the user says "콘텐츠명만 노출되게 만들어줘"
# Let's replace:
new_text = pattern.sub(replacer, text)

with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Title simplified!")
