import re

with open('CMS-webpage/wireframe_site/content-editor.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern for category dropdown under Application Settings
# <div>
#   <label class="form-label required">Category</label>
#   <select class="input" style="width:100%" id="category">
#     ...
#   </select>
# </div>

pattern = re.compile(
    r'<div>\s*<label class="form-label required">Category</label>\s*<select class="input" style="width:100%" id="category">.*?</select>\s*</div>',
    re.DOTALL
)
text = pattern.sub('', text)

# JS code removal
text = re.sub(r"document\.getElementById\('category'\)\.value = '.*?';\n", "", text)

with open('CMS-webpage/wireframe_site/content-editor.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Remaining category fields removed.")
