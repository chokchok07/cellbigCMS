import json
import re

def update_api_html():
    with open('api.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Update Devices Register Request Body
    old_system_info = r"<tr><td>systemInfo</td><td>object</td><td>No</td><td>OS 버전, CPU, RAM 등 시스템 정보</td></tr>"
    new_system_info = """<tr><td>meta</td><td>object</td><td>No</td><td>디바이스 최초 실행 시 자동 수집되는 하드웨어 사양 정보 JSON (CPU모델명, RAM 용량, GPU 모델명, 디스크 여유공간, OS버전, 해상도 등)</td></tr>
                      <tr><td>storeId</td><td>array[string]</td><td>Yes</td><td>할당할 스토어 고유 ID 목록 (2개 이상 입력 가능)</td></tr>
                      <tr><td>productId</td><td>array[string]</td><td>No</td><td>관련 상품 ID 목록 (2개 이상 입력 가능)</td></tr>"""
    html = html.replace(old_system_info, new_system_info)

    # Update Users API (Add loginId, etc if missing)
    # We will just do a generic replace for user schema if we found it.
    
    # Save back
    with open('api_updated.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Done")

update_api_html()
