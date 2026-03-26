import re

with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace("onclick=\"location.href='content-detail.html'\"", "onclick=\"openContentViewModal(this)\"")
html = html.replace('<button class="action-btn">View</button>', '<button class="action-btn" onclick="openContentViewModal(this)">View</button>')

modal_html = """
    <!-- Content Detail View Modal -->
    <div id="contentViewModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:10000; align-items:center; justify-content:center; padding:20px;">
      <div style="background:white; border-radius:8px; width:100%; max-width:450px; padding:24px; box-shadow:0 4px 6px rgba(0,0,0,0.1);">
        <div style="display:flex; justify-content:space-between; align-items:center; border-bottom:1px solid #e5e7eb; padding-bottom:12px; margin-bottom:16px;">
          <h2 style="margin:0; font-size:18px; color:#111827;">🎬 Content Registration Info</h2>
          <button type="button" style="background:transparent; border:none; font-size:24px; cursor:pointer; color:#6b7280;" onclick="closeContentViewModal()">&times;</button>
        </div>
        
        <div style="display:flex; gap:16px; margin-bottom:16px;">
          <div style="width:80px; height:80px; background:#f3f4f6; border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:32px;">🏖️</div>
          <div style="flex:1;">
            <h3 id="cvModalTitle" style="margin:0 0 4px 0; font-size:16px; color:#111827;">SandCraft - Beach</h3>
            <p style="margin:0 0 2px 0; font-size:13px; color:#6b7280;">ID: <span style="color:#111827; font-weight:500;">sandcraft-beach</span></p>
            <p style="margin:0 0 2px 0; font-size:13px; color:#6b7280;">Type: <span style="color:#111827;">single</span></p>
            <p style="margin:0; font-size:13px; color:#6b7280;">Version: <span style="color:#2563eb; font-weight:500;">v2.1</span></p>
          </div>
        </div>
        
        <div style="background:#f9fafb; padding:12px; border-radius:6px; margin-bottom:16px;">
          <p style="margin:0 0 8px 0; font-size:12px; font-weight:600; color:#4b5563; text-transform:uppercase;">DESCRIPTION</p>
          <p style="margin:0; font-size:13px; color:#374151; line-height:1.5;">해변을 테마로 한 모래놀이 콘텐츠. 다양한 해양 생물과 상호작용이 가능합니다.</p>
        </div>
        
        <div style="display:flex; justify-content:flex-end; gap:8px; border-top:1px solid #e5e7eb; padding-top:16px;">
          <button type="button" class="btn btn-secondary" onclick="closeContentViewModal()">닫기</button>
          <button type="button" class="btn btn-primary" onclick="location.href='content-detail.html'">상세 페이지로 이동</button>
        </div>
      </div>
    </div>
    
    <script>
    function openContentViewModal(btn) {
      if(btn) {
          let row = btn.closest('tr');
          if(row) {
              let titleEl = row.querySelector('.content-title');
              if(titleEl) {
                  document.getElementById('cvModalTitle').innerText = titleEl.innerText;
              }
          }
      }
      document.getElementById('contentViewModal').style.display = 'flex';
    }
    
    function closeContentViewModal() {
      document.getElementById('contentViewModal').style.display = 'none';
    }
    </script>
"""

if 'contentViewModal' not in html:
    html = html.replace('</body>', modal_html + '\n</body>')
    with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('SUCCESS')
