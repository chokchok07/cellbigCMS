import re

file_path = 'CMS-webpage/wireframe_site/device-detail.html'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add Auth Mode toggle inside the left info panel
auth_html = '''          <div class="info-group">
            <label class="info-label">Auth Mode</label>
            <div style="display:flex; gap:16px; align-items:center;">
              <label style="display:flex; align-items:center; gap:4px; cursor:pointer;">
                <input type="radio" name="authMode" value="online" checked style="cursor:pointer;"> 
                <span style="font-size:14px; color:#374151;">온라인 (상시 인증)</span>
              </label>
              <label style="display:flex; align-items:center; gap:4px; cursor:pointer;">
                <input type="radio" name="authMode" value="offline" style="cursor:pointer;"> 
                <span style="font-size:14px; color:#374151;">오프라인 (One-time)</span>
              </label>
              <button type="button" id="btnDownloadKey" style="display:none; margin-left:12px; padding:4px 8px; background:#10b981; color:white; border:none; border-radius:4px; font-size:12px; cursor:pointer;">🔑 Key 다운로드</button>
            </div>
          </div>'''

if 'Auth Mode' not in text:
    text = re.sub(r'(<div class="info-group">\s*<label class="info-label">Store</label>.*?</select>\s*</div>)', r'\1\n' + auth_html, text, flags=re.DOTALL)

# 2. Modify the Installed Packages table to add delete buttons and an 'Add' button
package_table_head = '''<thead>
              <tr style="background:#f8fafc; text-align:left;">
                <th style="padding:12px; font-weight:600; color:#475569; width:20%;">Package ID</th>
                <th style="padding:12px; font-weight:600; color:#475569; width:40%;">Package Name</th>
                <th style="padding:12px; font-weight:600; color:#475569; width:20%;">Version</th>
                <th style="padding:12px; font-weight:600; color:#475569; width:20%; text-align:right;">Action</th>
              </tr>
            </thead>'''

if 'Action</th>' not in text:
    text = re.sub(r'<thead>.*?</thead>', package_table_head, text, flags=re.DOTALL, count=1)

package_tbody = '''<tbody>
              <tr style="border-bottom:1px solid #f1f5f9">
                <td style="padding:12px; font-weight:500; color:#2563eb;"><a href="package-detail.html" style="text-decoration:none; color:inherit;">PKG-101</a></td>
                <td style="padding:12px">Kiosk Standard Pack</td>
                <td style="padding:12px">v1.2.0</td>
                <td style="padding:12px; text-align:right;">
                  <button style="padding:4px 8px; border:1px solid #ef4444; background:#fff; color:#ef4444; border-radius:4px; cursor:pointer; font-size:12px;">제거</button>
                </td>
              </tr>
              <tr style="border-bottom:1px solid #f1f5f9">
                <td style="padding:12px; font-weight:500; color:#2563eb;"><a href="package-detail.html" style="text-decoration:none; color:inherit;">PKG-105</a></td>
                <td style="padding:12px">Event Promo Pack</td>
                <td style="padding:12px">v2.0.1</td>
                <td style="padding:12px; text-align:right;">
                  <button style="padding:4px 8px; border:1px solid #ef4444; background:#fff; color:#ef4444; border-radius:4px; cursor:pointer; font-size:12px;">제거</button>
                </td>
              </tr>
            </tbody>'''

if '제거</button>' not in text:
    text = re.sub(r'<tbody>.*?</tbody>', package_tbody, text, flags=re.DOTALL, count=1)

add_package_div = '''<div style="padding: 12px; background: #fff; border-top: 1px solid #e5e7eb; display:flex; justify-content:space-between; align-items:center;">
              <select style="padding:6px; border:1px solid #d1d5db; border-radius:4px; width:60%;">
                <option value="">➕ 설치할 패키지 선택...</option>
                <option value="PKG-106">PKG-106 (Summer Event Pack)</option>
                <option value="PKG-107">PKG-107 (Admin Tools)</option>
              </select>
              <button style="padding:6px 12px; background:#2563eb; color:white; border:none; border-radius:4px; cursor:pointer; font-size:13px; font-weight:500;">추가</button>
            </div>'''
if '설치할 패키지 선택' not in text:
    # Need to append right after the table
    text = text.replace('</table>', '</table>\n            ' + add_package_div, 1)

script_auth = '''<script>
      document.querySelectorAll('input[name="authMode"]').forEach(radio => {
        radio.addEventListener('change', (e) => {
          const btn = document.getElementById('btnDownloadKey');
          if(e.target.value === 'offline') {
            btn.style.display = 'inline-block';
            btn.classList.add('pulse-anim');
          } else {
            btn.style.display = 'none';
            btn.classList.remove('pulse-anim');
          }
        });
      });
    </script>
    <style>
      @keyframes popPulse { 0% { transform: scale(1); } 50% { transform: scale(1.05); } 100% { transform: scale(1); } }
      .pulse-anim { animation: popPulse 1.5s infinite; }
    </style>'''

if 'pulse-anim' not in text:
    text = text.replace('</body>', script_auth + '\n  </body>')

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(text)

print("Updates successfully applied to device-detail.html!")
