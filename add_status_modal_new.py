import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Replace Change Status button clicks
html = re.sub(
    r'onclick="alert\(\'상태 변경 모달 오픈\'\)">Change Status</button>',
    r'onclick="openChangeStatusModal(this)">Change Status</button>',
    html
)

# 2. Add JavaScript openChangeStatusModal function and Modal HTML
change_status_html = """
  <!-- Change Status Modal -->
  <div id="changeStatusModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; align-items:center; justify-content:center; padding:20px;">
    <div style="background:#fff; width:450px; border-radius:8px; display:flex; flex-direction:column; overflow:hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
      
      <!-- Modal Header -->
      <div style="padding:16px 20px; border-bottom:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; background:#f9fafb;">
        <h3 style="margin:0; font-size:18px; color:#111827;">배포 상태 변경 (Change Status)</h3>
        <button type="button" style="background:transparent; border:none; font-size:24px; cursor:pointer; color:#6b7280;" onclick="closeChangeStatusModal()">&times;</button>
      </div>
      
      <!-- Modal Body -->
      <div style="padding:20px; display:flex; flex-direction:column; gap:16px;">
        <p style="margin:0; font-size:14px; color:#4b5563;">해당 버전의 현재 배포 상태를 지정하시겠습니까?</p>
        
        <div style="display:flex; flex-direction:column; gap:12px; padding:12px; background:#f9fafb; border:1px solid #e5e7eb; border-radius:6px;">
          <label style="display:flex; align-items:center; gap:8px; cursor:pointer; font-size:14px; padding:4px;">
            <input type="radio" name="changeStatusChoice" value="draft" style="width:16px; height:16px;">
            <span style="font-weight:600; color:#4b5563;">Draft (초안)</span> - 일반 사용자에게 미노출
          </label>
          <label style="display:flex; align-items:center; gap:8px; cursor:pointer; font-size:14px; padding:4px;">
            <input type="radio" name="changeStatusChoice" value="staged" style="width:16px; height:16px;">
            <span style="font-weight:600; color:#047857;">Staged (테스트)</span> - 내부 테스트 기기에서만 다운로드 가능
          </label>
          <label style="display:flex; align-items:center; gap:8px; cursor:pointer; font-size:14px; padding:4px;">
            <input type="radio" name="changeStatusChoice" value="published" style="width:16px; height:16px;">
            <span style="font-weight:600; color:#1d4ed8;">Published (상용/발행)</span> - 운영 대상 기기에 전면 배포
          </label>
          <label style="display:flex; align-items:center; gap:8px; cursor:pointer; font-size:14px; padding:4px;">
            <input type="radio" name="changeStatusChoice" value="deprecated" style="width:16px; height:16px;">
            <span style="font-weight:600; color:#ef4444;">Deprecated (사용 중단)</span> - 더이상 사용 및 다운로드 불가
          </label>
        </div>
      </div>
      
      <!-- Modal Footer -->
      <div style="padding:16px 20px; border-top:1px solid #e5e7eb; display:flex; justify-content:flex-end; gap:10px; background:#f9fafb;">
        <button type="button" class="btn btn-secondary" onclick="closeChangeStatusModal()">취소</button>
        <button type="button" class="btn btn-primary" style="background:#3b82f6; border-color:#3b82f6;" onclick="submitChangeStatus()">적용</button>
      </div>
      
    </div>
  </div>

  <script>
    function openChangeStatusModal(btn) {
      document.getElementById('changeStatusModal').style.display = 'flex';
      
      const radios = document.getElementsByName('changeStatusChoice');
      for(let r of radios) {
        r.checked = false;
      }
    }

    function closeChangeStatusModal() {
      document.getElementById('changeStatusModal').style.display = 'none';
    }

    function submitChangeStatus() {
      const radios = document.getElementsByName('changeStatusChoice');
      let selected = false;
      for(let r of radios) {
        if(r.checked) {
          selected = r.value;
          break;
        }
      }
      
      if(!selected) {
        alert('상태를 먼저 선택해 주세요.');
        return;
      }
      
      // 시뮬레이션
      alert('[' + selected.toUpperCase() + '] 상태로 변경되었습니다!');
      closeChangeStatusModal();
    }
  </script>
</body>
"""

html = html.replace('</body>', change_status_html)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(html)
print("done")