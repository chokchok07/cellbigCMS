import shutil

# Restore from backup
shutil.copy('CMS-webpage/wireframe_site/device-detail.bak2.html', 'CMS-webpage/wireframe_site/device-detail.html')

with open('CMS-webpage/wireframe_site/device-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. FIX AUTH MODE
old_auth = '''<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">인증 모드:</div>
                <div style="display:flex; align-items:center;">
                  <span class="status-badge status-active" style="background:#f0fdf4; color:#166534; padding:4px 8px; border-radius:4px; font-size:12px; font-weight:600; border:1px solid #bbf7d0;">오프라인 인증</span>
                  <span style="margin-left:8px; font-size:13px; color:#6b7280;">(유효기간: 365일)</span>
                </div>'''

new_auth = '''<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">인증 모드:</div>
                <div style="display:flex; align-items:center; gap: 16px; min-height: 38px;">
                    <label style="display:flex; align-items:center; gap:4px; cursor:pointer;">
                      <input type="radio" name="authMode" value="online" style="cursor:pointer; margin:0;" onchange="toggleAuthMode(this.value)"> 
                      <span style="font-size:14px; color:#374151;">🌐 온라인</span>
                    </label>
                    <label style="display:flex; align-items:center; gap:4px; cursor:pointer;">
                      <input type="radio" name="authMode" value="offline" checked style="cursor:pointer; margin:0;" onchange="toggleAuthMode(this.value)"> 
                      <span style="font-size:14px; color:#374151;">🔌 오프라인</span>
                    </label>
                    <button type="button" id="btnDownloadKey" class="pulse-anim" style="display:inline-block; margin-left:auto; padding:4px 12px; background:#10b981; color:white; border:none; border-radius:4px; font-size:12px; cursor:pointer; font-weight: 600;">🔑 Key 발급</button>
                    
                    <script>
                      function toggleAuthMode(val) {
                         const btn = document.getElementById('btnDownloadKey');
                         if(val === 'offline') {
                            btn.style.display = 'inline-block';
                            btn.classList.add('pulse-anim');
                         } else {
                            btn.style.display = 'none';
                            btn.classList.remove('pulse-anim');
                         }
                      }
                    </script>
                    <style>
                      @keyframes popPulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }
                      .pulse-anim { animation: popPulse 1.5s infinite; }
                    </style>
                </div>'''

text = text.replace(old_auth, new_auth)

# 2. MODIFY PACKAGES UI (in the right column)
packages_list = '''<div style="padding: 16px; border: 1px solid #10b981; border-radius: 8px; margin-bottom: 12px; background: #f0fdf4; transition: background 0.2s;" onmouseover="this.style.background='#dcfce7'" onmouseout="this.style.background='#f0fdf4'">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                  <div style="font-weight: 600; color: #065f46; font-size: 14px;">📦 pkg-v1.1 (Active)</div>
                </div>
                <div class="device-info" style="color:#047857; font-size:13px; margin-bottom:4px;">Content: Spring</div>
                <div class="device-info" style="color:#047857; font-size:13px;">Installed: 2d ago</div>
                <button class="btn btn-outline" style="width: 100%; border-color:#34d399; color:#059669; padding: 6px; font-size: 13px; margin-top:8px" onclick="location.href='package-detail.html'">View Package</button>
              </div>

              <div style="padding: 16px; border: 1px solid #e5e7eb; border-radius: 8px; margin-bottom: 12px; background: #fafafa; transition: background 0.2s;" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background='#fafafa'">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 8px;">
                  <div style="font-weight: 600; color: #4b5563; font-size: 14px;">📦 pkg-v1.0 (Backup)</div>
                </div>
                <div class="device-info" style="color:#6b7280; font-size:13px; margin-bottom:4px;">Content: Winter</div>
                <div class="device-info" style="color:#6b7280; font-size:13px;">Installed: 30d</div>
                <button class="btn btn-outline" style="width: 100%; border-color:#d1d5db; color:#4b5563; padding: 6px; font-size: 13px; margin-top:8px" onclick="location.href='package-detail.html'">View Package</button>
              </div>'''

new_packages_ui = '''
              <div style="border: 1px solid #e5e7eb; border-radius: 8px; overflow: hidden; margin-bottom: 12px; background: #fff;">
                <table style="width:100%; border-collapse: collapse; font-size: 13px;">
                  <thead>
                    <tr style="background:#f9fafb; border-bottom:1px solid #e5e7eb;">
                      <th style="padding:8px 12px; text-align:left; font-weight:600; color:#4b5563;">Version</th>
                      <th style="padding:8px 12px; text-align:left; font-weight:600; color:#4b5563;">Content</th>
                      <th style="padding:8px 12px; text-align:right; font-weight:600; color:#4b5563;">Status</th>
                      <th style="padding:8px 12px; text-align:right; font-weight:600; color:#4b5563;">Action</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr style="border-bottom:1px solid #f3f4f6;">
                      <td style="padding:10px 12px; color:#111827; font-weight:500;">pkg-v1.1</td>
                      <td style="padding:10px 12px; color:#6b7280;">Spring</td>
                      <td style="padding:10px 12px; text-align:right;"><span style="color:#10b981; font-weight:600; font-size:12px;">Active</span></td>
                      <td style="padding:10px 12px; text-align:right;">
                         <button type="button" style="padding:4px 8px; background:#fff; border:1px solid #ef4444; color:#ef4444; border-radius:4px; font-size:12px; cursor:pointer;">제거</button>
                      </td>
                    </tr>
                    <tr>
                      <td style="padding:10px 12px; color:#111827; font-weight:500;">pkg-v1.0</td>
                      <td style="padding:10px 12px; color:#6b7280;">Winter</td>
                      <td style="padding:10px 12px; text-align:right;"><span style="color:#9ca3af; font-size:12px;">Backup</span></td>
                      <td style="padding:10px 12px; text-align:right;">
                         <button type="button" style="padding:4px 8px; background:#fff; border:1px solid #ef4444; color:#ef4444; border-radius:4px; font-size:12px; cursor:pointer;">제거</button>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </div>

              <div style="background: #f9fafb; padding:12px; border-radius:8px; border:1px dashed #d1d5db; display:flex; gap:8px; align-items:center;">
                 <select style="flex:1; padding:6px; border:1px solid #d1d5db; border-radius:4px; font-size:13px; outline:none;">
                   <option value="">➕ 추가할 패키지 선택...</option>
                   <option value="pkg-v1.2">pkg-v1.2 (Summer Update)</option>
                   <option value="pkg-admin">pkg-admin-kit</option>
                 </select>
                 <button type="button" style="padding:6px 12px; background:#2563eb; color:#fff; border:none; border-radius:4px; cursor:pointer; font-weight:500; font-size:13px;">설치 (전송)</button>
              </div>
'''

text = text.replace(packages_list, new_packages_ui)

with open('CMS-webpage/wireframe_site/device-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Safely replaced in python!")
