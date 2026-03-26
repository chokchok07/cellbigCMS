import io
import re

fp = "CMS-webpage/wireframe_site/localarea-editor.html"
with io.open(fp, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Basic Info block
html = html.replace('''            <div class="form-group">
                <label class="form-label required">LocalArea ID</label>
                <input type="text" class="input" style="width:100%; background:#f3f4f6; color:#9ca3af;" value="" placeholder="(서버에서 자동 생성)" disabled>

              <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right;">Name:</div>
              <input type="text" class="input" style="width:100%;" value="" placeholder="예: 서울 권역 (Seoul Region)">


            </div>''', '''            <div class="form-group">
              <label class="form-label required">LocalArea ID</label>
              <input type="text" class="input" style="width:100%; background:#f3f4f6; color:#9ca3af;" value="" placeholder="(서버에서 자동 생성)" disabled>
            </div>
            
            <div class="form-group">
              <label class="form-label required">Name</label>
              <input type="text" class="input" style="width:100%;" value="" placeholder="예: 서울 권역 (Seoul Region)">
            </div>''')

# Fix Address Grid
html = re.sub(
    r'<div style="display: grid; grid-template-columns: 140px 1fr; gap: 16px 24px; align-items: center; margin-bottom: 24px;">(.*?)<h3',
    r'<div style="display: flex; flex-direction: column; gap: 16px;">\1</div>\n            <h3',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<div class="info-label"[^>]*>Country:</div>\s*<select([^>]*)>(.*?)</select>',
    r'<div class="form-group">\n                <label class="form-label required">Country</label>\n                <select\1>\2</select>\n              </div>',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<div class="info-label"[^>]*>Address:</div>\s*<input([^>]*)value="([^"]*)"([^>]*)>',
    r'<div class="form-group">\n                <label class="form-label">Address</label>\n                <input\1value="" placeholder="예: 서울시 강남구 테헤란로 123"\3>\n              </div>',
    html,
    flags=re.DOTALL
)

html = re.sub(
    r'<div class="info-label"[^>]*>Manager:</div>\s*<input([^>]*)>',
    r'<div class="form-group">\n                <label class="form-label">Manager</label>\n                <input\1>\n              </div>',
    html,
    flags=re.DOTALL
)

with io.open(fp, 'w', encoding='utf-8') as f:
    f.write(html)
print("fixed localarea")
