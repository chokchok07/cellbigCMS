import re

with open('CMS-webpage/wireframe_site/version-register.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace <div class="form-group"> for release notes to inject State before it
new_html = '''
            <!-- 상태 (Draft / Test / Published) -->
            <div class="form-group">
              <label>버전 상태 지정</label>
              <div class="radio-group" style="padding: 10px; background: #f9fafb; border-radius: 6px; border: 1px solid #e5e7eb;">
                <div class="radio-option">
                  <input type="radio" id="stateDraft" name="versionState" value="draft" checked>
                  <label for="stateDraft" style="font-weight:600; color:#4b5563;">Draft (초안)</label>
                </div>
                <div class="radio-option">
                  <input type="radio" id="stateStaged" name="versionState" value="staged">
                  <label for="stateStaged" style="font-weight:600; color:#047857;">Staged (테스트 배포)</label>
                </div>
                <div class="radio-option">
                  <input type="radio" id="statePublished" name="versionState" value="published">
                  <label for="statePublished" style="font-weight:600; color:#1d4ed8;">Published (즉시 상용 배포)</label>
                </div>
              </div>
              <div style="font-size:12px; color:#6b7280; margin-top:6px;">새 버전을 업로드 시 기본 상태는 'Draft(초안)'이며, 의도치 않은 즉시 상용 배포를 막기 위함입니다.</div>
            </div>

            <!-- 버전 설명 -->
'''

content = content.replace('<!-- 버전 설명 -->', new_html)

# Update state in JavaScript
content = content.replace(\"state: 'draft'\", 'state: document.querySelector(\\'input[name=\"versionState\"]:checked\\').value')

with open('CMS-webpage/wireframe_site/version-register.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated version-register.html")

