import io
import re

fp = 'CMS-webpage/wireframe_site/localarea-editor.html'
html = io.open(fp, 'r', encoding='utf-8').read()

html = re.sub(
    r'<div class="form-group">\s*<label class="form-label required">LocalArea ID</label>.*?<input[^>]*disabled>.*?<div class="info-label"[^>]*>Name:</div>\s*<input[^>]*>.*?</div>',
    r'''<div class="form-group">
                <label class="form-label required">LocalArea ID</label>
                <input type="text" class="input" style="width:100%; background:#f3f4f6; color:#9ca3af;" value="" placeholder="(서버에서 자동 생성)" disabled>
            </div>

            <div class="form-group">
                <label class="form-label required">Name</label>
                <input type="text" class="input" style="width:100%;" value="" placeholder="예: 서울 권역">
            </div>''',
    html, flags=re.DOTALL
)

io.open(fp, 'w', encoding='utf-8').write(html)
print('Fixed LA')
