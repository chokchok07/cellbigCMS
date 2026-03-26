import re

with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

old_str = "alert(${action} action for: );"
new_str = """if (action === 'View') return;
          alert(${action} action for: );"""

if old_str in text and "if (action === 'View') return;" not in text:
    text = text.replace(old_str, new_str)
    with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed!")
else:
    print("Already fixed or not found")
