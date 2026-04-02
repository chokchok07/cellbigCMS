# -*- coding: utf-8 -*-
import glob, codecs, re

for filepath in glob.glob('*-list.html'):
    if filepath == 'content-list.html': continue # Skip already done
    with codecs.open(filepath, 'r', 'utf-8') as f:
        text = f.read()

    # Change editor to detail
    text = re.sub(r'onclick="window\.location\.href=\'([\w-]+)-editor\.html\?id=(\w+)\'">View</button>',
                  r'onclick="window.location.href=\'\1-detail.html?id=\2\'">상세/수정</button>', text)
                  
    # If there are any remaining just 'View' buttons
    text = text.replace('>View</button>', '>상세/수정</button>')

    # Translate some common headers and filters
    text = text.replace('<th>Type</th>', '<th>타입</th>')
    text = text.replace('<th>Status</th>', '<th style="width:140px">상태</th>')
    text = text.replace('<th>Version</th>', '<th style="width:100px">버전</th>')
    text = text.replace('<th>Actions</th>', '<th style="width:180px">관리</th>')
    
    # Specific ones
    text = text.replace('<th>Device Name</th>', '<th>장비명</th>')
    text = text.replace('<th>MAC Address</th>', '<th>시리얼넘버(MAC)</th>')
    text = text.replace('<th>Store</th>', '<th>매장</th>')
    text = text.replace('<th>Registered Date</th>', '<th>등록일</th>')
    text = text.replace('<th>Package Name</th>', '<th>패키지명</th>')
    text = text.replace('<th>Contents Count</th>', '<th>콘텐츠 수</th>')

    # Common labels
    text = text.replace('<label>Search</label>', '<label>검색</label>')
    text = text.replace('<label>Status</label>', '<label>상태</label>')
    text = text.replace('<button class="btn btn-secondary">Apply Filters</button>', '<button class="btn btn-secondary">검색 적용</button>')

    # Remove escapes from re.sub replacement
    text = text.replace(r"href=\'", "href='")
    text = text.replace(r"101\'", "101'")
    text = text.replace(r"102\'", "102'")
    text = text.replace(r"103\'", "103'")

    with codecs.open(filepath, 'w', 'utf-8') as f:
        f.write(text)

print('Global list fix applied.')
