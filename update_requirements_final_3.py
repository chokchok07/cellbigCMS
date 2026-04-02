import re

fname = 'CMS-webpage/wireframe_site/package-detail.html'
with open(fname, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Expand the modal size (wait, it was 600px -> make it 900px)
html = html.replace('width: 600px;', 'width: 900px;')

# 2. Remove the "상태" column from the UI table headers
html = html.replace('<th style="padding: 12px; text-align: center; font-size: 13px; color: #4b5563;">상태</th>\n', '')

# 3. Remove the badges from the body (✔ 포함됨, 미포함)
html = re.sub(
    r'<td style="padding: 12px; text-align: center;">\s*<span style="display:inline-block; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 600; background: #def7ec; color: #03543f;">✔ 포함됨</span>\s*</td>',
    '',
    html
)
html = re.sub(
    r'<td style="padding: 12px; text-align: center;">\s*<span style="display:inline-block; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 600; background: #f3f4f6; color: #6b7280;">미포함</span>\s*</td>',
    '',
    html
)

with open(fname, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated modal HTML")