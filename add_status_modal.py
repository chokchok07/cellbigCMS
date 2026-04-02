import re

with open("CMS-webpage/wireframe_site/content-versions.html", "r", encoding="utf-8") as f:
    text = f.read()

modal = """
<!-- Version Status Modal -->
<div id="versionStatusModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; justify-content:center; align-items:center;">
  <div style="background:#fff; width:400px; border-radius:8px; overflow:hidden; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
    <div style="padding:16px 24px; border-bottom:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center;">
      <h3 style="margin:0; font-size:18px; font-weight:600; color:#111827;">버전 상태 변경 (Change Status)</h3>
      <button type="button" onclick="closeVersionStatusModal()" style="background:none; border:none; font-size:24px; cursor:pointer; color:#6b7280;">&times;</button>
    </div>
    <div style="padding:24px; display:flex; flex-direction:column; gap:16px;">
      <p style="margin:0; color:#374151; font-size:14px; font-weight:500;">변경할 상태를 선택하세요:</p>
      
      <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
        <input type="radio" name="versionActionStatus" value="published" style="width:16px; height:16px;" checked />
        <span style="font-size:14px; font-weight:600; color:#1d4ed8;">Published (발행)</span>
      </label>
      
      <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
        <input type="radio" name="versionActionStatus" value="test" style="width:16px; height:16px;" />
        <span style="font-size:14px; font-weight:600; color:#047857;">Test (테스트)</span>
      </label>
      
      <label style="display:flex; align-items:center; gap:8px; cursor:pointer;">
        <input type="radio" name="versionActionStatus" value="unpublished" style="width:16px; height:16px;" />
        <span style="font-size:14px; font-weight:600; color:#4b5563;">Unpublished / Draft (초안)</span>
      </label>
    </div>
    <div style="padding:16px 24px; border-top:1px solid #e5e7eb; display:flex; justify-content:flex-end; gap:8px; background:#f9fafb;">
      <button type="button" class="btn btn-secondary" onclick="closeVersionStatusModal()">취소</button>
      <button type="button" class="btn btn-primary" onclick="confirmVersionStatus()">적용</button>
    </div>
  </div>
</div>

<script>
function openVersionStatusModal() {
    document.getElementById('versionStatusModal').style.display = 'flex';
}
function closeVersionStatusModal() {
    document.getElementById('versionStatusModal').style.display = 'none';
}
function confirmVersionStatus() {
    let selected = document.querySelector('input[name="versionActionStatus"]:checked');
    if (selected) {
        alert('상태가 [' + selected.value + '] (으)로 변경되었습니다.');
    }
    closeVersionStatusModal();
}
</script>
"""

# Replace all openStatusModal() with openVersionStatusModal()
text = text.replace('openStatusModal()', 'openVersionStatusModal()')

if 'id="versionStatusModal"' not in text:
    text = text.replace('</body>', modal + '\n</body>')

with open("CMS-webpage/wireframe_site/content-versions.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Status modal generated and applied!")
