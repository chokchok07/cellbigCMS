import re

with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Resize the Modal to 80%
text = re.sub(
    r'width:\s*1400px;\s*max-width:\s*95vw;\s*height:\s*90vh;\s*max-height:\s*95vh;',
    r'width: 80vw; max-width: 1200px; height: 80vh; max-height: 80vh;',
    text
)

# 2. Add confirmation logic to the Done button.
# Let's see what the Done button looks like.
# <button type="button" class="btn btn-primary" onclick="submitManageContentsNew()">Done</button>
# Or maybe it's just calling a function. Let's wrap the function body or the onclick.

# Let's search for "submitManageContentsNew()" or whatever function is there.
# If I inject a confirm into the start of `submitManageContentsNew()`, that works perfectly.

# If the JS is simple:
if 'function submitManageContentsNew()' in text:
    text = re.sub(
        r'(function submitManageContentsNew\(\)\s*\{)',
        r'\1\n  if (!confirm("콘텐츠를 추가하시겠습니까?")) return;\n',
        text
    )
elif 'function saveManageContents()' in text:
    text = re.sub(
        r'(function saveManageContents\(\)\s*\{)',
        r'\1\n  if (!confirm("콘텐츠를 추가하시겠습니까?")) return;\n',
        text
    )
else:
    # If the function is named something else, let's find the Done button and change its onclick.
    # Looking for a button that says 'Done'
    text = re.sub(
        r'(<button[^>]*onclick=")([^"]+)("[^>]*>Done<\/button>)',
        r'\1if(confirm(\'콘텐츠를 추가하시겠습니까?\')) { \2 }\3',
        text
    )

with open('CMS-webpage/wireframe_site/package-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Modal reduced to 80% and confirmation added.")
