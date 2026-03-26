with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = "alert(`${action} action for: ${title}`);"
replacement = "if (action === 'View') return;\n          alert(`${action} action for: ${title}`);"

if pattern in text:
    text = text.replace(pattern, replacement)
    with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed!")
else:
    print("Pattern not found!")
