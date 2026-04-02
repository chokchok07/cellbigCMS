import re
with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    text = f.read()

view_modal = """
<!-- View/Edit Version Modal -->
<div id="viewVersionModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; align-items:center; justify-content:center; padding:20px;">
  <div style="background:#fff; width:600px; max-width:100%; max-height:90vh; border-radius:8px; display:flex; flex-direction:column; overflow:hidden; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.1);">
    <!-- Modal Header -->
    <div style="padding:16px 20px; border-bottom:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; background:#f9fafb;">
      <h3 style="margin:0; font-size:18px; color:#111827;">버전 상세 및 수정 (Version Details)</h3>
      <button onclick="closeViewVersionModal()" style="background:transparent; border:none; font-size:24px; cursor:pointer; color:#6b7280;" type="button">✕</button>
    </div>
    <!-- Modal Body -->
    <div style="padding:20px; overflow-y:auto; display:flex; flex-direction:column; gap:24px;">
      <!-- 버전 -->
      <div>
        <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 (Version)</label>
        <div style="display:flex; align-items:center; gap:8px;">
          <input id="viewVersionMajor" max="999" min="0" style="width:70px; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; text-align:center;" type="number" value="2"/>
          <span style="font-weight:bold; color:#6b7280;">.</span>
          <input id="viewVersionMinor" max="999" min="0" style="width:70px; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; text-align:center;" type="number" value="1"/>
          <span style="font-weight:bold; color:#6b7280;">.</span>
          <input id="viewVersionPatch" max="999" min="0" style="width:70px; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; text-align:center;" type="number" value="0"/>
        </div>
      </div>
      <div style="display:grid; grid-template-columns: 1fr 1fr; gap:20px;">
        <!-- 업데이트 유형 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">업데이트 유형</label>
          <div style="display:flex; gap:16px;">
            <label for="viewUpdateForced" style="display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input id="viewUpdateForced" name="viewUpdateType" style="width:16px; height:16px;" type="radio" value="forced"/>
              <span style="font-size:13px;">강제 업데이트</span>
            </label>
            <label for="viewUpdateOptional" style="display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input checked="" id="viewUpdateOptional" name="viewUpdateType" style="width:16px; height:16px;" type="radio" value="optional"/>
              <span style="font-size:13px;">선택 업데이트</span>
            </label>
          </div>
        </div>
        <!-- 배포 환경 -->
        <div>
          <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">배포 환경</label>
          <div style="display:flex; gap:16px;">
            <label for="viewDeployProduction" style="display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input id="viewDeployProduction" checked="" name="viewDeploymentTarget" style="width:16px; height:16px;" type="radio" value="production"/>
              <span style="font-size:13px;">상용 (Production)</span>
            </label>
            <label for="viewDeployTest" style="display:flex; align-items:center; gap:6px; cursor:pointer;">
              <input id="viewDeployTest" name="viewDeploymentTarget" style="width:16px; height:16px;" type="radio" value="test"/>
              <span style="font-size:13px;">테스트 (Test)</span>
            </label>
          </div>
        </div>
      </div>
      <!-- 버전 파일 및 확인 -->
      <div>
        <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 파일 (Artifact File)</label>
        <div style="display:flex; gap:8px; align-items:center; margin-bottom:8px;">     
          <div id="viewVersionFileName" style="flex:1; padding:8px 12px; border:1px solid #d1d5db; border-radius:4px; background:#f9fafb; font-size:13px; color:#6b7280;">content-101-v2.1.0.zip</div>
          <input accept=".zip" id="viewVersionFile" onchange="document.getElementById('viewVersionFileName').textContent=this.files[0] ? this.files[0].name : 'content-101-v2.1.0.zip'" style="display:none" type="file"/>
          <button class="btn btn-outline" onclick="document.getElementById('viewVersionFile').click()" style="padding:8px 16px; font-size:13px;" type="button">파일 변경</button>
        </div>
      </div>
      <!-- 버전 설명 -->
      <div>
        <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">버전 설명 (Release Notes)</label>
        <textarea id="viewReleaseNotes" style="width:100%; min-height:100px; padding:12px; border:1px solid #d1d5db; border-radius:4px; font-family:inherit; font-size:13px; resize:vertical;">- 버그 수정: 로그인 오류 해결
- 새 기능: 다크 모드 지원</textarea>
      </div>
    </div>
    <!-- Modal Footer -->
    <div style="padding:16px 20px; border-top:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; background:#f9fafb;">
      <button class="btn" style="background:#ef4444; color:white; border:none; padding:8px 16px; border-radius:4px; font-size:14px; cursor:pointer;" onclick="deleteVersion()" type="button">버전 삭제 (Delete)</button>
      <div style="display:flex; gap:10px;">
        <button class="btn btn-secondary" onclick="closeViewVersionModal()" type="button">취소 (Cancel)</button>
        <button class="btn btn-primary" onclick="updateVersion()" type="button">수정 완료 (Update)</button>
      </div>
    </div>
  </div>
</div>
"""

js_funcs = """
<script>
function downloadVersionFile(name) {
    const a = document.createElement('a');
    a.href = 'data:application/zip;base64,UEsFBgAAAAAAAAAAAAAAAAAAAAAAAA==';
    a.download = name || 'mock-file.zip';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}
function openViewVersionModal() {
    document.getElementById('viewVersionModal').style.display = 'flex';
}
function closeViewVersionModal() {
    document.getElementById('viewVersionModal').style.display = 'none';
}
function updateVersion() {
    alert('버전 정보가 성공적으로 수정되었습니다.');
    closeViewVersionModal();
}
function deleteVersion() {
    if(confirm('정말 이 버전을 삭제하시겠습니까? 파일이 완전히 삭제됩니다.')) {
        alert('버전이 삭제되었습니다.');
        closeViewVersionModal();
    }
}
</script>
"""

if 'id="viewVersionModal"' not in text:
    text = text.replace('</body>', view_modal + '\n' + js_funcs + '\n</body>')

# Handle "⬇️ Download" 
def replace_dl(m):
    s = m.group(0)
    if 'onclick' not in s:
        s = s.replace('<button', '<button onclick="downloadVersionFile(\'version-file.zip\')"')
    return s
text = re.sub(r'<button[^>]+>.*?Download.*?</button>', replace_dl, text)

# Handle "Change Status"
def replace_cs(m):
    s = m.group(0)
    if 'onclick' not in s:
        s = s.replace('<button', '<button onclick="openStatusModal()"')
    return s
text = re.sub(r'<button[^>]+>Change Status</button>', replace_cs, text)

# Inject View Button into gap:8px divs
def inject_view(m):
    block = m.group(0)
    if '>View</button>' not in block and '🔍 View' not in block:
        idx = block.rfind('</div>')
        btn = '\n                  <button class="btn btn-outline" style="padding:4px 8px; font-size:12px; color:#10b981; border-color:#10b981;" onclick="openViewVersionModal()">🔍 View</button>\n                '
        return block[:idx] + btn + block[idx:]
    return block
text = re.sub(r'<div style="display:flex; gap:8px;">.*?</div>', inject_view, text, flags=re.DOTALL)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Modal, JS, and updated Action Buttons successfully installed.")
