import re

with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Clean up the button's onclick
text = re.sub(
    r'onclick="[^"]*confirm\([^"]*\)[^"]*submitManageContentsNew\(\);?\s*}?"',
    r'onclick="submitManageContentsNew()"',
    text
)

# 2. Put the confirm inside the function
new_func = """function submitManageContentsNew() {
      if (!confirm('콘텐츠를 추가하시겠습니까?')) return;
      const checked = document.querySelectorAll('#manageModal .cnt-checkbox:checked');
      alert(checked.length + ' 개의 콘텐츠가 패키지에 반영되었습니다.');
      closeModal('manageModal'); // close the large modal
    }"""

text = re.sub(
    r'function submitManageContentsNew\(\)\s*\{[\s\S]*?closeModal\(\'manageModal\'\);[^\}]*\}',
    new_func,
    text
)

with open('CMS-webpage/wireframe_site/package-detail.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Applied fix.")
