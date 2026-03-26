const fs = require('fs');
const path = require('path');
const dir = 'CMS-webpage/wireframe_site';

const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));
let count = 0;

for (const file of files) {
  const fp = path.join(dir, file);
  let content = fs.readFileSync(fp, 'utf8');
  let changed = false;

  // 1. Replace the old "Inactive" button logic in header-actions
  // We'll replace it with BOTH Active and Inactive buttons, or maybe just support dynamic. 
  // Let's replace the single Inactive button with the dual buttons:
  const btnRegex = /<button type="button" class="btn btn-danger" onclick="openInactiveModal\(\)">Inactive<\/button>/g;
  if (btnRegex.test(content)) {
    content = content.replace(btnRegex, `<button type="button" class="btn btn-success" onclick="openStatusModal('active')" style="background:#10b981; border-color:#10b981; color:#fff;">Active</button>\n              <button type="button" class="btn btn-danger" onclick="openStatusModal('inactive')" style="background:#ef4444; border-color:#ef4444; color:#fff;">Inactive</button>`);
    changed = true;
  }

  // 2. Replace the modal HTML
  const modalRegex = /<div [^>]*id="inactiveConfirmModal"[\s\S]*?<\/script>/;
  if (modalRegex.test(content)) {
    content = content.replace(modalRegex, `<div id="statusConfirmModal" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999; justify-content: center; align-items: center;">
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
        });
      });
    </script>`);
    changed = true;
  }
  
  if(changed) {
    fs.writeFileSync(fp, content, 'utf8');
    count++;
  }
}
console.log('Updated ' + count + ' files.');