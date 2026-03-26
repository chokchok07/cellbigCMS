import re

file_path = "CMS-webpage/wireframe_site/content-versions.html"

with open(file_path, "r", encoding="utf-8") as f:
    html_content = f.read()

# 1. Expand the grid columns to allow Date column to stand alone
html_content = html_content.replace('grid-template-columns: 2fr 1fr 1fr', 'grid-template-columns: 2fr 1fr 1fr 1fr')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html_content)

print(f"File updated. Columns replaced: {html_content.count('grid-template-columns: 2fr 1fr 1fr 1fr')}")
