import re
import glob
import os

css_path = 'CMS-webpage/wireframe_site/styles.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css_content = f.read()

# Make sure we add test and unpublished styles to styles.css
if '.badge-test' not in css_content:
    css_add = """
.badge-test, .status-test { background: #fef08a; color: #92400e; }
.badge-unpublished, .status-unpublished { background: #f3f4f6; color: #4b5563; }
"""
    css_content += css_add
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)

for filepath in glob.glob('CMS-webpage/wireframe_site/*.html'):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    original_text = text
    
    # 1. Replace "Staged" or "staged" with Test or Unpublished
    # Let's replace 'Staged' with 'Test' and 'staged' with 'test' for class names
    text = re.sub(r'\bStaged\b', 'Test', text)
    text = re.sub(r'\bstaged\b', 'test', text)
    text = re.sub(r'⏳\s*Test', '', text) # clean up emoji if we just replaced Staged -> Test
    
    # In content-list.html specifically
    text = re.sub(r'<span class="status-badge status-test">\s*<span>\s*</span>', '<span class=\"badge badge-test\">Test</span>', text)

    # 2. Convert remaining 'status-test', 'status-unpublished', 'status-published' to badge classes where applicable to unify
    text = re.sub(r'class="status-badge status-published"[^>]*>Published</span>', 'class="badge badge-published">Published</span>', text)
    text = re.sub(r'class="status-badge status-test"[^>]*>Test</span>', 'class="badge badge-test">Test</span>', text)
    text = re.sub(r'class="status-badge status-unpublished"[^>]*>Unpublished</span>', 'class="badge badge-unpublished">Unpublished</span>', text)

    text = re.sub(r'class="badge badge-draft"', 'class="badge badge-unpublished"', text)
    text = re.sub(r'>Draft<', '>Unpublished<', text)

    if text != original_text:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Updated {filepath}")

print("Cleaned up 'Staged' and unified colors in CSS.")
