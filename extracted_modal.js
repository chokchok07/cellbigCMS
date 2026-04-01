// New Version Modal Logic
    function openNewVersionModal() {
      document.getElementById('newVersionModal').style.display = 'flex';
    }

    function closeNewVersionModal() {
      document.getElementById('newVersionModal').style.display = 'none';
      document.getElementById('newVersionFile').value = '';
      document.getElementById('newVersionFileName').textContent = '파일을 선택해 주세요.';
      document.getElementById('newVersionFileName').style.color = '#6b7280';
      document.getElementById('newVersionFileSize').textContent = '0 MB';
      
      const verifyBtn = document.getElementById('verifyFileBtn');
      verifyBtn.disabled = true;
      verifyBtn.style.cursor = 'not-allowed';
      verifyBtn.style.opacity = '0.6';
    }

    function handleNewVersionFileSelect(event) {
      if(event.target.files.length > 0) {
        const file = event.target.files[0];
        document.getElementById('newVersionFileName').textContent = file.name;
        document.getElementById('newVersionFileName').style.color = '#111827';
        
        // Mock file size config
        const sizeMB = (file.size / (1024 * 1024)).toFixed(2);
        document.getElementById('newVersionFileSize').textContent = sizeMB + ' MB';

        const verifyBtn = document.getElementById('verifyFileBtn');
        verifyBtn.disabled = false;
        verifyBtn.style.cursor = 'pointer';
        verifyBtn.style.opacity = '1';
      }
    }

    function submitNewVersion() {
      const vMajor = document.getElementById('versionMajor').value;
      const vMinor = document.getElementById('versionMinor').value;
      const vPatch = document.getElementById('versionPatch').value;
      
      alert(`v${vMajor}.${vMinor}.${vPatch} 버전이 성공적으로 등록되었습니다!`);
      closeNewVersionModal();
      // In a real scenario, this would update the version list UI dynamically
    }
  </script>

  <!-- New Version Modal -->
  <div id="newVersionModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; align-items:center; justify-content:center; padding:20px;">
    <div style="background:#fff; width:600px; max-width:100%; max-height:90vh; border-radius:8px; display:flex; flex-direction:column; overflow:hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
      
      <!-- Modal Header -->
      <div style="padding:16px 20px; border-bottom:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; background:#f9fafb;">
        <h3 style="margin:0; font-size:18px; color:#111827;">새 버전 업로드 (+ New Version)</h3>
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
            <input type="number" id="versionMinor" min="0" max="999" value="4" style="width:70px; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; text-align:center;">
            <span style="font-weight:bold; color:#6b7280;">.</span>
            <input type="number" id="versionPatch" min="0" max="999" value="0" style="width:70px; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; text-align:center;">
          </div>
        </div>

        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px;">
          <!-- 업데이트 타입 -->
          <div>
            <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">업데이트 유형</label>
            <div style="display:flex; gap:16px;">
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;" for="updateForced">
                <input type="radio" id="updateForced" name="updateType" value="forced" style="width:16px; height:16px;">
                <span style="font-size:13px;">강제 업데이트</span>
              </label>
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;" for="updateOptional">
                <input type="radio" id="updateOptional" name="updateType" value="optional" checked style="width:16px; height:16px;">
                <span style="font-size:13px;">선택 업데이트</span>
              </label>
            </div>
          </div>

          <!-- 배포 환경 -->
          <div>
            <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">배포 환경</label>
            <div style="display:flex; gap:16px;">
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;" for="deployProduction">
                <input type="radio" id="deployProduction" name="deploymentTarget" value="production" style="width:16px; height:16px;">
                <span style="font-size:13px;">상용 (Production)</span>
              </label>
              <label style="display:flex; align-items:center; gap:6px; cursor:pointer;" for="deployTest">
                <input type="radio" id="deployTest" name="deploymentTarget" value="test" checked style="width:16px; height:16px;">
                <span style="font-size:13px;">테스트 (Test)</span>
              </label>
            </div>
          </div>
        </div>

        <!-- 버전 파일 및 확인 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 파일 (Artifact File)</label>
          <div style="display:flex; gap:8px; align-items:center; margin-bottom:8px;">
            <div style="flex:1; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; background:#f9fafb; font-size:13px; color:#6b7280;" id="newVersionFileName">파일을 선택해 주세요.</div>
            <input type="file" id="newVersionFile" style="display:none" accept=".zip" onchange="handleNewVersionFileSelect(event)">
            <button type="button" class="btn btn-outline" style="padding:8px 16px; font-size:13px;" onclick="document.getElementById('newVersionFile').click()">파일 찾기</button>
          </div>
          <div style="display:flex; gap:12px; align-items:center; font-size:13px;">
            <div style="background:#f3f4f6; padding:6px 12px; border-radius:4px; flex:1;">
              <strong>파일 크기:</strong> <span id="newVersionFileSize">0 MB</span>
            </div>
            <button type="button" id="verifyFileBtn" class="btn" style="padding:6px 12px; background:#10b981; color:white; border:none; border-radius:4px; cursor:not-allowed; opacity:0.6;" disabled onclick="alert('파일 확인 완료!')">파일 확인 (Verify)</button>
          </div>
        </div>

        <!-- 상태 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">상태 (Status)</label>
          <div style="display:flex; gap:20px; padding:12px; background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; align-items:center;">
            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;" for="stateDraft">
              <input type="radio" id="stateDraft" name="versionState" value="draft" checked style="width:16px; height:16px;">
              <span style="font-size:14px; font-weight:600; color:#4b5563;">Draft (초안)</span>
            </label>
            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;" for="stateStaged">
              <input type="radio" id="stateStaged" name="versionState" value="staged" style="width:16px; height:16px;">
              <span style="font-size:14px; font-weight:600; color:#047857;">Staged (테스트)</span>
            </label>
            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;" for="statePublished">
              <input type="radio" id="statePublished" name="versionState" value="published" style="width:16px; height:16px;">
              <span style="font-size:14px; font-weight:600; color:#1d4ed8;">Published (발행)</span>
            </label>
          </div>
          <div style="font-size:12px; color:#6b7280; margin-top:6px;">새 버전을 업로드 시 기본 상태는 'Draft(초안)'이며, 의도치 않은 상용 배포를 방지합니다.</div>
        </div>

        <!-- 버전 설명 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 설명 (Release Notes)</label>
          <textarea id="releaseNotes" style="width:100%; min-height:100px; padding:12px; border:1px solid #d1d5db; border-radius:4px; font-family:inherit; font-size:13px; resize:vertical;" placeholder="변경 사항 및 배포 노트를 입력하세요."></textarea>
        </div>

      </div>
      
      <!-- Modal Footer -->
      <div style="padding:16px 20px; border-top:1px solid #e5e7eb; display:flex; justify-content:flex-end; gap:10px; background:#f9fafb;">
        <button type="button" class="btn btn-secondary" onclick="closeNewVersionModal()">취소</button>
        <button type="button" class="btn btn-primary" onclick="submitNewVersion()">버전 등록</button>
      </div>
      
    </div>
  </div>

  <!-- Inactive Confirm Modal -->
  <div id="statusConfirmModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999; justify-content: center; align-items: center;">
      <div style="background: #fff; width: 400px; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
        <div style="padding: 16px 24px; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center;">
          <h3 style="margin: 0; font-size: 1.125rem; font-weight: 600; color: #111827;" id="statusModalTitle">상태 변경</h3>
          <button type="button" onclick="closeStatusModal()" style="background: none; border: none; font-size: 1.25rem; cursor: pointer; color: #6b7280;">&times;</button>
        </div>
        <div style="padding: 24px;">
          <p style="margin: 0; color: #374151; font-size: 1rem;" id="statusModalMessage">변경 하시겠습니까?</p>
        </div>
        <div style="padding: 16px 24px; border-top: 1px solid #e5e7eb; display: flex; justify-content: flex-end; gap: 8px; background: #f9fafb;">
          <button type="button" class="btn btn-secondary" onclick="closeStatusModal()">취소</button>
          <button type="button" class="btn btn-primary" id="statusConfirmBtn" onclick="confirmStatus()">확인</button>
        </div>
      </div>
    </div>
    <script>
      let currentStatusAction = '';
      function openStatusModal(action) {
        currentStatusAction = action;
        const modal = document.getElementById('statusConfirmModal');
        const title = document.getElementById('statusModalTitle');
        const message = document.getElementById('statusModalMessage');
        const confirmBtn = document.getElementById('statusConfirmBtn');
        
        if (action === 'active') {
          title.innerText = '활성화 확인';
          message.innerText = '활성화 하시겠습니까?';
          confirmBtn.innerText = '활성화';
          confirmBtn.style.background = '#10b981';
          confirmBtn.style.borderColor = '#10b981';
        } else {
          title.innerText = '비활성화 확인';
          message.innerText = '비활성화 하시겠습니까?';
          confirmBtn.innerText = '비활성화';
          confirmBtn.style.background = '#ef4444';
          confirmBtn.style.borderColor = '#ef4444';
        }
        
        modal.style.display = 'flex';
      }
      function closeStatusModal() {
        document.getElementById('statusConfirmModal').style.display = 'none';
      }
      function confirmStatus() {
        closeStatusModal();
      }
      
      document.addEventListener('DOMContentLoaded', () => {
        // Also bind any generic Active/Inactive buttons in table lists
        document.querySelectorAll('.btn-danger, .btn-success, .btn').forEach(btn => {
          if(btn.innerText.includes('Inactive') && !btn.hasAttribute('onclick')) {
            btn.addEventListener('click', () => openStatusModal('inactive'));
          }
          if(btn.innerText.includes('Active') && !btn.hasAttribute('onclick')) {
            btn.addEventListener('click', () => openStatusModal('active'));
          }
        }