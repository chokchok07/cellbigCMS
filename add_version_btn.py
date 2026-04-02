import re

# 1. Modify content-list.html to add "Version" button
with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

# We look for the action buttons in content-list.html
# Example: <button class="action-btn" onclick="window.location.href='content-editor.html?id=101'">View</button>
text = re.sub(
    r'(<button class="action-btn" onclick="window\.location\.href=\'content-editor\.html\?id=\d+\'">View<\/button>\s*)',
    r'\1<button class="action-btn version-btn" onclick="window.location.href=\'content-versions.html?id=101\'" style="margin-left:4px; background-color:#6366f1; color:white; border-color:#6366f1;">Version</button>\n',
    text
)

with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated content-list.html successfully.")
