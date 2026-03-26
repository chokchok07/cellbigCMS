import re

def update_api():
    with open('api.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update /devices/register Body
    html = html.replace(
        '<tr><td>macAddress</td><td>string</td><td>Yes</td><td>PC의 물리적 MAC 주소 (식별자)</td></tr>\n                      <tr><td>systemInfo</td><td>object</td><td>No</td><td>OS 버전, CPU, RAM 등 시스템 정보</td></tr>',
        '''<tr><td>macAddress</td><td>string</td><td>Yes</td><td>PC의 물리적 MAC 주소 (식별자)</td></tr>
                      <tr><td>storeId</td><td>array</td><td>Yes</td><td>스토어 고유 ID (2개 이상 입력 가능)</td></tr>
                      <tr><td>productId</td><td>array</td><td>No</td><td>상품 ID (2개 이상 입력 가능)</td></tr>
                      <tr><td>meta</td><td>object</td><td>No</td><td>CPU모델명, RAM 용량, GPU 모델명, 디스크 여유공간, OS버전, 해상도 등 하드웨어 사양 정보</td></tr>'''
    )

    # 2. Update /devices/{deviceId}/info Body
    html = html.replace(
        '<tr><td>systemInfo</td><td>object</td><td>Yes</td><td>os, cpu, ramTotal, diskFree 등 시스템 세부 스펙</td></tr>',
        '<tr><td>meta</td><td>object</td><td>Yes</td><td>CPU, RAM, GPU, 디스크, OS, 해상도 등 최신 하드웨어 사양 스펙 JSON</td></tr>'
    )
    html = html.replace(
        '"systemInfo": {\n                          "os": "Windows 10",\n                          "cpu": "Intel i7",\n                          "ramTotal": "16GB",\n                          "diskFree": "500GB"\n                      }',
        '"meta": {\n                          "os": "Windows 10",\n                          "cpu": "Intel i7",\n                          "gpu": "RTX 3060",\n                          "ram": "16GB",\n                          "diskFree": "500GB",\n                          "resolution": "1920x1080"\n                      }'
    )

    # 3. Add Notice API under #admin-api
    # Find the end of admin-api or a suitable place. Before '<!-- Logs API -->' or '<section id="log-api">'
    notice_api_html = """
        <h3>공지사항 관리 (Notices)</h3>
        <p>어드민 대시보드 및 클라이언트 팝업 등을 위한 공지사항 데이터를 관리합니다.</p>

        <!-- [POST] 공지사항 등록 -->
        <div class="endpoint-card">
            <div class="endpoint-header">
                <span class="method post">POST</span>
                <span class="path">/notices</span>
                <span class="tag tag-admin">Admin</span>
                <span class="desc">신규 공지사항 등록</span>
            </div>
            <div class="endpoint-body">
                <p>새로운 공지사항을 생성합니다.</p>
                <h4>Parameters (Body)</h4>
                <table>
                    <tr><th>Field</th><th>Type</th><th>Required</th><th>Description</th></tr>
                    <tr><td>title</td><td>string</td><td>Yes</td><td>공지사항 제목</td></tr>
                    <tr><td>content</td><td>string</td><td>Yes</td><td>공지사항 본문</td></tr>
                    <tr><td>importance</td><td>enum</td><td>No</td><td>NORMAL, URGENT</td></tr>
                    <tr><td>display_method</td><td>enum</td><td>Yes</td><td>DASHBOARD, POPUP, BOTH</td></tr>
                    <tr><td>target_type</td><td>enum</td><td>Yes</td><td>ALL, AREA, STORE</td></tr>
                    <tr><td>target_ids</td><td>array</td><td>No</td><td>노출 대상 ID 목록 (ALL이면 null/빈 배열)</td></tr>
                    <tr><td>start_at</td><td>string</td><td>Yes</td><td>게시 시작 일시 (DateTime)</td></tr>
                    <tr><td>end_at</td><td>string</td><td>No</td><td>게시 종료 일시 (DateTime)</td></tr>
                    <tr><td>popup_start_at</td><td>string</td><td>No</td><td>팝업 노출 시작 일시</td></tr>
                    <tr><td>popup_end_at</td><td>string</td><td>No</td><td>팝업 노출 종료 일시</td></tr>
                </table>
            </div>
        </div>
    """
    if '<h3>공지사항 관리 (Notices)</h3>' not in html:
        html = html.replace('<section id="log-api">', notice_api_html + '\n    <section id="log-api">')

    # 4. Update Logs API response
    html = html.replace(
        '"action": "CONTENT_ACCESS"',
        '"action_type": "CONTENT_ACCESS",\n                        "target_entity": "Contents",\n                        "target_id": "content_001",\n                        "before_value": null,\n                        "after_value": null'
    )
    html = html.replace(
        '"targetId": "content_001",',
        ''
    )
    html = html.replace(
        '"details": "Started playing promotional video"',
        ''
    )

    with open('api.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done applying ERD updates to api.html")

update_api()
