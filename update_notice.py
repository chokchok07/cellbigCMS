import re

new_content = """    <main class="main-content">
      <div class="container">
        
        <div class="breadcrumb" style="font-size: 13px; color: #6b7280; margin-bottom: 20px; display:flex; gap:8px; align-items:center;">
          <span style="cursor:pointer; padding: 4px 8px; border-radius: 4px; transition: background 0.2s;" onmouseover="this.style.background='#e5e7eb'" onmouseout="this.style.background='transparent'" onclick="location.href='index.html'">🏠 Home</span>
          <span style="color: #d1d5db;">/</span>
          <span style="color: #374151; font-weight: 600; padding: 4px 8px;">📢 Notice</span>
        </div>

        <div class="page-header" style="display:flex; justify-content:space-between; align-items:flex-end; margin-bottom: 24px;">
          <div>
            <h1 class="page-title" style="margin:0; font-size:24px; color:#111827;">📢 공지사항</h1>
            <p class="page-desc" style="margin:8px 0 0 0; color:#6b7280;">시스템 업데이트 및 콘텐츠 관련 중요 안내 사항을 공유합니다.</p>
          </div>
          <div class="header-actions">
            <button type="button" class="btn btn-primary" onclick="openNoticeModal()" style="padding:8px 16px; background-color:#2563eb; color:white; border:none; border-radius:6px; font-weight:500; cursor:pointer;">+ 공지 등록</button>
          </div>
        </div>

        <!-- Filter & Search -->
        <div style="display:flex; justify-content:space-between; margin-bottom: 16px; align-items:center;">
          <div style="display:flex; gap:12px;">
            <select style="padding:8px 12px; border:1px solid #d1d5db; border-radius:6px; font-size:14px; outline:none; background:#fff; min-width:140px; cursor:pointer;">
              <option value="all">전체 분류</option>
              <option value="system">🖥️ 시스템 공지</option>
              <option value="content">📦 콘텐츠 공지</option>
            </select>
            <input type="text" placeholder="제목 또는 내용 검색" style="padding:8px 12px; border:1px solid #d1d5db; border-radius:6px; width:240px; font-size:14px; outline:none;">
          </div>
          <div>
             <span style="font-size:13px; color:#6b7280;">총 <strong>3</strong>건</span>
          </div>
        </div>

        <!-- Data Table -->
        <div class="card" style="background:#fff; border-radius:8px; box-shadow:0 1px 3px rgba(0,0,0,0.1); overflow:hidden;">
          <table class="data-table" style="width:100%; border-collapse:collapse; text-align:left;">
            <thead>
              <tr style="background:#f9fafb; border-bottom:1px solid #e5e7eb;">
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb; width:80px; text-align:center;">번호</th>
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb; width:120px; text-align:center;">분류</th>
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb;">제목</th>
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb; width:80px; text-align:center;">첨부</th>
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb; width:120px; text-align:center;">작성자</th>
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb; width:120px; text-align:center;">등록일</th>
                <th style="padding:12px 16px; font-weight:600; color:#4b5563; border-bottom:1px solid #e5e7eb; width:80px; text-align:center;">조회수</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #e5e7eb; cursor:pointer;" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background=''" onclick="openNoticeViewModal(3)">
                <td style="padding:16px; text-align:center; color:#6b7280;">3</td>
                <td style="padding:16px; text-align:center;"><span style="padding:4px 8px; background:#eff6ff; color:#2563eb; border-radius:4px; font-size:12px; font-weight:600;">시스템 공지</span></td>
                <td style="padding:16px; color:#111827; font-weight:500;"><span style="color:#ef4444; font-weight:bold; margin-right:4px;">[필독]</span> CellbigCMS 시스템 v1.2 업데이트 안내</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">📎 1</td>
                <td style="padding:16px; text-align:center; color:#4b5563;">Admin</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">2026-03-31</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">142</td>
              </tr>
              <tr style="border-bottom:1px solid #e5e7eb; cursor:pointer;" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background=''" onclick="openNoticeViewModal(2)">
                <td style="padding:16px; text-align:center; color:#6b7280;">2</td>
                <td style="padding:16px; text-align:center;"><span style="padding:4px 8px; background:#f0fdf4; color:#16a34a; border-radius:4px; font-size:12px; font-weight:600;">콘텐츠 공지</span></td>
                <td style="padding:16px; color:#111827; font-weight:500;">[신규] 봄맞이 테마 SandCraft 콘텐츠 일괄 배포</td>
                <td style="padding:16px; text-align:center; color:#d1d5db;">-</td>
                <td style="padding:16px; text-align:center; color:#4b5563;">Content_Team</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">2026-03-28</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">89</td>
              </tr>
              <tr style="border-bottom:1px solid #e5e7eb; cursor:pointer;" onmouseover="this.style.background='#f3f4f6'" onmouseout="this.style.background=''" onclick="openNoticeViewModal(1)">
                <td style="padding:16px; text-align:center; color:#6b7280;">1</td>
                <td style="padding:16px; text-align:center;"><span style="padding:4px 8px; background:#eff6ff; color:#2563eb; border-radius:4px; font-size:12px; font-weight:600;">시스템 공지</span></td>
                <td style="padding:16px; color:#111827; font-weight:500;">디바이스 펌웨어 다운로드 최적화 패치 현황</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">📎 2</td>
                <td style="padding:16px; text-align:center; color:#4b5563;">Dev_Team</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">2026-03-25</td>
                <td style="padding:16px; text-align:center; color:#6b7280;">210</td>
              </tr>
            </tbody>
          </table>
        </div>

      </div>
    </main>

    <!-- Modal for Notice Create / Edit -->
    <div id="noticeModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999; justify-content: center; align-items: center;">
      <div style="background: #fff; width: 680px; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display:flex; flex-direction:column; max-height: 90vh;">
        <div style="padding: 16px 24px; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center;">
          <h3 style="margin: 0; font-size: 1.125rem; font-weight: 600; color: #111827;">새 공지사항 등록 / 수정</h3>
          <button type="button" onclick="closeNoticeModal()" style="background: none; border: none; font-size: 1.25rem; cursor: pointer; color: #6b7280;">&times;</button>
        </div>
        <div style="padding: 24px; overflow-y:auto; flex:1;">
          
          <div style="display:flex; gap:16px; margin-bottom:16px;">
            <div style="flex: 1;">
              <label style="display:block; margin-bottom:8px; font-weight:500; font-size:14px;">분류 <span style="color:#ef4444">*</span></label>
              <select style="width:100%; padding:8px 12px; border:1px solid #d1d5db; border-radius:6px; box-sizing:border-box;">
                <option value="system">🖥️ 시스템 공지</option>
                <option value="content">📦 콘텐츠 공지</option>
              </select>
            </div>
            <div style="flex: 2; display:flex; align-items:flex-end;">
              <div style="display:flex; align-items:center; gap:8px; padding-bottom: 10px;">
                <input type="checkbox" id="isCritical" style="cursor:pointer; width:16px; height:16px;">
                <label for="isCritical" style="font-size:14px; cursor:pointer; font-weight:500; color:#ef4444;">[필독] 중요 공지로 상단 고정</label>
              </div>
            </div>
          </div>

          <div style="margin-bottom:16px;">
            <label style="display:block; margin-bottom:8px; font-weight:500; font-size:14px;">제목 <span style="color:#ef4444">*</span></label>
            <input type="text" style="width:100%; padding:8px 12px; border:1px solid #d1d5db; border-radius:6px; box-sizing:border-box;" placeholder="공지사항 제목을 입력하세요.">
          </div>
          
          <div style="margin-bottom:16px;">
            <label style="display:block; margin-bottom:8px; font-weight:500; font-size:14px;">내용 <span style="color:#ef4444">*</span></label>
            <textarea style="width:100%; padding:12px; border:1px solid #d1d5db; border-radius:6px; min-height:220px; resize:vertical; box-sizing:border-box; font-family:inherit;" placeholder="마크다운 또는 에디터를 이용한 상세 내용을 입력하세요."></textarea>
          </div>

          <!-- Attachment Area -->
          <div>
            <label style="display:block; margin-bottom:8px; font-weight:500; font-size:14px;">첨부파일</label>
            <div style="border:1px dashed #d1d5db; padding:20px; border-radius:6px; text-align:center; background:#f9fafb; margin-bottom:8px;">
              <span style="color:#6b7280; font-size:13px;">클릭하거나 파일을 여기로 드래그하세요. (최대 50MB)</span>
              <input type="file" multiple style="display:block; margin: 12px auto 0 auto; font-size:13px; color:#4b5563;">
            </div>
          </div>

        </div>
        <div style="padding: 16px 24px; border-top: 1px solid #e5e7eb; display: flex; justify-content: flex-end; gap: 8px; background: #f9fafb;">
          <button type="button" class="btn btn-secondary" onclick="closeNoticeModal()" style="padding:8px 16px; border:1px solid #d1d5db; border-radius:6px; background:#fff; cursor:pointer;">취소</button>
          <button type="button" class="btn btn-primary" onclick="closeNoticeModal()" style="padding:8px 16px; border:none; background:#2563eb; color:white; border-radius:6px; cursor:pointer;">저장</button>
        </div>
      </div>
    </div>

    <!-- Modal for Notice View -->
    <div id="noticeViewModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999; justify-content: center; align-items: center;">
      <div style="background: #fff; width: 700px; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1); display:flex; flex-direction:column; max-height: 90vh;">
        
        <!-- View Header -->
        <div style="padding: 24px 24px 16px; border-bottom: 1px solid #e5e7eb;">
          <div style="display:flex; justify-content:space-between; align-items:flex-start; margin-bottom:12px;">
            <div style="display:flex; gap:8px; align-items:center;">
              <span style="padding:4px 8px; background:#eff6ff; color:#2563eb; border-radius:4px; font-size:12px; font-weight:600;">시스템 공지</span>
              <h3 style="margin: 0; font-size: 1.25rem; font-weight: 600; color: #111827; line-height:1.4;"><span style="color:#ef4444; font-weight:bold; margin-right:4px;">[필독]</span> CellbigCMS 시스템 v1.2 업데이트 안내</h3>
            </div>
            <button type="button" onclick="closeNoticeViewModal()" style="background: none; border: none; font-size: 1.25rem; cursor: pointer; color: #6b7280; padding:0; margin-top:-4px;">&times;</button>
          </div>
          <div style="display:flex; gap:16px; font-size:13px; color:#6b7280;">
            <span><strong style="color:#4b5563;">작성자:</strong> Admin</span>
            <span><strong style="color:#4b5563;">등록일:</strong> 2026-03-31 10:24</span>
            <span><strong style="color:#4b5563;">조회수:</strong> 142</span>
          </div>
        </div>

        <!-- View Body -->
        <div style="padding: 24px; overflow-y:auto; flex:1; font-size:14px; color:#374151; line-height:1.6;">
          <p>안녕하세요. CellbigCMS 관리자입니다.</p>
          <p>이번 v1.2 업데이트를 통해 다음과 같은 기능이 개선되었습니다. 운영 및 서비스 관리 업무에 참고 부탁드립니다.</p>
          <ul style="padding-left:20px; line-height:1.8; margin-top:16px; background:#f9fafb; padding-top:12px; padding-bottom:12px; border-radius:6px; border:1px solid #f3f4f6;">
            <li><strong>상태 관리 일원화:</strong> 콘텐츠 상태 로직이 자동 인식 기반으로 고도화되었습니다.</li>
            <li><strong>서버 헬스 체크:</strong> 대시보드 및 모든 사이드바 하단에 API 실시간 연결 상태가 추가되었습니다.</li>
            <li><strong>위험 UI 제거:</strong> 휴먼 에러 방지를 위해 대량 작업(Bulk Actions)이 안전하게 제외되었습니다.</li>
          </ul>
          <p style="margin-top:20px;">자세한 사항은 첨부파일의 메뉴얼 변경점 안내서를 확인해 주시기 바랍니다.</p>
          <p>감사합니다.</p>
        </div>

        <!-- Attachment List -->
        <div style="padding: 16px 24px; border-top: 1px solid #e5e7eb; background: #fafafa;">
          <h4 style="margin:0 0 8px 0; font-size:13px; color:#374151;">📎 첨부파일 (1)</h4>
          <div style="display:flex; gap:12px;">
            <a href="#" style="display:inline-flex; align-items:center; gap:6px; padding:6px 12px; background:#fff; border:1px solid #d1d5db; border-radius:4px; font-size:12px; color:#2563eb; text-decoration:none; cursor:pointer;" onmouseover="this.style.borderColor='#93c5fd'" onmouseout="this.style.borderColor='#d1d5db'">
               <span>v1.2_release_note_admin.pdf</span> <span style="color:#9ca3af; font-size:11px;">(1.4MB)</span>
               <svg style="width:14px; height:14px; fill:none; stroke:currentColor; viewBox:0 0 24 24" stroke-width="2"><path d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"></path></svg>
            </a>
          </div>
        </div>

        <!-- View Footer: Delete / Edit / Close -->
        <div style="padding: 16px 24px; border-top: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items:center; background: #fff;">
          <div>
             <button type="button" onclick="confirmDelete()" style="padding:8px 16px; border:1px solid #ef4444; background:#fff; color:#ef4444; border-radius:6px; cursor:pointer; font-weight:500;">삭제</button>
          </div>
          <div style="display:flex; gap:8px;">
            <button type="button" class="btn btn-secondary" onclick="openNoticeModal(); closeNoticeViewModal();" style="padding:8px 16px; border:1px solid #d1d5db; border-radius:6px; background:#fff; cursor:pointer;">수정</button>
            <button type="button" class="btn btn-primary" onclick="closeNoticeViewModal()" style="padding:8px 16px; border:none; background:#374151; color:white; border-radius:6px; cursor:pointer;">목록으로</button>
          </div>
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
      function confirmDelete() {
        if(confirm("정말 이 공지사항을 삭제하시겠습니까?")) {
          alert('삭제되었습니다.');
          closeNoticeViewModal();
        }
      }

      document.querySelectorAll('.sidebar-item').forEach(item => {
        item.addEventListener('click', () => {
          if(item.dataset.page) { window.location.href = item.dataset.page; }
        });
      });
    </script>
  </body>
</html>"""

with open('CMS-webpage/wireframe_site/notice-list.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace <main class="main-content"> ... </html> with the supercharged HTML
new_html = re.sub(r'<main class="main-content">.*</html>', new_content, text, flags=re.DOTALL)

with open('CMS-webpage/wireframe_site/notice-list.html', 'w', encoding='utf-8') as f:
    f.write(new_html)

print("Advanced Notice page logic injected!")
