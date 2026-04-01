from bs4 import BeautifulSoup
import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

soup = BeautifulSoup(html, 'html.parser')

buttons = soup.find_all('button', string=lambda s: s and 'Change Status' in s)
for btn in buttons:
    # Set onclick attribute properly
    card = btn.find_parent('div', class_='card')
    if not card: continue
    
    # Try to find the version span (vX.X.X) typically it's the first span with strong styling or large font
    # "display:flex; align-items:center" -> span inside
    version_span = card.find('span', style=lambda s: s and 'font-size:20px' in s)
    if not version_span:
        version_span = card.find('span', string=re.compile(r'v\d+\.\d+'))
        
    version_txt = version_span.get_text(strip=True) if version_span else 'Unknown'
    
    # get current badge
    badge = card.find('span', class_=re.compile(r'badge'))
    current_status = badge.get_text(strip=True).lower() if badge else 'test'
    
    btn['onclick'] = f"openVersionStatusModal(this, '{version_txt}', '{current_status}')"

# Add the modal HTML before body ends
modal_html = """
  <!-- Version Status Change Modal -->
  <div id="versionStatusModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; align-items:center; justify-content:center; padding:20px;">
    <div style="background:#fff; border-radius:8px; width:100%; max-width:400px; overflow:hidden; box-shadow:0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);">
      <div style="padding:16px 20px; border-bottom:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; background:#f9fafb;">
        <h3 style="margin:0; font-size:18px; color:#111827;">버전 상태 변경 (<span id="vsModalVersionLabel"></span>)</h3>
        <button type="button" style="background:transparent; border:none; font-size:24px; cursor:pointer; color:#6b7280;" onclick="closeVersionStatusModal()">&times;</button>
      </div>
      <div style="padding:20px;">
        <p style="margin-top:0; font-size:13px; color:#4b5563; margin-bottom:16px; line-height:1.5;">
          배포 상태에 따라 해당 콘텐츠 버전이 단말기로 다운로드될지 여부가 결정됩니다.
        </p>
        
        <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">새로운 상태 (New Status)</label>
        <select id="vsModalSelect" class="input" style="width:100%; margin-bottom:20px;">
          <option value="test">Test (테스트 기기에만 허용)</option>
          <option value="published">Published (상용/전체 기기 배포)</option>
          <option value="deprecated">Deprecated (배포 중지/사용 안함)</option>
        </select>
        
        <div style="display:flex; justify-content:flex-end; gap:8px;">
          <button type="button" class="btn btn-secondary" onclick="closeVersionStatusModal()">취소</button>
          <button type="button" class="btn btn-primary" onclick="submitVersionStatusChange()">변경 적용</button>
        </div>
      </div>
    </div>
  </div>
"""

# Append modal right before </body>
if not soup.find(id='versionStatusModal'):
    soup.body.append(BeautifulSoup(modal_html, 'html.parser'))

# JS Logic
js_code = """
  let currentStatusBtnTarget = null;
  
  function openVersionStatusModal(btnElement, version, currentStatus) {
    currentStatusBtnTarget = btnElement;
    document.getElementById('vsModalVersionLabel').textContent = version;
    
    // Normalize currentStatus
    let optionValue = 'test';
    if(currentStatus && currentStatus.toLowerCase().includes('published')) optionValue = 'published';
    if(currentStatus && currentStatus.toLowerCase().includes('deprecated')) optionValue = 'deprecated';
    
    document.getElementById('vsModalSelect').value = optionValue;
    document.getElementById('versionStatusModal').style.display = 'flex';
  }
  
  function closeVersionStatusModal() {
    document.getElementById('versionStatusModal').style.display = 'none';
    currentStatusBtnTarget = null;
  }
  
  function submitVersionStatusChange() {
    if(!currentStatusBtnTarget) return;
    
    const newStatus = document.getElementById('vsModalSelect').value;
    
    // Find the badge element in the card
    const card = currentStatusBtnTarget.closest('.card');
    if(card) {
      const badge = card.querySelector('.badge');
      if(badge) {
        if(newStatus === 'published') {
          badge.className = 'badge badge-published';
          badge.textContent = 'Published';
          badge.style.backgroundColor = '#d1fae5'; // light green
          badge.style.color = '#047857';
        } else if (newStatus === 'test') {
          badge.className = 'badge badge-test';
          badge.textContent = 'Test';
          badge.style.backgroundColor = '#fef3c7'; // yellow
          badge.style.color = '#b45309';
        } else if (newStatus === 'deprecated') {
          // Default grey badge
          badge.className = 'badge';
          badge.textContent = 'Deprecated';
          badge.style.backgroundColor = '#f3f4f6'; // gray
          badge.style.color = '#6b7280';
        }
      }
    }
    
    // Optional: show a quick Toast or just close
    closeVersionStatusModal();
    // Simulate slight delay for effect
    setTimeout(() => {
        alert('버전 배포 상태가 성공적으로 변경되었습니다.');
    }, 100);
  }
"""

scripts = soup.find_all('script')
if scripts:
    last_script = scripts[-1]
    if last_script.string and 'openVersionStatusModal' not in last_script.string:
        last_script.string += f"\n{js_code}\n"
    elif not last_script.string:
        last_script.string = js_code
else:
    new_script = soup.new_tag('script')
    new_script.string = js_code
    soup.body.append(new_script)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(str(soup).replace('&times;', '×')) # safe encoding fallback
    
print("Change Status functionality added successfully!")
