import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Download UI Flow update (replace simulateDownload)
# Previously: onclick="simulateDownload(this)"
# Change to: onclick="showDownloadToast()"
html = re.sub(r'onclick="simulateDownload\(this\)"', r'onclick="showDownloadToast()"', html)

# 2. Change Status UI Flow
html = re.sub(
    r'onclick="alert\(\'상태 변경 모달 오픈\'\)">Change Status</button>',
    r'onclick="openChangeStatusModal()">Change Status</button>',
    html
)
html = re.sub(
    r'onclick="alert\(\'상태 변경 모달 오픈\'\)">\s*Change Status\s*</button>',
    r'onclick="openChangeStatusModal()">Change Status</button>',
    html
)

# 3. View UI Flow
html = re.sub(
    r'onclick="location\.href=\'version-register\.html\'">View</button>',
    r'onclick="openViewModal()">View</button>',
    html
)


# Add Modals and Toasts at the end of the body
modals_html = """
  <!-- 다운로드 토스트 UI -->
  <div id="downloadToast" style="display:none; position:fixed; bottom:20px; right:20px; background:#3b82f6; color:#fff; padding:12px 24px; border-radius:8px; box-shadow:0 4px 6px rgba(0,0,0,0.1); font-size:14px; z-index:10000; align-items:center; gap:8px;">
    <svg width="20" height="20" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
    다운로드가 시작되었습니다...
  </div>

  <!-- Change Status 모달 UI -->
  <div id="changeStatusModal" class="modal-overlay" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; align-items:center; justify-content:center;">
    <div style="background:#fff; width:400px; border-radius:8px; display:flex; flex-direction:column; overflow:hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
      <div style="padding:16px 20px; border-bottom:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; background:#f9fafb;">
        <h3 style="margin:0; font-size:16px; color:#111827;">배포 상태 변경</h3>
        <button type="button" style="background:transparent; border:none; font-size:20px; cursor:pointer;" onclick="closeChangeStatusModal()">&times;</button>
      </div>
      <div style="padding:20px; display:flex; flex-direction:column; gap:12px;">
        <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
          <input type="radio" name="statusOption" checked>
          <span style="font-size:14px;">Draft (초안)</span>
        </label>
        <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
          <input type="radio" name="statusOption">
          <span style="font-size:14px; color:#047857;">Staged (테스트)</span>
        </label>
        <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
          <input type="radio" name="statusOption">
          <span style="font-size:14px; color:#1d4ed8;">Published (상용/발행)</span>
        </label>
        <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
          <input type="radio" name="statusOption">
          <span style="font-size:14px; color:#ef4444;">Deprecated (사용 중단)</span>
        </label>
      </div>
      <div style="padding:16px 20px; border-top:1px solid #e5e7eb; display:flex; justify-content:flex-end; gap:8px; background:#f9fafb;">
        <button type="button" class="btn btn-secondary" onclick="closeChangeStatusModal()">취소</button>
        <button type="button" class="btn btn-primary" onclick="alert('[UI 시뮬레이션] 상태가 변경되었습니다.'); closeChangeStatusModal();">적용</button>
      </div>
    </div>
  </div>

  <!-- View (버전 상세 정보) 모달 UI -->
  <div id="viewModal" class="modal-overlay" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; align-items:center; justify-content:center;">
    <div style="background:#fff; width:500px; border-radius:8px; display:flex; flex-direction:column; overflow:hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
      <div style="padding:16px 20px; border-bottom:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; background:#f9fafb;">
        <h3 style="margin:0; font-size:16px; color:#111827;">버전 상세정보</h3>
        <button type="button" style="background:transparent; border:none; font-size:20px; cursor:pointer;" onclick="closeViewModal()">&times;</button>
      </div>
      <div style="padding:20px; display:flex; flex-direction:column; gap:16px;">
        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:12px;">
          <div>
            <label style="display:block; margin-bottom:4px; font-weight:600; font-size:13px;">버전 번호</label>
            <input type="text" class="form-control" value="v1.0.0" disabled style="background:#f3f4f6;">
          </div>
          <div>
             <label style="display:block; margin-bottom:4px; font-weight:600; font-size:13px;">출시일</label>
             <input type="date" class="form-control" value="2023-10-25">
          </div>
        </div>
        <div>
           <label style="display:block; margin-bottom:4px; font-weight:600; font-size:13px;">상태</label>
           <input type="text" class="form-control" value="Published" disabled style="background:#f3f4f6; color:#1d4ed8; font-weight:bold;">
        </div>
        <div>
           <label style="display:block; margin-bottom:4px; font-weight:600; font-size:13px;">릴리즈 노트</label>
           <textarea class="form-control" rows="3">- 초기 버전 런칭</textarea>
        </div>
      </div>
      <div style="padding:16px 20px; border-top:1px solid #e5e7eb; display:flex; justify-content:flex-end; gap:8px; background:#f9fafb;">
        <button type="button" class="btn btn-secondary" onclick="closeViewModal()">닫기</button>
        <button type="button" class="btn btn-primary" onclick="alert('[UI 시뮬레이션] 상세 정보가 저장되었습니다.'); closeViewModal();">저장</button>
      </div>
    </div>
  </div>

  <script>
    function showDownloadToast() {
      const toast = document.getElementById('downloadToast');
      toast.style.display = 'flex';
      setTimeout(() => { toast.style.display = 'none'; }, 2000);
    }
    function openChangeStatusModal() {
      document.getElementById('changeStatusModal').style.display = 'flex';
    }
    function closeChangeStatusModal() {
      document.getElementById('changeStatusModal').style.display = 'none';
    }
    function openViewModal() {
      document.getElementById('viewModal').style.display = 'flex';
    }
    function closeViewModal() {
      document.getElementById('viewModal').style.display = 'none';
    }
  </script>
</body>
"""

# Only append if not already in file
if 'changeStatusModal' not in html:
    html = html.replace('</body>', modals_html)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Modals added and buttons updated.")
