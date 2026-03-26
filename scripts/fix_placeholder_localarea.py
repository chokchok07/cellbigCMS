import io

fp = "CMS-webpage/wireframe_site/localarea-editor.html"
with io.open(fp, 'r', encoding='utf-8') as f:
    html = f.read()

# Fix Name
html = html.replace(
    'class="input" style="width:100%;" value="KR-SEOUL"',
    'class="input" style="width:100%;" value="" placeholder="예: 서울 권역 (Seoul Region)"'
)
# Manager (if any)
html = html.replace(
    'class="input" style="width:100%;" value="Admin"',
    'class="input" style="width:100%;" value="" placeholder="예: 관리자 이름 (홍길동)"'
)
# Description
html = html.replace(
    'class="input" style="width:100%; height:80px; resize:vertical">Seoul Main Area</textarea>',
    'class="input" style="width:100%; height:80px; resize:vertical" placeholder="예: 서울특별시 및 수도권 지역을 포괄하는 그룹입니다."></textarea>'
)

with io.open(fp, 'w', encoding='utf-8') as f:
    f.write(html)
print("localarea-editor placeholders fixed")
