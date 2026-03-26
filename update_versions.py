import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make the grid 4 columns instead of 3
html = html.replace('grid-template-columns: 2fr 1fr 1fr;', 'grid-template-columns: 2fr 1fr 1.2fr 1fr;')

# Replacement logic for each version item:
# v2.1.0
old_col3_v2_1 = '''    <!-- Col 3: Actions & Meta -->
    <div style="display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end;">
      <div style="text-align:right; font-size:12px; color:#6b7280;">
        <div>Created: 2026-03-10 14:00</div>
        <div>By: admin@example.com</div>
      </div>
      <div style="display:flex; gap:8px;">
        <button class="btn btn-outline" style="padding:4px 8px; font-size:12px;">⬇️ Download</button>
        <button class="btn btn-secondary" style="padding:4px 8px; font-size:12px;">Change Status</button>
      </div>
    </div>'''

new_col3_4_v2_1 = '''    <!-- Col 3: Dates & Meta -->
    <div style="font-size:13px; color:#4b5563; display:flex; flex-direction:column; gap:8px; justify-content:center;">
      <div><strong>등록일:</strong> 2026-03-10 14:00</div>
      <div><strong>수정일:</strong> 2026-03-10 14:00</div>
      <div><strong>작성자:</strong> admin@example.com</div>
    </div>

    <!-- Col 4: Actions -->
    <div style="display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end;">
      <div style="display:flex; gap:6px; flex-wrap:wrap; justify-content:flex-end; width:100%;">
        <button class="btn btn-secondary" style="padding:4px 8px; font-size:12px;">수정</button>
        <button class="btn" style="background:#ef4444; color:white; border:none; padding:4px 8px; font-size:12px; border-radius:4px;">삭제</button>
      </div>
      <div style="display:flex; gap:6px; margin-top:8px;">
        <button class="btn btn-outline" style="padding:4px 8px; font-size:12px;">⬇️ 다운로드</button>
      </div>
    </div>'''

html = html.replace(old_col3_v2_1, new_col3_4_v2_1)


# v2.0.0
old_col3_v2_0 = '''    <!-- Col 3: Actions & Meta -->
    <div style="display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end;">
      <div style="text-align:right; font-size:12px; color:#6b7280;">
        <div>Created: 2026-03-05 10:20</div>
        <div>By: developer@example.com</div>
      </div>
      <div style="display:flex; gap:8px;">
        <button class="btn btn-outline" style="padding:4px 8px; font-size:12px;">⬇️ Download</button>
        <button class="btn btn-primary" style="padding:4px 8px; font-size:12px;">Publish Now</button>
      </div>
    </div>'''

new_col3_4_v2_0 = '''    <!-- Col 3: Dates & Meta -->
    <div style="font-size:13px; color:#4b5563; display:flex; flex-direction:column; gap:8px; justify-content:center;">
      <div><strong>등록일:</strong> 2026-03-05 10:20</div>
      <div><strong>수정일:</strong> 2026-03-08 09:15</div>
      <div><strong>작성자:</strong> developer@example.com</div>
    </div>

    <!-- Col 4: Actions -->
    <div style="display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end;">
      <div style="display:flex; gap:6px; flex-wrap:wrap; justify-content:flex-end; width:100%;">
        <button class="btn btn-secondary" style="padding:4px 8px; font-size:12px;">수정</button>
        <button class="btn" style="background:#ef4444; color:white; border:none; padding:4px 8px; font-size:12px; border-radius:4px;">삭제</button>
      </div>
      <div style="display:flex; gap:6px; margin-top:8px;">
        <button class="btn btn-primary" style="padding:4px 8px; font-size:12px;">Publish Now</button>
        <button class="btn btn-outline" style="padding:4px 8px; font-size:12px;">⬇️ 다운로드</button>
      </div>
    </div>'''

html = html.replace(old_col3_v2_0, new_col3_4_v2_0)


# v1.1.0
old_col3_v1_1 = '''    <!-- Col 3: Actions & Meta -->
    <div style="display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end;">
      <div style="text-align:right; font-size:12px; color:#6b7280;">
        <div>Created: 2026-01-15 09:00</div>
        <div>By: admin@example.com</div>
      </div>
      <div style="display:flex; gap:8px;">
        <button class="btn btn-outline" style="padding:4px 8px; font-size:12px;">⬇️ Download</button>
      </div>
    </div>'''

new_col3_4_v1_1 = '''    <!-- Col 3: Dates & Meta -->
    <div style="font-size:13px; color:#4b5563; display:flex; flex-direction:column; gap:8px; justify-content:center;">
      <div><strong>등록일:</strong> 2026-01-15 09:00</div>
      <div><strong>수정일:</strong> 2026-02-01 11:30</div>
      <div><strong>작성자:</strong> admin@example.com</div>
    </div>

    <!-- Col 4: Actions -->
    <div style="display:flex; flex-direction:column; justify-content:space-between; align-items:flex-end;">
      <div style="display:flex; gap:6px; flex-wrap:wrap; justify-content:flex-end; width:100%;">
        <button class="btn btn-secondary" style="padding:4px 8px; font-size:12px;">수정</button>
        <button class="btn" style="background:#ef4444; color:white; border:none; padding:4px 8px; font-size:12px; border-radius:4px;">삭제</button>
      </div>
      <div style="display:flex; gap:6px; margin-top:8px;">
        <button class="btn btn-outline" style="padding:4px 8px; font-size:12px;">⬇️ 다운로드</button>
      </div>
    </div>'''

html = html.replace(old_col3_v1_1, new_col3_4_v1_1)

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Updated versions page")
