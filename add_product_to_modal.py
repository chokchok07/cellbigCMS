import re

with open('CMS-webpage/wireframe_site/content-list.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Insert Product selection after Title
product_html = """          </div>

          <div class="form-group" style="margin-bottom:16px;">
            <label class="form-label" style="display:block; margin-bottom:6px; font-size:13px; font-weight:500;">Product (제품 할당)</label>
            <select class="input" style="width:100%; padding:8px 12px; border:1px solid #d1d5db; border-radius:6px;">
              <option value="">선택 안함</option>
              <option value="sandcraft">샌드크래프트 (SandCraft)</option>
              <option value="actionwall">액션월 (ActionWall)</option>
              <option value="alive">얼라이브 (Alive)</option>
            </select>
          </div>"""

html = html.replace('          </div>\n\n          <div class="form-group" style="margin-bottom:16px;">\n            <label class="form-label" style="display:block; margin-bottom:6px; font-size:13px; font-weight:500;">Description (설명)</label>', product_html + '\n\n          <div class="form-group" style="margin-bottom:16px;">\n            <label class="form-label" style="display:block; margin-bottom:6px; font-size:13px; font-weight:500;">Description (설명)</label>')


# 2. Add onChange and Size display to Initial Upload
upload_orig = """            <input type="file" id="modalFileUpload" style="display:none" accept=".zip">
          </div>
        </div>"""

upload_new = """            <input type="file" id="modalFileUpload" style="display:none" accept=".zip" onchange="handleModalFileUpload(event)">
          </div>
          <div id="modalFileSizeDisplay" style="margin-top:12px; font-size:14px; color:#3b82f6; text-align:center; display:none;"></div>
        </div>"""

html = html.replace(upload_orig, upload_new)

# 3. Add JS function
js_func = """    function handleModalFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        const sizeMB = (file.size / (1024 * 1024)).toFixed(2);
        const display = document.getElementById('modalFileSizeDisplay');
        display.style.display = 'block';
        display.innerHTML = `선택된 파일: <strong>${file.name}</strong> (${sizeMB} MB)`;
      }
    }
  </script>"""

html = html.replace("  </script>", js_func)

with open('CMS-webpage/wireframe_site/content-list.html', 'w', encoding='utf-8') as f:
    f.write(html)
