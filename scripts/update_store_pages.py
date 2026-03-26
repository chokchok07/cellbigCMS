import codecs
import re

# 1. Process store-list.html
with codecs.open('CMS-webpage/wireframe_site/store-list.html', 'r', 'utf-8') as f:
    list_html = f.read()

# Make register button point to store-editor.html
list_html = re.sub(
    r"window\.location\.href = 'store-detail\.html\?id=new';",
    r"window.location.href = 'store-editor.html';",
    list_html
)
list_html = list_html.replace(
    "window.location.href = 'store-detail.html'",
    "window.location.href = 'store-editor.html'"
)
# Revert for View/Edit buttons, but keep it for register
# Wait, actually in store-list.html:
# if (action === 'View') { window.location.href = 'store-detail.html'; }
# So replacing just blindly is bad. I'll just write a specific replacement for Register Button.

