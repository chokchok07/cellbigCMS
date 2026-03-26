import sys

filename = 'CMS-webpage/wireframe_site/product-detail.html'
with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

# Make absolutely sure it's not already there to avoid duplicates
if 'function openPackageSelectionModal()' not in content:
    script_html = '''
  <script>
    function openPackageSelectionModal() {
      document.getElementById('packageSelectionModal').style.display = 'flex';
    }
    function closePackageSelectionModal() {
      document.getElementById('packageSelectionModal').style.display = 'none';
    }
    function submitPackageSelection() {
      const checked = document.querySelectorAll('.pkg-checkbox:checked');
      if (checked.length === 0) {
        alert('추가할 패키지를 선택해주세요.');
        return;
      }
      alert(checked.length + '개의 패키지가 성공적으로 추가되었습니다.');
      closePackageSelectionModal();
    }
  </script>
'''
    content = content.replace('</body>', script_html + '\n</body>')
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Script injected!")
else:
    print("Script already present! Need to debug where it went.")
