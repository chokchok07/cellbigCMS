import codecs
import re

print("Clean JS from store-editor.html")
with codecs.open('CMS-webpage/wireframe_site/store-editor.html', 'r', 'utf-8') as f:
    editor_html = f.read()

# The JS in store-editor.html might have logic for urlParams 'isNew'
# Since it's purely a creation page now, we can remove the logic related to toggling things on/off.
editor_html = re.sub(
    r"const isNew = urlParams\.get\('id'\) === 'new';.*?(?=function\s+deleteStore)",
    r"",
    editor_html,
    flags=re.IGNORECASE | re.DOTALL
)

# Wait, let's just do a string replace or a safer regex
# Let me look at the JS in store-editor.html
