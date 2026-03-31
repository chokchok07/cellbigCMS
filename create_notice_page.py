import re

with open('CMS-webpage/wireframe_site/localarea-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make it notice-list.html. Ensure the sidebar is active for notice-list.html, not localarea-list.html.
html = html.replace('<div class="sidebar-item active" data-page="localarea-list.html">', '<div class="sidebar-item" data-page="localarea-list.html">')
html = html.replace('<div class="sidebar-item" data-page="notice-list.html">', '<div class="sidebar-item active" data-page="notice-list.html">')

# Modify breadcrumb
html = re.sub(
    r'<div class="breadcrumb".*?</div>',
    r'''<div class="breadcrumb" style="font-size: 13px; color: #6b7280; margin-bottom: 20px; display:flex; gap:8px; align-items:center;">
        <span style="cursor:pointer; padding: 4px 8px; border-radius: 4px; transition: background 0.2s;" onmouseover="this.style.background='#e5e7eb'" onmouseout="this.style.background='transparent'" onclick="location.href='index.html'">🏠 Home</span>
        <span style="color: #d1d5db;">/</span>
        <span style="color: #374151; font-weight: 600; padding: 4px 8px;">📢 Notice</span>
    </div>''',
    html,
    flags=re.DOTALL
)

# New Main Content replacement
new_main_content = """    <main class="main-content">
      <div class="container">
        
        <div class="breadcrumb" style="font-size: 13px; color: #6b7280; margin-bottom: 20px; display:flex; gap:8px; align-items:center;">
          <span style="cursor:pointer; padding: 4px 8px; border-radius: 4px; transition: background 0.2s;" onmouseover="this.style.background='#e5e7eb'" onmouseout="this.style.background='transparent'" onclick="location.href='index.html'">🏠 Home</span>
          <span style="color: #d1d5db;">/</span>
          <span style="color: #374151; font-weight: 600; padding: 4px 8px;">📢 Notice</span>
        </div>

        <div class="page-header" style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom: 24px;">
          <div>
            <h1 class="page-title" style="margin:0; font-size:24px; color:#111827;">📢 공지사항</h1>
            <p class="page-desc" style="margin:8px 0 0 0; color:#6b7280;">시스템 업데이트 및 중요 안내 사항을 관리합니다.</p>
          </div>
          <div class="header-actions">
            <button type="button" class="btn btn-primary" onclick="openNoticeModal()" style="padding:8px 16px; background-color:#2563eb; color:white; border:none; border-radius:6px; font-weight:500; cursor:pointer;">+ 공지 등록</button>
          </div>
        </div>

        <div class="card" style="background:#fff; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.1); overflow:hidden;">
          <table class="data-table" style="width:100%; border-collapse:collapse; text-align:left;">
            <thead>
              <tr style="background:#f9fafb; border-bottom:1px solid #e5e7eb;">
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb; width:80px; text-align:center;">번호</th>
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb;">제목</th>
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb; width:120px; text-align:center;">작성자</th>
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb; width:120px; text-align:center;">등록일</th>
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb; width:80px; text-align:center;">조회수</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #e5e7eb; cursor:pointer;" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background=''" onclick="openNoticeViewModal(3)">
                <td style="padding:16px; text-align:center; color:#6b7280;">3</td>
                <td style="padding:16px; color:#111827; font-weight:500;"><span style="color:#ef4444; font-weight:bold; margin-right:4px;">[필독]</span> CellbigCMS 시스템 v1.2 업데이트 안내</td>
                <td style="padding:16px; text-align:center; color:#4b5563;">Admin</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">2026-03-31</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">142</td>
              </tr>
              <tr style="border-bottom:1px solid #e5e7eb; cursor:pointer;" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background=''" onclick="openNoticeViewModal(2)">
                <td style="padding:16px; text-align:center; color:#6b7280;">2</td>
                <td style="padding:16px; color:#111827; font-weight:500;">신규 단말기(Device) 펌웨어 적용 일정</td>
                <td style="padding:16px; text-align:center; color:#4b5563;">System</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">2026-03-25</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">89</td>
              </tr>
              <tr style="border-bottom:1px solid #e5e7eb; cursor:pointer;" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background=''" onclick="openNoticeViewModal(1)">
                <td style="padding:16px; text-align:center; color:#6b7280;">1</td>
                <td style="padding:16px; color:#111827; font-weight:500;">CellbigCMS 관리자 가이드 라인 배포</td>
                <td style="padding:16px; text-align:center; color:#4b5563;">Admin</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">2026-03-01</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">412</td>
              </tr>
            </tbody>
          </table>
        </div>

      </div>
    </main>

    <!-- Modal for Notice Create -->
    <div id="noticeModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999; justify-content: center; align-items: center;">
      <div style="background: #fff; width: 600px; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display:flex; flex-direction:column; max-height: 90vh;">
        <div style="padding: 16px 24px; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center;">
          <h3 style="margin: 0; font-size: 1.125rem; font-weight: 600; color: #111827;">새 공지사항 등록</h3>
          <button type="button" onclick="closeNoticeModal()" style="background: none; border: none; font-size: 1.25rem; cursor: pointer; color: #6b7280;">&times;</button>
        </div>
        <div style="padding: 24px; overflow-y:auto; flex:1;">
          <div style="margin-bottom:16px;">
            <label style="display:block; margin-bottom:8px; font-weight:500; font-size:14px;">제목 <span style="color:#ef4444">*</span></label>
            <input type="text" style="width:100%; padding:8px 12px; border:1px solid #d1d5db; border-radius:6px; box-sizing:border-box;" placeholder="공지사항 제목을 입력하세요.">
          </div>
          <div style="margin-bottom:16px; display:flex; align-items:center; gap:8px;">
            <input type="checkbox" id="isCritical" style="cursor:pointer;">
            <label for="isCritical" style="font-size:14px; cursor:pointer;">[필독] 중요 공지로 설정</label>
          </div>
          <div>
            <label style="display:block; margin-bottom:8px; font-weight:500; font-size:14px;">내용 <span style="color:#ef4444">*</span></label>
            <textarea style="width:100%; padding:12px; border:1px solid #d1d5db; border-radius:6px; min-height:200px; resize:vertical; box-sizing:border-box; font-family:inherit;" placeholder="공지 내용을 입력하세요."></textarea>
          </div>
        </div>
        <div style="padding: 16px 24px; border-top: 1px solid #e5e7eb; display: flex; justify-content: flex-end; gap: 8px; background: #f9fafb;">
          <button type="button" class="btn btn-secondary" onclick="closeNoticeModal()" style="padding:8px 16px; border:1px solid #d1d5db; border-radius:6px; background:#fff; cursor:pointer;">취소</button>
          <button type="button" class="btn btn-primary" onclick="closeNoticeModal()" style="padding:8px 16px; border:none; background:#2563eb; color:white; border-radius:6px; cursor:pointer;">등록</button>
        </div>
      </div>
    </div>

    <!-- Modal for Notice View -->
    <div id="noticeViewModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999; justify-content: center; align-items: center;">
      <div style="background: #fff; width: 600px; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display:flex; flex-direction:column; max-height: 90vh;">
        <div style="padding: 24px 24px 16px; border-bottom: 1px solid #e5e7eb;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start;">
            <h3 style="margin: 0 0 12px 0; font-size: 1.25rem; font-weight: 600; color: #111827; line-height:1.4;">CellbigCMS 시스템 v1.2 업데이트 안내</h3>
            <button type="button" onclick="closeNoticeViewModal()" style="background: none; border: none; font-size: 1.25rem; cursor: pointer; color: #6b7280; padding:0; margin-top:-4px;">&times;</button>
          </div>
          <div style="display:flex; gap:16px; font-size:13px; color:#6b7280;">
            <span>작성자: Admin</span>
            <span>등록일: 2026-03-31</span>
            <span>조회수: 142</span>
          </div>
        </div>
        <div style="padding: 24px; overflow-y:auto; flex:1; font-size:14px; color:#374151; line-height:1.6;">
          <p>안녕하세요. 관리자입니다.</p>
          <p>이번 v1.2 업데이트를 통해 CMS 시스템 내 다음과 같은 기능이 개선되었습니다.</p>
          <ul style="padding-left:20px; line-height:1.8; margin-top:16px;">
            <li>콘텐츠 상태 관리 로직 일원화 (버전 자동 인식 반영)</li>
            <li>대시보드 사이드바에 실시간 서버 상태 표기 추가</li>
            <li>필요 없는 Bulk Action 기능 제거 및 UI 개선</li>
          </ul>
          <p style="margin-top:20px;">감사합니다.</p>
        </div>
        <div style="padding: 16px 24px; border-top: 1px solid #e5e7eb; display: flex; justify-content: flex-end; gap: 8px; background: #f9fafb;">
          <button type="button" class="btn btn-secondary" onclick="closeNoticeViewModal()" style="padding:8px 16px; border:1px solid #d1d5db; border-radius:6px; background:#fff; cursor:pointer;">닫기</button>
        </div>
      </div>
    </div>

    <script>
      function openNoticeModal() {
        document.getElementById('noticeModal').style.display = 'flex';
      }
      function closeNoticeModal() {
        document.getElementById('noticeModal').style.display = 'none';
      }
      function openNoticeViewModal(id) {
        document.getElementById('noticeViewModal').style.display = 'flex';
      }
      function closeNoticeViewModal() {
        document.getElementById('noticeViewModal').style.display = 'none';
      }

      document.querySelectorAll('.sidebar-item').forEach(item => {
        item.addEventListener('click', () => {
          if(item.dataset.page) { window.location.href = item.dataset.page; }
        });
      });
    </script>
  </body>
</html>
"""

# Now replace the <main class="main-content"> ... </html> part
new_html = re.sub(r'<main class="main-content">.*</html>', new_main_content, html, flags=re.DOTALL)

with open('CMS-webpage/wireframe_site/notice-list.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Created notice-list.html based on sidebar logic.")
