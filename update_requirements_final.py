import re

with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    html = f.read()

new_modal = """<div class="modal-overlay" id="manageModal" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); align-items: center; justify-content: center; z-index: 1000;">
    <div class="modal-content" style="background: white; border-radius: 8px; width: 600px; max-height: 80vh; display: flex; flex-direction: column; overflow: hidden; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);">
      <div class="modal-header" style="padding: 16px 24px; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center;">
        <h2 style="margin: 0; font-size: 18px; color: #111827;">Connected Contents</h2>
        <button type="button" onclick="closeModal('manageModal')" style="background: none; border: none; font-size: 20px; cursor: pointer; color: #6b7280;">&times;</button>
      </div>
      <div class="modal-body" style="padding: 24px; overflow-y: auto;">
        
        <!-- Search part -->
        <div style="margin-bottom: 20px; display: flex; justify-content: space-between; align-items: flex-end;">
          <div style="flex: 1; margin-right: 20px;">
            <label style="display: block; font-size: 14px; font-weight: 500; color: #374151; margin-bottom: 8px;">Product 선택</label>
            <div style="display: flex; gap: 8px;">
              <select class="input" style="flex: 1;">
                <option value="">All Products</option>
                <option value="sandcraft" selected>SandCraft</option>
                <option value="fishworld">FishWorld</option>
              </select>
              <button class="btn btn-secondary">Search</button>
            </div>
          </div>
          <div style="font-size: 14px; font-weight: 600; color: #111827; white-space: nowrap;">
            현재 선택된 콘텐츠: <span class="badge badge-success" style="font-size: 14px; padding: 2px 8px;">2개</span>
          </div>
        </div>

        <!-- Contents List -->
        <div style="border: 1px solid #e5e7eb; border-radius: 6px; overflow: hidden;">
          <table class="content-table" style="width: 100%; border-collapse: collapse;">
            <thead>
              <tr style="background: #f9fafb; border-bottom: 1px solid #e5e7eb;">
                <th style="padding: 12px; text-align: left; font-size: 13px; color: #4b5563;">Content ID</th>
                <th style="padding: 12px; text-align: left; font-size: 13px; color: #4b5563;">Name</th>
                <th style="padding: 12px; text-align: center; font-size: 13px; color: #4b5563;">상태</th>
                <th style="padding: 12px; text-align: center; font-size: 13px; color: #4b5563;">Action</th>
              </tr>
            </thead>
            <tbody>
              <!-- Added Content -->
              <tr style="border-bottom: 1px solid #e5e7eb;">
                <td style="padding: 12px; font-family: monospace; color: #6b7280;">c-sand-01</td>
                <td style="padding: 12px; color: #111827;">화산 폭발 (Volcano)</td>
                <td style="padding: 12px; text-align: center;">
                  <span style="display:inline-block; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 600; background: #def7ec; color: #03543f;">✔ 포함됨</span>
                </td>
                <td style="padding: 12px; text-align: center;">
                  <label style="cursor: pointer; display: inline-flex; align-items: center; gap: 4px;">
                    <input type="checkbox" checked style="accent-color: #10b981; width: 16px; height: 16px; cursor: pointer;">
                  </label>
                </td>
              </tr>
              <!-- Added Content -->
              <tr style="border-bottom: 1px solid #e5e7eb;">
                <td style="padding: 12px; font-family: monospace; color: #6b7280;">c-sand-02</td>
                <td style="padding: 12px; color: #111827;">공룡 화석 발굴 (Dino)</td>
                <td style="padding: 12px; text-align: center;">
                  <span style="display:inline-block; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 600; background: #def7ec; color: #03543f;">✔ 포함됨</span>
                </td>
                <td style="padding: 12px; text-align: center;">
                  <label style="cursor: pointer; display: inline-flex; align-items: center; gap: 4px;">
                    <input type="checkbox" checked style="accent-color: #10b981; width: 16px; height: 16px; cursor: pointer;">
                  </label>
                </td>
              </tr>
              <!-- Not Added Content -->
              <tr style="border-bottom: 1px solid #e5e7eb; background: #f9fafb;">
                <td style="padding: 12px; font-family: monospace; color: #6b7280;">c-sand-03</td>
                <td style="padding: 12px; color: #111827;">개미왕국 (Ants)</td>
                <td style="padding: 12px; text-align: center;">
                  <span style="display:inline-block; padding: 2px 8px; border-radius: 12px; font-size: 12px; font-weight: 600; background: #f3f4f6; color: #6b7280;">미포함</span>
                </td>
                <td style="padding: 12px; text-align: center;">
                  <label style="cursor: pointer; display: inline-flex; align-items: center; gap: 4px;">
                    <input type="checkbox" style="accent-color: #10b981; width: 16px; height: 16px; cursor: pointer;">
                  </label>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

      </div>
      <div class="modal-footer" style="padding: 16px 24px; border-top: 1px solid #e5e7eb; display: flex; justify-content: flex-end; gap: 8px;">
        <button type="button" class="btn btn-secondary" onclick="closeModal('manageModal')">Cancel</button>
        <button type="button" class="btn btn-primary" onclick="alert('변경사항이 저장되었습니다.'); closeModal('manageModal')">Done</button>
      </div>
    </div>
  </div>"""

m = re.search(r'<div class="modal-overlay" id="manageModal"[\s\S]*?(?=<script>|</body|</body>)', html)
if m:
    html = html[:m.start()] + new_modal + '\n' + html[m.end():]
    with open('CMS-webpage/wireframe_site/package-detail.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Replaced modal.")
else:
    print("Could not find modal boundary.")
