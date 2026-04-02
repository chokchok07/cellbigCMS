import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

view_modal_html = """<div id="viewModal" class="modal-overlay" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; align-items:center; justify-content:center;">
    <div style="background:#fff; width:650px; max-height:85vh; border-radius:8px; display:flex; flex-direction:column; overflow:hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
      
      <!-- Modal Header -->
      <div style="padding:16px 20px; border-bottom:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; background:#f9fafb;">
        <h3 style="margin:0; font-size:18px; color:#111827;">버전 상세 정보 (View & Edit)</h3>
        <button type="button" style="background:transparent; border:none; font-size:24px; cursor:pointer; color:#6b7280;" onclick="closeViewModal()">&times;</button>
      </div>
      
      <!-- Modal Body (Scrollable) -->
      <div style="padding:20px; display:flex; flex-direction:column; gap:20px; overflow-y:auto;">
        
        <!-- 그리드 2단 -->
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px;">
          <div>
            <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 번호 (Version No.)</label>
            <input type="text" class="form-control" value="v1.0.0" disabled style="background:#f3f4f6; color:#9ca3af;">
          </div>
          <div>
            <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">출시일 (Release Date)</label>
            <input type="date" class="form-control" value="2023-10-25">
          </div>
        </div>

        <!-- 업데이트 유형 / 배포 대상 -->
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px;">
          <!-- 업데이트 유형 -->
          <div>
            <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">업데이트 유형 (Update Type)</label>
            <div style="display:flex; gap:12px;">
              <label style="display:flex; align-items:center; gap:4px; font-size:13px; cursor:pointer;">
                <input type="radio" name="viewUpdateType" checked> Content
              </label>
              <label style="display:flex; align-items:center; gap:4px; font-size:13px; cursor:pointer;">
                <input type="radio" name="viewUpdateType"> App
              </label>
              <label style="display:flex; align-items:center; gap:4px; font-size:13px; cursor:pointer;">
                <input type="radio" name="viewUpdateType"> Both
              </label>
            </div>
          </div>
          
          <!-- 배포 대상 -->
          <div>
            <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">배포 대상 (Deploy Target)</label>
            <div style="display:flex; gap:12px;">
              <label style="display:flex; align-items:center; gap:4px; font-size:13px; cursor:pointer;">
                <input type="radio" name="viewDeployTarget" checked> All
              </label>
              <label style="display:flex; align-items:center; gap:4px; font-size:13px; cursor:pointer;">
                <input type="radio" name="viewDeployTarget"> Internal / Group
              </label>
            </div>
          </div>
        </div>

        <!-- 버전 파일 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 파일 (Artifact File)</label>
          <div style="display:flex; gap:8px; align-items:center;">
            <div style="flex:1; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; background:#f9fafb; font-size:13px; color:#111827;">content_v1.0.0.zip</div>
            <button type="button" class="btn btn-outline" style="padding:8px 16px; font-size:13px;" onclick="alert('파일 탐색기가 뜹니다. (시뮬레이션)')">파일 변경</button>
          </div>
          
          <!-- UI 전용: 파일 용량 표시 -->
          <div style="margin-top:8px; font-size:13px; color:#4b5563; display:flex; align-items:center; gap:6px;">
            <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" viewBox="0 0 24 24" stroke="currentColor" style="color:#10b981;">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7" />
            </svg>
            <span>업로드된 파일 용량: <strong style="color:#111827;">150.8 MB</strong></span>
          </div>
        </div>

        <!-- 상태 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">상태 (Status)</label>
          <div style="display:flex; gap:20px; padding:12px; background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px; align-items:center;">
            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input type="radio" name="viewState" style="width:16px; height:16px;">
              <span style="font-size:14px; font-weight:600; color:#4b5563;">Draft</span>
            </label>
            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input type="radio" name="viewState" style="width:16px; height:16px;">
              <span style="font-size:14px; font-weight:600; color:#047857;">Staged</span>
            </label>
            <label style="display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input type="radio" name="viewState" checked style="width:16px; height:16px;">
              <span style="font-size:14px; font-weight:600; color:#1d4ed8;">Published</span>
            </label>
          </div>
        </div>

        <!-- 릴리즈 노트 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">릴리즈 노트 (Release Notes)</label>
          <textarea class="form-control" rows="4" placeholder="해당 버전에 대한 설명이나 변경 사항을 입력하세요.">- 초기 런칭 버전 배포
- 기본 기능 및 에셋 포함</textarea>
        </div>
        
      </div>
      
      <!-- Modal Footer -->
      <div style="padding:16px 20px; border-top:1px solid #e5e7eb; display:flex; justify-content:flex-end; gap:10px; background:#f9fafb;">
        <button type="button" class="btn btn-secondary" onclick="closeViewModal()">닫기</button>
        <button type="button" class="btn btn-primary" onclick="alert('[UI 시뮬레이션] 상세 정보가 성공적으로 수정되었습니다.'); closeViewModal();">저장하기</button>
      </div>
      
    </div>
  </div>"""

# Replace existing viewModal with the new one
html = re.sub(r'<div id=\"viewModal\".*?</script>\s*</body>', view_modal_html + '\n  <script>\n    function showDownloadToast() {\n      const toast = document.getElementById(\'downloadToast\');\n      toast.style.display = \'flex\';\n      setTimeout(() => { toast.style.display = \'none\'; }, 2000);\n    }\n    function openChangeStatusModal() {\n      document.getElementById(\'changeStatusModal\').style.display = \'flex\';\n    }\n    function closeChangeStatusModal() {\n      document.getElementById(\'changeStatusModal\').style.display = \'none\';\n    }\n    function openViewModal() {\n      document.getElementById(\'viewModal\').style.display = \'flex\';\n    }\n    function closeViewModal() {\n      document.getElementById(\'viewModal\').style.display = \'none\';\n    }\n  </script>\n</body>', html, flags=re.DOTALL)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(html)
