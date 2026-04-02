# -*- coding: utf-8 -*-
text = open('content-list.html', encoding='utf-8').read()

text = text.replace('<th>Title</th>', '<th>콘텐츠명</th>')
text = text.replace('<th style="width:100px">Type</th>', '<th style="width:100px">타입</th>')
text = text.replace('<th style="width:140px">Status</th>', '<th style="width:140px">상태</th>')
text = text.replace('<th style="width:100px">Version</th>', '<th style="width:100px">버전</th>')
text = text.replace('<th style="width:180px">Actions</th>', '<th style="width:180px">관리</th>')

# Fix filter panel
text = text.replace('<label>Search</label>', '<label>검색</label>')
text = text.replace('<label>Type</label>', '<label>타입</label>')
text = text.replace('<label>Status</label>', '<label>상태</label>')
text = text.replace('<label>Product</label>', '<label>프로덕트</label>')
text = text.replace('<button class="btn btn-secondary">Apply Filters</button>', '<button class="btn btn-secondary">검색 적용</button>')

# View button to Detail + Adding Ver button
old_btn_code = '<button class="action-btn" onclick="window.location.href=\'content-editor.html?id=101\'">View</button>'
new_btn_code = '''<button class="action-btn" onclick="window.location.href='content-detail.html?id=101'">상세/수정</button>
                      <button class="action-btn" onclick="window.location.href='content-versions.html?id=101'">버전 관리</button>'''
text = text.replace(old_btn_code, new_btn_code)

open('content-list.html', 'w', encoding='utf-8').write(text)
print('Done!')
