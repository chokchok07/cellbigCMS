import re
text = open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8').read()

# remove versionsSection
text = re.sub(r'<div class="card" id="versionsSection".*?<!-- Initial Upload Section', '<!-- Initial Upload Section', text, flags=re.DOTALL)

# remove newVersionModal
text = re.sub(r'<div id="newVersionModal".*?<!-- Script -->', '<!-- Script -->', text, flags=re.DOTALL)

# remove JS functions
text = re.sub(r'function openNewVersionModal\(\) \{.*?\n\s*\}\n', '', text, flags=re.DOTALL)
text = re.sub(r'function closeNewVersionModal\(\) \{.*?\n\s*\}\n', '', text, flags=re.DOTALL)
text = re.sub(r'function submitNewVersion\(\) \{.*?alert\([^)]+\);\n\s*\}\n', '', text, flags=re.DOTALL)

with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Done")
