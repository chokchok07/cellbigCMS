import io

with open('CMS-webpage/wireframe_site/settings.html', 'r', encoding='utf-8') as f:
    text = f.read()

idx = text.rfind('</body>')

modal_code = """
      <!-- Account Approval Modal -->
      <div id=\"approvalModal\" style=\"display: none; position: fixed; top: 0; left: 0; width: 100%; height: 100%; background: rgba(0,0,0,0.5); z-index: 9999; justify-content: center; align-items: center;\">
        <div style=\"background: #fff; width: 450px; border-radius: 8px; overflow: hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);\">
          <div style=\"padding: 16px 24px; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center;\">
            <h3 style=\"margin: 0; font-size: 1.125rem; font-weight: 600; color: #111827;\">계정 가입 승인</h3>
            <button type=\"button\" onclick=\"closeApprovalModal()\" style=\"background: none; border: none; font-size: 1.25rem; cursor: pointer; color: #6b7280;\">&times;</button>
          </div>
          <div style=\"padding: 24px;\">
            <div style=\"margin-bottom: 16px; background: #f9fafb; padding: 12px; border-radius: 6px; border: 1px solid #e5e7eb;\">
              <div style=\"margin-bottom: 8px; font-size: 0.9rem; color: #6b7280;\">이름/소속</div>
              <div style=\"font-weight: 600; color: #111827;\" id=\"approvalModal_name_company\"></div>
              <div style=\"margin-top: 8px; font-size: 0.9rem; color: #6b7280;\">아이디</div>
              <div style=\"font-weight: 600; color: #111827;\"><input type=\"text\" id=\"approvalModal_id\" readonly style=\"border:none;background:transparent;font-weight:bold;color:#111827;width:100%;padding:0;\"></div>
            </div>
            
            <div class=\"form-group\" style=\"margin-bottom: 16px;\">
              <label style=\"display: block; font-weight: 600; margin-bottom: 8px; color: #374151;\">계정 권한(Role) 배정</label>
              <select id=\"approvalModal_role\" class=\"input\" style=\"width: 100%;\" onchange=\"toggleRegionSelect()\">
                <option value=\"OperationAdmin\">운영 관리자 (Operation Admin)</option>
                <option value=\"LocalAdmin\">지역 관리자 (Regional Admin)</option>
                <option value=\"SuperAdmin\">최고 관리자 (Super Admin)</option>
                <option value=\"Technician\">설치/유지보수 기사 (Technician)</option>
              </select>
            </div>

            <div class=\"form-group\" id=\"approvalModal_regionGroup\" style=\"margin-bottom: 16px; display: none;\">
              <label style=\"display: block; font-weight: 600; margin-bottom: 8px; color: #374151;\">관리 지역(Region) 할당</label>
              <select id=\"approvalModal_region\" class=\"input\" style=\"width: 100%;\">
                <option value=\"\">-- 지역을 선택하세요 --</option>
                <option value=\"Seoul\">서울광역시</option>
                <option value=\"Gyeonggi\">경기도</option>
                <option value=\"Busan\">부산광역시</option>
                <option value=\"Jeju\">제주/기타</option>
              </select>
              <p style=\"font-size: 0.8rem; color: #6b7280; margin-top: 4px;\">※ 지역 관리자에게는 선택한 지역의 장비 및 콘텐츠 실적만 표시됩니다.</p>
            </div>

          </div>
          <div style=\"padding: 16px 24px; background: #f9fafb; border-top: 1px solid #e5e7eb; display: flex; justify-content: flex-end; gap: 12px;\">
            <button type=\"button\" class=\"btn btn-secondary\" onclick=\"closeApprovalModal()\">취소</button>
            <button type=\"button\" class=\"btn btn-primary\" onclick=\"confirmApproval()\">승인 및 권한 부여</button>
          </div>
        </div>
      </div>

<script>
        // Account Approval Modal Logic
        function openApprovalModal(id, name, company) {
          document.getElementById('approvalModal_id').value = id;
          document.getElementById('approvalModal_name_company').innerText = name + \" / \" + company;
          document.getElementById('approvalModal').style.display = 'flex';
          toggleRegionSelect();
        }

        function closeApprovalModal() {
          document.getElementById('approvalModal').style.display = 'none';
        }

        function toggleRegionSelect() {
          const roleSelect = document.getElementById('approvalModal_role');
          const regionGroup = document.getElementById('approvalModal_regionGroup');
          if (roleSelect.value === 'LocalAdmin') {
            regionGroup.style.display = 'block';
          } else {
            regionGroup.style.display = 'none';
          }
        }

        function confirmApproval() {
          var roleSel = document.getElementById('approvalModal_role');
          var role = roleSel.options[roleSel.selectedIndex].text;
          var isLocal = roleSel.value === 'LocalAdmin';
          var region = isLocal ? document.getElementById('approvalModal_region').value : '';
          
          var msg = "계정이 [" + role + "] 권한으로 승인되었습니다.";
          if (isLocal) {
            msg += "\\n할당된 지역: " + (region ? region : '지정되지 않음');
          }
          
          alert(msg);
          closeApprovalModal();
        }
</script>
"""

# Check if modal is already present
if 'id="approvalModal"' not in text:
    new_text = text[:idx] + modal_code + text[idx:]
    with open('CMS-webpage/wireframe_site/settings.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Modal successfully injected!")
else:
    print("Modal already exists!")
