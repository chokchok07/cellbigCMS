const fs = require('fs');

const editorFile = 'CMS-webpage/wireframe_site/device-editor.html';
let html = fs.readFileSync(editorFile, 'utf8');

const authSection = `
              <div class="card" id="auth-section" style="margin-top:24px;">
                <h2 style="margin-top:0">🔐 인증 및 라이선스 (Authentication)</h2>

                <div class="form-group">
                  <label class="form-label required">인증 방식 (Auth Mode)</label>
                  <select class="input" style="width:100%" id="authMode" onchange="toggleAuthMode()">
                    <option value="ONLINE">네트워크 상시 인증 (Online)</option>
                    <option value="OFFLINE">스탠드얼론 1회성 인증 (Offline / License Key)</option>
                  </select>
                </div>

                <div id="offline-keygen-section" style="display:none; background:#f9fafb; padding:16px; border:1px dashed #d1d5db; border-radius:6px; margin-top:16px;">
                  <label class="form-label">오프라인 시리얼 발급 패키지 선택</label>
                  <div style="display:flex; gap:8px;">
                    <select class="input" style="flex:1" id="licensePackageId">
                      <option value="pkg-sand-11">샌드크래프트 v1.1</option>
                      <option value="pkg-sand-full">샌드크래프트 Full</option>
                      <option value="pkg-fish-basic">물고기잡기 Basic</option>
                    </select>
                    <button class="btn btn-primary" type="button" onclick="generateLicenseKey()">발급하기</button>
                  </div>
                  <div style="margin-top:12px;">
                    <label class="form-label">발급된 라이선스 키</label>
                    <input type="text" class="input" style="width:100%; font-family:monospace; background:#e5e7eb; color:#1f2937; font-weight:bold;" id="generatedLicense" readonly placeholder="여기에 16자리 키가 표시됩니다">
                  </div>
                  <p style="font-size:12px; color:#6b7280; margin-top:8px;">* 오프라인 1회성 인증을 선택한 경우, 이 기기에 등록할 초기 라이선스 키를 즉시 생성할 수 있습니다.</p>
                </div>
              </div>
`;

if (!html.includes('인증 및 라이선스')) {
    html = html.replace(/<div class="form-actions">/, authSection + '\n              <div class="form-actions">');
    
    const jsInjection = `
      function toggleAuthMode() {
        const mode = document.getElementById('authMode').value;
        const offlineSec = document.getElementById('offline-keygen-section');
        
        if (mode === 'OFFLINE') {
          offlineSec.style.display = 'block';
        } else {
          offlineSec.style.display = 'none';
        }
      }
      
      function generateLicenseKey() {
        alert('시리얼 키를 생성했습니다.');
        document.getElementById('generatedLicense').value = 'CBIG-A1B2-C3D4-E5F6';
      }
    `;
    html = html.replace('</script>\n</body>', jsInjection + '\n</script>\n</body>');
    fs.writeFileSync(editorFile, html);
    console.log('Added Auth Mode to device-editor.html');
}
