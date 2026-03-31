import re

with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace openContentViewModal(this) with window.location.href='content-detail.html'
text = text.replace('openContentViewModal(this)', "window.location.href='content-detail.html'")

# Remove the content view modal
# It usually starts with <!-- Content View Modal --> and ends with some closing divs. I'll use regex.
text = re.sub(r'<!--\s*Content View Modal\s*-->.*?</div>\s*</div>\s*</div>\s*</div>', '', text, flags=re.DOTALL)

with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('Updated content-list.html')
