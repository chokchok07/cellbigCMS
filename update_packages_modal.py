import re

with open('CMS-webpage/wireframe_site/device-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Remove Product
text = re.sub(r'<div class="info-label"[^>]*>Product:</div>.*?</datalist>\s*</div>', '', text, flags=re.DOTALL)
# Remove Package
text = re.sub(r'<div class="info-label"[^>]*>Package:</div>.*?</datalist>\s*</div>', '', text, flags=re.DOTALL)

# Update Installed Packages header
old_header_re = r'<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px">\s*<h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px; width: 100%;">📦 설치된 패키지</h2>\s*</div>'
new_header = '''<div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px;">
                <h2 style="font-size: 18px; color: #111827; margin: 0;">📦 설치된 패키지</h2>
                <button class="btn btn-primary" style="padding: 6px 12px; font-size: 14px;" onclick="showAddPackageModal()">+ 패키지 추가</button>
              </div>'''
text = re.sub(old_header_re, new_header, text)

# Add Delete to Active
old_active = r'<div style="font-weight: 600; color: #065f46; font-size: 14px;">📦 pkg-v1.1 \(Active\)</div>\s*</div>'
new_active = '''<div style="font-weight: 600; color: #065f46; font-size: 14px;">📦 pkg-v1.1 (Active)</div>
                  <button class="btn btn-outline" style="border-color:#ef4444; color:#ef4444; padding: 2px 8px; font-size: 12px;" onclick="if(confirm(\'이 패키지를 디바이스에서 삭제하시겠습니까?\')) { alert(\'삭제되었습니다.\'); }">삭제</button>
                </div>'''
text = re.sub(old_active, new_active, text)

# Add Delete to Backup
old_backup = r'<div style="font-weight: 600; color: #4b5563; font-size: 14px;">📦 pkg-v1.0 \(Backup\)</div>\s*</div>'
new_backup = '''<div style="font-weight: 600; color: #4b5563; font-size: 14px;">📦 pkg-v1.0 (Backup)</div>
                  <button class="btn btn-outline" style="border-color:#ef4444; color:#ef4444; padding: 2px 8px; font-size: 12px;" onclick="if(confirm(\'이 패키지를 디바이스에서 삭제하시겠습니까?\')) { alert(\'삭제되었습니다.\'); }">삭제</button>
                </div>'''
text = re.sub(old_backup, new_backup, text)

# Add Modal
if 'addPackageModal' not in text:
    modal_html = """
  <!-- Add Package Modal -->
  <div class="modal-overlay" id="addPackageModal" style="display:none; position:fixed; top:0; left:0; right:0; bottom:0; background:rgba(0,0,0,0.5); align-items:center; justify-content:center; z-index:9999;">
    <div class="modal-content" style="background:#fff; padding:24px; border-radius:8px; max-width:500px; width:100%;">
      <div class="modal-header" style="margin-bottom: 20px; display:flex; justify-content:space-between; align-items:center;">
        <h2 style="font-size: 18px; margin: 0;">패키지 추가</h2>
        <button class="close-btn" style="background:none; border:none; font-size:20px; cursor:pointer;" onclick="hideAddPackageModal()">&times;</button>
      </div>
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <div>
          <label class="info-label" style="margin-bottom: 4px; display: block; font-weight:600; color:#4b5563;">1. Product 선택</label>
          <input type="text" list="modalProductList" class="input" style="width: 100%; border:1px solid #e5e7eb; padding:8px; border-radius:4px;" placeholder="Product 검색/선택">
          <datalist id="modalProductList">
            <option value="Product A">Product A</option>
            <option value="Product B">Product B</option>
            <option value="Product C">Product C</option>
          </datalist>
        </div>
        <div>
          <label class="info-label" style="margin-bottom: 4px; display: block; font-weight:600; color:#4b5563;">2. Package 선택</label>
          <input type="text" list="modalPackageList" class="input" style="width: 100%; border:1px solid #e5e7eb; padding:8px; border-radius:4px;" placeholder="Package 검색/선택">
          <datalist id="modalPackageList">
            <option value="Package v1.0">Package v1.0</option>
            <option value="Package v2.0">Package v2.0</option>
            <option value="Package v3.1">Package v3.1</option>
          </datalist>
        </div>
      </div>
      <div class="modal-actions" style="margin-top: 24px; display: flex; justify-content: flex-end; gap: 8px;">
        <button class="btn btn-outline" onclick="hideAddPackageModal()">취소</button>
        <button class="btn btn-primary" onclick="addPackage()">추가</button>
      </div>
    </div>
  </div>

  <script>
    function showAddPackageModal() {
      document.getElementById('addPackageModal').style.display = 'flex';
    }
    function hideAddPackageModal() {
      document.getElementById('addPackageModal').style.display = 'none';
    }
    function addPackage() {
      alert('패키지가 디바이스에 추가되었습니다.');
      hideAddPackageModal();
    }
  </script>
</body>"""
    text = text.replace('</body>', modal_html)

with open('CMS-webpage/wireframe_site/device-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("SUCCESS")
