import re

path = 'CMS-webpage/wireframe_site/product-detail.html'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Replace ⚪ Test with 🟡 Test -> and add unpublished row
match_str = r'<td><span style="color:#6b7280">.*?Test</span></td>'
replacement = """<td><span style="color:#f59e0b">🟡 Test</span></td>
                  </tr>
                  <tr>
                    <td><a href="#" class="action-link">Winter Scene</a></td>
                    <td>single</td>
                    <td>v1.0</td>
                    <td><span style="color:#6b7280">⚪ Unpublished</span></td>"""

text = re.sub(match_str, replacement, text)

with open(path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Status updated successfully")
