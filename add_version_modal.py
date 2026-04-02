import re

file_path = 'CMS-webpage/wireframe_site/content-versions.html'
with open(file_path, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update the + New Version button
html = re.sub(
    r'<button class="btn btn-primary" onclick="location\.href=\'version-register\.html\'">\+ New Version</button>',
    r'<button class="btn btn-primary" onclick="openNewVersionModal()">+ New Version</button>',
    html
)

# 2. Add New Version Modal HTML and JS before </body>
modal_html = """
  <!-- New Version Modal -->
  <div id="newVersionModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; align-items:center; justify-content:center; padding:20px;">
    <div style="background:#fff; width:600px; max-height:90vh; border-radius:8px; display:flex; flex-direction:column; overflow:hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
      
      <!-- Modal Header -->
      <div style="padding:16px 20px; border-bottom:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; background:#f9fafb;">
        <h3 style="margin:0; font-size:18px; color:#111827;" id="modalVersionTitle">새 버전 업로드 (+ New Version)</h3>
        <button type="button" style="background:transparent; border:none; font-size:24px; cursor:pointer; color:#6b7280;" onclick="closeNewVersionModal()">&times;</button>
      </div>
      
      <!-- Modal Body -->
      <div style="padding:20px; overflow-y:auto; display:flex; flex-direction:column; gap:24px;">
        
        <!-- 버전 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 (Version)</label>
          <div style="display:flex; align-items:center; gap:8px;">
            <input type="number" id="versionMajor" min="0" max="999" value="1" style="width:70px; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; text-align:center;">
            <span style="font-weight:bold; color:#6b7280;">.</span>
            <input type="number" id="versionMinor" min="0" max="999" value="0" style="width:70px; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; text-align:center;">
            <span style="font-weight:bold; color:#6b7280;">.</span>
            <input type="number" id="versionPatch" min="0" max="999" value="0" style="width:70px; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; text-align:center;">
          </div>
        </div>

        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px;">
          <!-- 업데이트 타입 -->
          <div>
            <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">업데이트 유형</label>
            <div style="display:flex; gap:16px;">
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
                <input type="radio" name="updateType" value="forced" style="width:16px; height:16px;">
                <span style="font-size:13px;">강제 업데이트</span>
              </label>
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
                <input type="radio" name="updateType" value="optional" checked style="width:16px; height:16px;">
                <span style="font-size:13px;">선택 업데이트</span>
              </label>
            </div>
          </div>

          <!-- 배포 환경 -->
          <div>
            <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">배포 환경</label>
            <div style="display:flex; gap:16px;">
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
                <input type="radio" name="deploymentTarget" value="production" style="width:16px; height:16px;">
                <span style="font-size:13px;">상용 (Production)</span>
              </label>
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
                <input type="radio" name="deploymentTarget" value="test" checked style="width:16px; height:16px;">
                <span style="font-size:13px;">테스트 (Test)</span>
              </label>
            </div>
          </div>
        </div>

        <!-- 버전 파일 및 크기 확인 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 파일 (Artifact File)</label>
          <div style="display:flex; gap:8px; align-items:center; margin-bottom:8px;">
            <div style="flex:1; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; background:#f9fafb; font-size:13px; color:#6b7280;" id="versionFileName">파일을 선택해 주세요. (.zip)</div>
            <input type="file" id="versionFile" style="display:none" accept=".zip" onchange="handleVersionFileSelect(event)">
            <button type="button" class="btn btn-outline" style="padding:8px 16px; font-size:13px;" onclick="document.getElementById('versionFile').click()">파일 찾기</button>
          </div>
          <div style="font-size:13px; display:none; color:#3b82f6;" id="versionFileSize"></div>
        </div>

        <!-- 상태 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">상태 (Status)</label>
          <div style="display:flex; gap:20px; padding:12px; background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; align-items:center;">
            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input type="radio" name="versionState" value="draft" checked style="width:16px; height:16px;">
              <span style="font-size:14px; font-weight:600; color:#4b5563;">Draft (초안)</span>
            </label>
            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input type="radio" name="versionState" value="staged" style="width:16px; height:16px;">
              <span style="font-size:14px; font-weight:600; color:#047857;">Staged (테스트)</span>
            </label>
            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input type="radio" name="versionState" value="published" style="width:16px; height:16px;">
              <span style="font-size:14px; font-weight:600; color:#1d4ed8;">Published (상용)</span>
            </label>
          </div>
        </div>

        <!-- 버전 설명 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 설명 (Release Notes)</label>
          <textarea id="versionReleaseNotes" style="width:100%; min-height:100px; padding:12px; border:1px solid #d1d5db; border-radius:4px; font-family:inherit; font-size:13px; resize:vertical;" placeholder="변경 사항 및 배포 노트를 입력하세요."></textarea>
        </div>

      </div>
      
      <!-- Modal Footer -->
      <div style="padding:16px 20px; border-top:1px solid #e5e7eb; display:flex; justify-content:flex-end; gap:10px; background:#f9fafb;">
        <button type="button" class="btn btn-secondary" onclick="closeNewVersionModal()">취소</button>
        <button type="button" class="btn btn-primary" onclick="submitNewVersion()">버전 등록</button>
      </div>
      
    </div>
  </div>

  <script>
    function openNewVersionModal() {
      document.getElementById('newVersionModal').style.display = 'flex';
    }

    function closeNewVersionModal() {
      document.getElementById('newVersionModal').style.display = 'none';
      // Reset values if needed
      document.getElementById('versionFileName').innerText = '파일을 선택해 주세요. (.zip)';
      document.getElementById('versionFileSize').style.display = 'none';
      document.getElementById('versionFile').value = '';
    }

    function handleVersionFileSelect(event) {
      const file = event.target.files[0];
      if (file) {
        document.getElementById('versionFileName').innerText = file.name;
        
        const sizeMB = (file.size / (1024 * 1024)).toFixed(2);
        const sizeDisplay = document.getElementById('versionFileSize');
        sizeDisplay.style.display = 'block';
        sizeDisplay.innerHTML = `파일 크기: <strong>${sizeMB} MB</strong>`;
      }
    }

    function submitNewVersion() {
      const major = document.getElementById('versionMajor').value;
      const minor = document.getElementById('versionMinor').value;
      const patch = document.getElementById('versionPatch').value;
      
      if (!document.getElementById('versionFile').files[0]) {
        alert('버전 파일(.zip)을 등록해주세요.');
        return;
      }
      
      alert(`v${major}.${minor}.${patch} 버전이 성공적으로 등록되었습니다!`);
      closeNewVersionModal();
    }
  </script>
</body>
"""

html = html.replace('</body>', modal_html)

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated 1. New Version modal.')
