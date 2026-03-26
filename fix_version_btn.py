with open('CMS-webpage/wireframe_site/version-register.html', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace("onclick=\"alert('신규 업데이트 등록 화면으로 이동합니다.');\"", "onclick=\"location.href='version-editor.html'\"")
text = text.replace("alert('신규 업데이트 등록 화면으로 이동합니다.');", "location.href='version-editor.html';")

with open('CMS-webpage/wireframe_site/version-register.html', 'w', encoding='utf-8') as f:
    f.write(text)
print('Linked version-register.html to version-editor.html')
