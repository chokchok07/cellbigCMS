import re

fname = 'CMS-webpage/wireframe_site/package-detail.html'
with open(fname, 'r', encoding='utf-8') as f:
    html = f.read()

# Make the count badge have an id
badge_pattern = r'(현재 선택된 콘텐츠: <span class="badge badge-success" style="font-size: 14px; padding: 2px 8px;")'
html = re.sub(badge_pattern, r'\1 id="modalSelectedCount"', html)

# Adjust checkboxes to call JS and have a unique class
html = re.sub(
    r'<input type="checkbox"(.*?)style="accent-color: #10b981; width: 16px; height: 16px; cursor: pointer;">',
    r'<input type="checkbox"\1 class="cnt-checkbox" onchange="updateModalCount()" style="accent-color: #10b981; width: 16px; height: 16px; cursor: pointer;">',
    html
)

# JS Block
js_snippet = """
    function updateModalCount() {
      const checkedCount = document.querySelectorAll('#manageModal .cnt-checkbox:checked').length;
      const badge = document.getElementById('modalSelectedCount');
      if (badge) badge.innerText = checkedCount + '개';
    }

    function submitManageContentsNew() {
      const checkedCount = document.querySelectorAll('#manageModal .cnt-checkbox:checked').length;
      alert(checkedCount + ' 개의 콘텐츠가 저장되었습니다.');
      closeModal('manageModal');
    }
"""

if "updateModalCount()" not in html:
    html = html.replace('function closeModal(id) {', js_snippet + '\n    function closeModal(id) {')

# Update "Done" button action
html = html.replace(
    '''onclick="alert('변경사항이 저장되었습니다.'); closeModal('manageModal')"''',
    '''onclick="submitManageContentsNew()"'''
)

with open(fname, 'w', encoding='utf-8') as f:
    f.write(html)
print("Updated JS and Hooks.")
