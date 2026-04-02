import re

files = ['CMS-webpage/wireframe_site/package-detail.html', 'CMS-webpage/wireframe_site/package-editor.html']

for fname in files:
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()

    print(f"Modifying {fname}...")
    
    # 1. Remove Version
    version_pattern = r'<div class="form-group">\s*<label class="form-label(?: required)?">Version</label>\s*<input[^>]*>\s*</div>'
    html = re.sub(version_pattern, '', html, flags=re.IGNORECASE)
    
    # Sometimes it's without 'form-group' just inline? Let's check for "Version"
    html = re.sub(r'<div[^>]*>\s*<label[^>]*>Version</label>\s*<input[^>]*>\s*</div>', '', html, flags=re.IGNORECASE)
    
    if 'package-detail.html' in fname:
        # Check if version exists in detail (e.g. grid-template-columns...)
        version_detail_pattern = r'<div class="info-label"[^>]*>Version:?</div>\s*<input[^>]*>'
        html = re.sub(version_detail_pattern, '', html, flags=re.IGNORECASE | re.DOTALL)
        
        # 2. Update manage modal
        new_modal = """<div class="modal-overlay" id="manageModal" style="display: none; position: fixed; top: 0; left: 0; right: 0; bottom: 0; background: rgba(0,0,0,0.5); align-items: center; justify-content: center; z-index: 1000;">
    <div class="modal-content" style="background: white; border-radius: 8px; width: 600px; max-height: 80vh; display: flex; flex-direction: column; overflow: hidden; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);">
      <div class="modal-header" style="padding: 16px 24px; border-bottom: 1px solid #e5e7eb; display: flex; justify-content: space-between; align-items: center;">
        <h2 style="margin: 0; font-size: 18px; color: #111827;">Connected Contents</h2>
        <button type="button" onclick="closeModal('manageModal')" style="background: none; border: none; font-size: 20px; cursor: pointer; color: #6b7280;">&times;</button>
      </div>
      <div class="modal-body" style="padding: 24px; overflow-y: auto;">
        
        <!-- Search part -->
        <div style="margin-bottom: 20px;">
          <label style="display: block; font-size: 14px; font-weight: 500; color: #374151; margin-bottom: 8px;">Product 기준 콘텐츠 검색</label>
          <div style="display: flex; gap: 8px;">
            <input type="text" class="input" style="flex: 1;" placeholder="콘텐츠 이름 또는 ID 검색...">
            <button class="btn btn-secondary">Search</button>
          </div>
        </div>

        <!-- Contents List -->
        <div style="border: 1px solid #e5e7eb; border-radius: 6px; overflow: hidden;">
          <table class="content-table" style="width: 100%; border-collapse: collapse;">
            <thead>
              <tr style="background: #f9fafb; border-bottom: 1px solid #e5e7eb;">
                <th style="padding: 12px; text-align: left; font-size: 13px; color: #4b5563;">Content ID</th>
                <th style="padding: 12px; text-align: left; font-size: 13px; color: #4b5563;">Name</th>
                <th style="padding: 12px; text-align: center; font-size: 13px; color: #4b5563;">Action</th>
              </tr>
            </thead>
            <tbody>
              <!-- Added Content -->
              <tr style="border-bottom: 1px solid #e5e7eb;">
                <td style="padding: 12px; font-family: monospace; color: #6b7280;">c-sand-01</td>
                <td style="padding: 12px; color: #111827;">화산 폭발 (Volcano)</td>
                <td style="padding: 12px; text-align: center;">
                  <button class="btn btn-danger" style="padding: 4px 8px; font-size: 12px;">Remove</button>
                </td>
              </tr>
              <!-- Added Content -->
              <tr style="border-bottom: 1px solid #e5e7eb;">
                <td style="padding: 12px; font-family: monospace; color: #6b7280;">c-sand-02</td>
                <td style="padding: 12px; color: #111827;">공룡 화석 발굴 (Dino)</td>
                <td style="padding: 12px; text-align: center;">
                  <button class="btn btn-danger" style="padding: 4px 8px; font-size: 12px;">Remove</button>
                </td>
              </tr>
              <!-- Not Added Content -->
              <tr style="border-bottom: 1px solid #e5e7eb; background: #fefce8;">
                <td style="padding: 12px; font-family: monospace; color: #6b7280;">c-sand-03</td>
                <td style="padding: 12px; color: #111827;">개미왕국 (Ants)</td>
                <td style="padding: 12px; text-align: center;">
                  <button class="btn btn-primary" style="padding: 4px 8px; font-size: 12px;">Add</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>

      </div>
      <div class="modal-footer" style="padding: 16px 24px; border-top: 1px solid #e5e7eb; display: flex; justify-content: flex-end; gap: 8px;">
        <button type="button" class="btn btn-primary" onclick="alert('변경사항이 저장되었습니다.'); closeModal('manageModal')">Done</button>
      </div>
    </div>
  </div>"""

        # Replace existing manageModal
        m = re.search(r'<div class="modal-overlay" id="manageModal"[\s\S]*?(?=<script>)', html)
        if m:
            html = html[:m.start()] + new_modal + '\n\n  ' + html[m.end():]
        else:
            print("  manageModal not found, appending before </body>...")
            html = html.replace('</body>', new_modal + '\n</body>')

    with open(fname, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Saved {fname}")
