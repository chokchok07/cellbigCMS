import re

with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Fix Filter Options
old_filter = """<option>Published</option>
              <option>Staged</option>
              <option>Draft</option>
              <option>Deprecated</option>"""

new_filter = """<option>Published</option>
              <option>Test</option>
              <option>Unpublished</option>"""
text = text.replace(old_filter, new_filter)

# 2. Fix Badges
text = re.sub(r'<span class="status-badge status-published">[\s\S]*?</span>', 
              r'<span class="badge badge-published">Published</span>', text)

text = re.sub(r'<span class="status-badge status-staged">[\s\S]*?</span>', 
              r'<span class="badge badge-test">Test</span>', text)

text = re.sub(r'<span class="status-badge status-draft">[\s\S]*?</span>', 
              r'<span class="badge badge-unpublished">Unpublished</span>', text)

text = re.sub(r'<span class="status-badge status-deprecated">[\s\S]*?</span>', 
              r'<span class="badge badge-test">Test</span>', text)

with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Status updated perfectly in content-list.html")
