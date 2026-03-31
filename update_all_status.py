import re

def update_status_in_file(filepath, replacements, css_snippet=None):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    for old, new in replacements:
        if isinstance(old, re.Pattern):
            text = old.sub(new, text)
        else:
            text = text.replace(old, new)
            
    if css_snippet and '</style>' in text and css_snippet not in text:
        text = text.replace('</style>', f'{css_snippet}\n  </style>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(text)

css = """
    .badge-test { background: #fef3c7; color: #b45309; }
    .badge-unpublished { background: #f3f4f6; color: #4b5563; }
    .status-test { background: #fef3c7; color: #b45309; }
    .status-unpublished { background: #f3f4f6; color: #4b5563; }
"""

# package-list.html
update_status_in_file('CMS-webpage/wireframe_site/package-list.html', [
    ('<option value="Draft">Draft</option>', '<option value="Test">Test</option>\n                    <option value="Unpublished">Unpublished</option>'),
    ('badge-draft">Draft</span>', 'badge-unpublished">Unpublished</span>'),
    # change one of the published to test just to show it
    ('<td><span class="badge badge-published">Published</span></td>\n                        <td>v2.0', '<td><span class="badge badge-test">Test</span></td>\n                        <td>v2.0')
], css_snippet=css)

# package-detail.html
update_status_in_file('CMS-webpage/wireframe_site/package-detail.html', [
    ('<option value="draft">Draft</option>', '<option value="test">Test</option>\n                      <option value="unpublished">Unpublished</option>'),
    ('badge-draft">Draft</span>', 'badge-unpublished">Unpublished</span>')
], css_snippet=css)

# content-list.html
update_status_in_file('CMS-webpage/wireframe_site/content-list.html', [
    ('<option>Draft</option>', '<option>Test</option>\n                    <option>Unpublished</option>'),
    ('<option>Deprecated</option>', ''),
    ('📝 Draft', '⚪ Unpublished'),
    ('🚫 Deprecated', '🟡 Test'),  # Change deprecated to test for variety
], css_snippet=css)

# content-detail.html
update_status_in_file('CMS-webpage/wireframe_site/content-detail.html', [
    ('Draft (초안)', 'Unpublished (미발행)'),
    ('<option>Draft</option>', '<option>Test</option>\n                  <option>Unpublished</option>'),
    ('Deprecated</span>', 'Test</span>'),
    ('Draft</span>', 'Unpublished</span>')
], css_snippet=css)

print("Updated package and content files.")
