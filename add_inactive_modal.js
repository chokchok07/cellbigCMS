const fs = require('fs');
const path = require('path');

const dir = 'CMS-webpage/wireframe_site';
const files = fs.readdirSync(dir).filter(f => f.endsWith('.html'));

const modalHTML = `
  <!-- Inactive Confirm Modal -->
  <div id="inactiveConfirmModal" class="modal-overlay" style="display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999; align-items: center; justify-content: center;">
    <div style="background: #fff; width: 400px; border-radius: 8px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); display: flex; flex-direction: column; overflow: hidden;">
      <div style="padding: 16px 24px; border-bottom: 1px solid #e5e7eb; background: #f9fafb;">
        <h2 style="margin: 0; font-size: 16px; color: #1f2937;">비활성화 확인</h2>
      </div>
      <div style="padding: 24px; color: #374151; font-size: 14px; text-align: center;">
        정말로 비활성화 하시겠습니까?
      </div>
      <div style="padding: 16px 24px; border-top: 1px solid #e5e7eb; display: flex; justify-content: flex-end; gap: 8px; background: #f9fafb;">
        <button type="button" class="btn btn-secondary" onclick="closeInactiveModal()">취소</button>
        <button type="button" class="btn btn-primary" style="background:#ef4444; border-color:#ef4444; color:#fff;" onclick="confirmInactive()">비활성화</button>
      </div>
    </div>
  </div>
  <script>
    function openInactiveModal(e) {
      if(e && e.preventDefault) e.preventDefault();
      document.getElementById('inactiveConfirmModal').style.display = 'flex';
    }
    function closeInactiveModal() {
      document.getElementById('inactiveConfirmModal').style.display = 'none';
    }
    function confirmInactive() {
      alert('비활성화 되었습니다.');
      closeInactiveModal();
    }
    // Handle toggleStatus if used in lists
    function toggleStatus(id) {
      openInactiveModal();
    }
    
    // Auto-bind to any generic Inactive buttons if they don't have onclick
    document.addEventListener('DOMContentLoaded', () => {
      document.querySelectorAll('.btn-danger').forEach(btn => {
        if(btn.innerText.includes('Inactive') && !btn.hasAttribute('onclick')) {
          btn.addEventListener('click', openInactiveModal);
        }
      });
    });
  </script>
`;

let updatedCount = 0;
for (const file of files) {
  const fp = path.join(dir, file);
  let content = fs.readFileSync(fp, 'utf8');
  let changed = false;

  // Add global modal
  if (!content.includes('inactiveConfirmModal')) {
    content = content.replace('</body>', `${modalHTML}\n</body>`);
    changed = true;
  }

  // Add "Inactive" button to Edit pages
  // Only for editor pages
  if (file.includes('-editor.html') || file.includes('-edit.html')) {
    if (content.includes('class="header-actions"') && !content.includes('openInactiveModal()') && !content.includes('Inactive (비활성화)')) {
      content = content.replace(
        /(<button[^>]*>Cancel<\/button>)/i,
        `<button type="button" class="btn btn-danger" style="background:#ef4444; border-color:#ef4444; color:#fff; margin-right:8px;" onclick="openInactiveModal()">Inactive</button>\n            $1`
      );
      changed = true;
    }
  }

  if (changed) {
    fs.writeFileSync(fp, content, 'utf8');
    updatedCount++;
  }
}
console.log("Updated", updatedCount, "files.");
