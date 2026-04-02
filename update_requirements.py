import re

with open('CMS-webpage/wireframe_site/device-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Update "인증 모드" & "라이선스 키" layout to be distinct
old_auth_section = r'''                <div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">인증 모드:</div>
                <select class="input" style="width:100%;" onchange="const isOffline = this.value === 'offline'; document.getElementById\('licenseSection'\)\.style\.display = isOffline \? 'flex' : 'none'; document.getElementById\('licenseLabel'\)\.style\.display = isOffline \? 'block' : 'none';">
                  <option value="online">온라인 인증</option>
                  <option value="offline" selected>오프라인 인증</option>
                </select>

                <div class="info-label" id="licenseLabel" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">라이선스 키:</div>
                <div id="licenseSection" style="display:flex; gap:8px;">
                  <input type="text" list="licenseList" class="input" style="flex:1; font-family:monospace;" value="LIC-OFF-X8B9Q2MA" placeholder="Search License Key...">
                  <datalist id="licenseList">
                    <option value="LIC-OFF-X8B9Q2MA">LIC-OFF-X8B9Q2MA \(Current\)</option>
                    <option value="LIC-OFF-NEW123">LIC-OFF-NEW123 \(Unused\)</option>
                  </datalist>
                    <button type="button" class="btn btn-outline" style="padding:4px 12px; font-size:13px;" onclick="prompt\('새로운 라이선스 키를 재발급 하시겠습니까\? 사유를 입력하세요 \(예: 하드웨어 교체, 포맷 등\) :'\); alert\('새 라이선스\(LIC-OFF-NEW99Z\)가 재발급 되었습니다.'\);">재발급</button>
                    <button type="button" class="btn btn-outline" style="padding:4px 12px; font-size:13px;" onclick="alert\('클립보드에 복사되었습니다.'\)">복사</button>
                  </div>'''

new_auth_section = r'''                <div style="grid-column: 1 / -1; background: #e0e7ff; border: 1px solid #6366f1; border-radius: 8px; padding: 16px; margin: 8px 0;">
                  <div style="display: grid; grid-template-columns: 108px 1fr; gap: 16px 24px; align-items: start;">
                    <div class="info-label" style="font-weight: 600; color: #4338ca; text-align: right; padding-top: 4px;">인증 모드:</div>
                    <select class="input" style="width:100%; border-color:#818cf8; background:#fff;" onchange="const isOffline = this.value === 'offline'; document.getElementById('licenseSection').style.display = isOffline ? 'flex' : 'none'; document.getElementById('licenseLabel').style.display = isOffline ? 'block' : 'none';">
                      <option value="online">온라인 인증</option>
                      <option value="offline" selected>오프라인 인증</option>
                    </select>

                    <div class="info-label" id="licenseLabel" style="font-weight: 600; color: #4338ca; text-align: right; padding-top: 4px;">라이선스 키:</div>
                    <div id="licenseSection" style="display:flex; gap:8px;">
                      <input type="text" list="licenseList" class="input" style="flex:1; font-family:monospace; border-color:#818cf8; background:#fff;" value="LIC-OFF-X8B9Q2MA" placeholder="Search License Key...">
                        <datalist id="licenseList">
                          <option value="LIC-OFF-X8B9Q2MA">LIC-OFF-X8B9Q2MA (Current)</option>
                          <option value="LIC-OFF-NEW123">LIC-OFF-NEW123 (Unused)</option>
                        </datalist>
                        <button type="button" class="btn btn-outline" style="padding:4px 12px; font-size:13px; border-color:#6366f1; color:#4338ca; background:#fff;" onclick="prompt('새로운 라이선스 키를 재발급 하시겠습니까? 사유를 입력하세요 (예: 하드웨어 교체, 포맷 등) :'); alert('새 라이선스(LIC-OFF-NEW99Z)가 재발급 되었습니다.');">재발급</button>
                        <button type="button" class="btn btn-outline" style="padding:4px 12px; font-size:13px; border-color:#6366f1; color:#4338ca; background:#fff;" onclick="alert('클립보드에 복사되었습니다.')">복사</button>
                    </div>
                  </div>
                </div>'''

text = re.sub(old_auth_section, new_auth_section, text)

# 2. Update Hardware Specs Header
old_hw_header = r'<h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px;">🖥️ Hardware Specs \(Meta Data\)</h2>'
new_hw_header = r'''<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px;">
                  <h2 style="font-size: 18px; color: #111827; margin: 0;">🖥️ Hardware Specs (Meta Data)</h2>
                  <span style="font-size:13px; color:#6b7280;">최근 업데이트: 2026-04-01 14:30:22</span>
                </div>'''
text = re.sub(old_hw_header, new_hw_header, text)

# 3. Update Hardware Specs inputs to be read-only text (divs instead of inputs)
old_hw_fields = r'(<div class=\"info-label\"[^>]*>(?:CPU|GPU|RAM|Disk Free|OS Version|Resolution):</div>)\s*<input type=\"text\" class=\"input\" style=\"width:100%\" value=\"(.*?)\">'
new_hw_fields = r'\1\n                  <div style="font-size:14px; font-weight:500; color:#111827; padding-top:4px;">\2</div>'
text = re.sub(old_hw_fields, new_hw_fields, text)

# 4. Update Delete Button in Header
old_del_btn = r'<button class="btn btn-danger" onclick="showDeleteModal\(\)">Delete</button>'
new_del_btn = r'<button class="btn btn-danger" onclick="if(confirm(\'디바이스를 삭제하시겠습니까?\')) { alert(\'삭제되었습니다.\'); location.href=\'device-list.html\'; }">Delete</button>'
text = re.sub(old_del_btn, new_del_btn, text)

with open('CMS-webpage/wireframe_site/device-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)

print('All 4 goals completed.')
