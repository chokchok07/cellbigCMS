import glob, codecs

replacements = {
    '<th>콘텐츠명</th>': '<th>Title</th>',
    '<th style="width:100px">타입</th>': '<th style="width:100px">Type</th>',
    '<th style="width:140px">상태</th>': '<th style="width:140px">Status</th>',
    '<th style="width:100px">버전</th>': '<th style="width:100px">Version</th>',
    '<th style="width:180px">관리</th>': '<th style="width:180px">Actions</th>',
    '<th>장비명</th>': '<th>Device Name</th>',
    '<th>시리얼넘버(MAC)</th>': '<th>MAC Address</th>',
    '<th>매장</th>': '<th>Store</th>',
    '<th>등록일</th>': '<th>Registered Date</th>',
    '<th>패키지명</th>': '<th>Package Name</th>',
    '<th>콘텐츠 수</th>': '<th>Contents Count</th>',
    '<label>검색</label>': '<label>Search</label>',
    '<label>타입</label>': '<label>Type</label>',
    '<label>상태</label>': '<label>Status</label>',
    '<label>프로덕트</label>': '<label>Product</label>',
    '<button class="btn btn-secondary">검색 적용</button>': '<button class="btn btn-secondary">Apply Filters</button>',
    '>상세/수정</button>': '>View</button>',
    '>버전 관리</button>': '>Version</button>'
}

for filepath in glob.glob('*-list.html'):
    with codecs.open(filepath, 'r', 'utf-8') as f:
        text = f.read()
        
    for kr, en in replacements.items():
        text = text.replace(kr, en)
        
    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(text)

print('Reverted to English')
