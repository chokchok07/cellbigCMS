import re

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = html.replace('onclick="simulateDownload(this)">⬇️ Download</button>', 'onclick="alert(\'다운로드를 시작합니다.\')">⬇️ Download</button>')
html = html.replace('onclick="alert(\'상태 변경 모달 오픈\')">Change Status</button>', 'onclick="openChangeStatusModal(this)">Change Status</button>')
html = html.replace('onclick="location.href=\'version-register.html\'">View</button>', 'onclick="openViewModal(this)">View</button>')

with open('CMS-webpage/wireframe_site/content-versions.html', 'w', encoding='utf-8') as f:
    f.write(html)
