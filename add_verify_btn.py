import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

target_html = """        <!-- 버전 파일 및 크기 확인 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 파일 (Artifact File)</label>
          <div style="display:flex; gap:8px; align-items:center; margin-bottom:8px;">
            <div style="flex:1; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; background:#f9fafb; font-size:13px; color:#6b7280;" id="versionFileName">파일을 선택해 주세요. (.zip)</div>
            <input type="file" id="versionFile" style="display:none" accept=".zip" onchange="handleVersionFileSelect(event)">
            <button type="button" class="btn btn-outline" style="padding:8px 16px; font-size:13px;" onclick="document.getElementById('versionFile').click()">파일 찾기</button>
          </div>
          <div style="font-size:13px; display:none; color:#3b82f6;" id="versionFileSize"></div>
        </div>"""

replacement_html = """        <!-- 버전 파일 및 크기 확인 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 파일 (Artifact File)</label>
          <div style="display:flex; gap:8px; align-items:center; margin-bottom:8px;">
            <div style="flex:1; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; background:#f9fafb; font-size:13px; color:#6b7280;" id="versionFileName">파일을 선택해 주세요. (.zip)</div>
            <input type="file" id="versionFile" style="display:none" accept=".zip" onchange="handleVersionFileSelect(event)">
            <button type="button" class="btn btn-outline" style="padding:8px 16px; font-size:13px;" onclick="document.getElementById('versionFile').click()">파일 찾기</button>
          </div>
          
          <!-- 새롭게 추가(복구)된 파일 확인 영역 -->
          <div style="display:flex; gap:12px; align-items:center; font-size:13px; display:none;" id="versionFileVerificationArea">
            <div style="background:#f3f4f6; padding:6px 12px; border-radius:4px; flex:1;">
              <strong>파일 크기:</strong> <span id="versionFileSize" style="color:#3b82f6; font-weight:bold;">0 MB</span>
            </div>
            <button type="button" id="verifyVersionFileBtn" class="btn" style="padding:6px 12px; background:#10b981; color:white; border:none; border-radius:4px; cursor:pointer;" onclick="alert('파일 검증(Verify)을 통과했습니다!')">파일 확인 (Verify)</button>
          </div>
        </div>"""

html = html.replace(target_html, replacement_html)

target_js = """    function handleVersionFileSelect(event) {
      const file = event.target.files[0];
      if (file) {
        document.getElementById('versionFileName').innerText = file.name;
        
        const sizeMB = (file.size / (1024 * 1024)).toFixed(2);
        const sizeDisplay = document.getElementById('versionFileSize');
        sizeDisplay.style.display = 'block';
        sizeDisplay.innerHTML = `파일 크기: <strong>${sizeMB} MB</strong>`;
      }
    }"""

replacement_js = """    function handleVersionFileSelect(event) {
      const file = event.target.files[0];
      if (file) {
        document.getElementById('versionFileName').innerText = file.name;
        
        const sizeMB = (file.size / (1024 * 1024)).toFixed(2);
        
        // 파일 영역 Display ON 및 용량 표시
        document.getElementById('versionFileVerificationArea').style.display = 'flex';
        document.getElementById('versionFileSize').innerText = `${sizeMB} MB`;
      }
    }"""

html = html.replace(target_js, replacement_js)

# js reset
target_js_reset = """    function closeNewVersionModal() {
      document.getElementById('newVersionModal').style.display = 'none';
      // Reset values if needed
      document.getElementById('versionFileName').innerText = '파일을 선택해 주세요. (.zip)';
      document.getElementById('versionFileSize').style.display = 'none';
      document.getElementById('versionFile').value = '';
    }"""

replacement_js_reset = """    function closeNewVersionModal() {
      document.getElementById('newVersionModal').style.display = 'none';
      document.getElementById('versionFileName').innerText = '파일을 선택해 주세요. (.zip)';
      
      const vArea = document.getElementById('versionFileVerificationArea');
      if (vArea) vArea.style.display = 'none';
      
      document.getElementById('versionFile').value = '';
    }"""

html = html.replace(target_js_reset, replacement_js_reset)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(html)
