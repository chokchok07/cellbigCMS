import codecs
import re

file_path = 'CMS-webpage/wireframe_site/device-editor.html'
with codecs.open(file_path, 'r', 'utf-8') as f:
    html = f.read()

license_html = """
                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">인증 모드 / 라이선스:</div>
                <div>
                  <select id="authModeSelect" class="input" style="width:100%; margin-bottom: 8px;" onchange="toggleLicenseContainer()">
                    <option value="online">상시 인증 (Online)</option>
                    <option value="offline">오프라인 인증 (Offline License)</option>
                  </select>
                  <div id="licenseContainer" style="display:none; padding:16px; border:1px dashed #d1d5db; border-radius:6px; background:#f9fafb; margin-top:8px;">
                    <div style="font-size:13px; color:#4b5563; margin-bottom:8px; font-weight:600;">오프라인 라이선스 키 발급 (기간 설정)</div>
                    <div style="display:flex; gap:8px; margin-bottom:8px;">
                      <select class="input" style="flex:1;">
                        <option value="90">90일</option>
                        <option value="180">180일</option>
                        <option value="365" selected>1년 (365일)</option>
                        <option value="permanent">영구 (무제한)</option>
                      </select>
                      <button type="button" class="btn btn-primary" style="white-space:nowrap; padding:6px 16px; font-size:13px;" onclick="document.getElementById('licenseKeyInput').value='LIC-' + Math.random().toString(36).substr(2,9).toUpperCase()">키 생성</button>
                    </div>
                    <input type="text" id="licenseKeyInput" class="input" style="width:100%; font-family:monospace; background:#e5e7eb; color:#374151; font-weight:bold;" placeholder="키 생성 버튼을 눌러주세요" readonly>
                  </div>
                </div>

                <script>
                  function toggleLicenseContainer() {
                    const mode = document.getElementById('authModeSelect');
                    if(!mode) return;
                    const container = document.getElementById('licenseContainer');
                    if(mode.value === 'offline') {
                      container.style.display = 'block';
                    } else {
                      container.style.display = 'none';
                    }
                  }
                  // Init
                  document.addEventListener('DOMContentLoaded', toggleLicenseContainer);
                </script>
"""

# Insert before "Name:" input
html = html.replace(
    '<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Name:</div>',
    license_html + '\n                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Name:</div>'
)

with codecs.open(file_path, 'w', 'utf-8') as f:
    f.write(html)
print("Updated editor!")
