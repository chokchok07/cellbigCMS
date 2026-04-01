from bs4 import BeautifulSoup
import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add onclick to the 'Change Status' button
# We'll use regex for precision
text = re.sub(
    r'<button class="btn btn-secondary"([^>]*)>Change Status</button>',
    r'<button class="btn btn-secondary" \1 onclick="openVersionStatusModal(this, \'v2.1.0\', \'published\')">Change Status</button>',
    text, count=1 # Only first one for test or we can do all. Let's do it dynamically.
)

soup = BeautifulSoup(text, 'html.parser')

buttons = soup.find_all('button', string=lambda s: s and 'Change Status' in s)
for btn in buttons:
    # Get the parent card to figure out what version this is.
    card = btn.find_parent('div', class_='card')
    if not card: continue
    
    version_span = card.find('span', style=lambda s: s and 'font-size:20px' in s)
    if not version_span: continue
    version_txt = version_span.get_text(strip=True)
    
    badge_span = card.find('span', class_=lambda c: c and 'badge' in c)
    current_status = badge_span.get_text(strip=True).lower() if badge_span else 'test'
    
    btn['onclick'] = f"openVersionStatusModal(this, '{version_txt}', '{current_status}')"

# Add the modal HTML
modal_html = """
  <!-- Version Status Change Modal -->
  <div id="versionStatusModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(0,0,0,0.5); z-index:9999; align-items:center; justify-content:center; padding:20px;">
    <div style="background:#fff; border-radius:8px; width:100%; max-width:400px; overflow:hidden; box-shadow:0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);">
      <div style="padding:16px 20px; border-bottom:1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center; background:#f9fafb;">
        <h3 style="margin:0; font-size:18px; color:#111827;">상태 변경 (<span id="vsModalVersionLabel"></span>)</h3>
        <button type="button" style="background:transparent; border:none; font-size:24px; cursor:pointer; color:#6b7280;" onclick="closeVersionStatusModal()">&times;</button>
      </div>
      <div style="padding:20px;">
        <p style="margin-top:0; font-size:14px; color:#4b5563; margin-bottom:16px;">
          이 버전의 배포 상태를 변경합니다. 상태에 따라 단말(디바이스)로의 배포 여부가 결정됩니다.
        </p>
        
        <label style="display:block; margin-bottom:8px; font-weight:600; color:#374151; font-size:14px;">New Status</label>
        <select id="vsModalSelect" class="input" style="width:100%; margin-bottom:20px;">
          <option value="test">Test (테스트용 단말에서만 다운로드)</option>
          <option value="published">Published (전체 단말 상용 배포)</option>
          <option value="deprecated">Deprecated (배포 중단/사용 안함)</option>
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
    if(currentStatus.includes('published')) optionValue = 'published';
    if(currentStatus.includes('deprecated')) optionValue = 'deprecated';
    
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
          badge.style.background = '#dcfce7'; // green
          badge.style.color = '#1d4ed8';
        } else if (newStatus === 'test') {
          badge.className = 'badge badge-test';
          badge.textContent = 'Test';
          badge.style.background = '#fef3c7'; // yellow
          badge.style.color = '#b45309';
        } else if (newStatus === 'deprecated') {
          badge.className = 'badge';
          badge.textContent = 'Deprecated';
          badge.style.background = '#f3f4f6'; // gray
          badge.style.color = '#6b7280';
        }
      }
    }
    
    alert('상태가 성공적으로 변경되었습니다!');
    closeVersionStatusModal();
  }
"""

scripts = soup.find_all('script')
if scripts:
    last_script = scripts[-1]
    if 'openVersionStatusModal' not in last_script.text:
        last_script.append(js_code)
else:
    new_script = soup.new_tag('script')
    new_script.string = js_code
    soup.body.append(new_script)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(str(soup))
    
print("Change Status functionality added successfully!")
