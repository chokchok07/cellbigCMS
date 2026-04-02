import re

with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Make sure submitManageContentsNew is in there
if 'function submitManageContentsNew()' not in text:
    js_to_add = """
    <script>
    function updateModalCount() {
      const cnt = document.querySelectorAll('#manageModal .cnt-checkbox:checked').length;
      const target = document.getElementById('modalSelectedCount');
      if (target) {
        target.innerText = cnt + ' selected';
      }
    }

    function submitManageContentsNew() {
      const checked = document.querySelectorAll('#manageModal .cnt-checkbox:checked');
      alert(checked.length + ' 개의 콘텐츠가 패키지에 반영되었습니다.');
      closeModal('manageModal'); // close the large modal
    }
    </script>
    """
    text = text.replace('</body>', js_to_add + '\n</body>')

with open('CMS-webpage/wireframe_site/package-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added missing JS to package-detail.html")
