import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace View button clicks
html = re.sub(
    r'onclick="alert\(\'상세 조회 페이지로 이동\'\)">View</button>',
    r'onclick="openViewModal(this)">View</button>',
    html
)

view_modal_html = """
  <!-- View / Edit Modal -->
  <div id="viewModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; align-items:center; justify-content:center; padding:20px;">
    <div style="background:#fff; width:600px; max-height:85vh; border-radius:8px; display:flex; flex-direction:column; overflow:hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
      
      <!-- Modal Header -->
      <div style="padding:16px 20px; border-bottom:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; background:#f9fafb;">
        <h3 style="margin:0; font-size:18px; color:#111827;">버전 상세정보 (View/Edit Version)</h3>
        <button type="button" style="background:transparent; border:none; font-size:24px; cursor:pointer; color:#6b7280;" onclick="closeViewModal()">&times;</button>
      </div>
      
      <!-- Modal Body (Scrollable) -->
      <div style="padding:20px; display:flex; flex-direction:column; gap:16px; overflow-y:auto;">
        
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px;">
          <div>
            <label style="display:block; margin-bottom:6px; font-weight:600; color:#374151;">버전 번호 (Version No.)</label>
            <input type="text" id="editVersionNo" class="form-control" value="v1.0.0" disabled style="background:#f3f4f6; color:#9ca3af;">
            <small style="color:#6b7280;">버전 번호는 수정할 수 없습니다.</small>
          </div>
          <div>
             <label style="display:block; margin-bottom:6px; font-weight:600; color:#374151;">출시일 (Release Date)</label>
             <input type="date" id="editReleaseDate" class="form-control" value="2023-10-25">
          </div>
        </div>
        
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:16px;">
          <div>
            <label style="display:block; margin-bottom:6px; font-weight:600; color:#374151;">업데이트 유형 (Update Type)</label>
            <select id="editUpdateType" class="form-control">
              <option value="content">Content Update (콘텐츠 변경/추가)</option>
              <option value="app">App Update (앱 엔진 업데이트)</option>
              <option value="both">Both (콘텐츠 및 앱 하이브리드)</option>
            </select>
          </div>
          <div>
            <label style="display:block; margin-bottom:6px; font-weight:600; color:#374151;">배포 대상 (Deploy Target)</label>
            <select id="editDeployTarget" class="form-control">
              <option value="all">All (전체)</option>
              <option value="group">Target Group (특정 그룹)</option>
              <option value="pilot">Pilot Testing (파일럿 테스트)</option>
            </select>
          </div>
        </div>

        <div>
           <label style="display:block; margin-bottom:6px; font-weight:600; color:#374151;">첨부 파일 (Attached File)</label>
           <div style="padding:10px; background:#f9fafb; border:1px solid #e5e7eb; border-radius:4px; display:flex; justify-content:space-between; align-items:center;">
             <span id="editFileInfo">content_v1.0.0.zip (45.2 MB)</span>
             <button type="button" class="btn btn-secondary btn-sm">파일 교체 (선택)</button>
           </div>
        </div>
        
        <div>
           <label style="display:block; margin-bottom:6px; font-weight:600; color:#374151;">릴리즈 노트 / 설명 (Release Notes)</label>
           <textarea id="editReleaseNotes" class="form-control" rows="4" style="resize:vertical;">- 초기 런칭 버전 배포\n- 기본 UI 및 에셋 포함</textarea>
        </div>

      </div>
      
      <!-- Modal Footer -->
      <div style="padding:16px 20px; border-top:1px solid #e5e7eb; display:flex; justify-content:flex-end; gap:10px; background:#f9fafb;">
        <button type="button" class="btn btn-secondary" onclick="closeViewModal()">닫기</button>
        <button type="button" class="btn btn-primary" style="background:#10b981; border-color:#10b981;" onclick="submitViewModal()">변경 저장</button>
      </div>
      
    </div>
  </div>

  <script>
    function openViewModal(btn) {
      // 실제 프로젝트에서는 btn 근처의 데이터를 읽어와서 모달에 채움
      // 여기서는 하드코딩된 더미 데이터를 사용
      const tr = btn.closest('tr');
      if(tr) {
        const verName = tr.querySelector('td:nth-child(2)').innerText.trim();
        document.getElementById('editVersionNo').value = verName;
        document.getElementById('editFileInfo').innerText = 'file_' + verName + '.zip (Size 추정값)';
      }
      
      document.getElementById('viewModal').style.display = 'flex';
    }

    function closeViewModal() {
      document.getElementById('viewModal').style.display = 'none';
    }

    function submitViewModal() {
      // 시뮬레이션
      alert('상세 정보가 성공적으로 수정/저장되었습니다.');
      closeViewModal();
    }
  </script>
</body>
"""

html = html.replace('</body>', view_modal_html)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done editing step 4")