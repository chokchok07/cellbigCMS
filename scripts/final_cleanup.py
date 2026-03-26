import re

def final_cleanup():
    with open('api.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # auth/me response (458)
    html = html.replace('"fullName": "시스템 관리자",', '"user_name": "시스템 관리자",\n      "email": "admin@example.com",\n      "description": "최고 관리자 계정입니다.",')
    
    # auth register request table (427)
    html = html.replace('<tr><td>fullName</td><td>string</td><td>Yes</td><td>이름</td></tr>', '<tr><td>user_name</td><td>string</td><td>Yes</td><td>유저 이름</td></tr>\n                    <tr><td>email</td><td>string</td><td>Yes</td><td>연락처 이메일</td></tr>\n                    <tr><td>description</td><td>string</td><td>No</td><td>사용자 계정 정보 (설명)</td></tr>')
    
    # auth me PUT table (482)
    html = html.replace('<tr><td>fullName</td><td>string</td><td>No</td><td>성명 변경 시</td></tr>', '<tr><td>user_name</td><td>string</td><td>No</td><td>유저 이름 변경 시</td></tr>\n                    <tr><td>email</td><td>string</td><td>No</td><td>연락처 이메일 변경 시</td></tr>\n                    <tr><td>description</td><td>string</td><td>No</td><td>사용자 계정 정보 (설명) 변경 시</td></tr>')
    
    # /auth/login req table
    html = html.replace('<tr><td>username</td><td>string</td><td>Yes</td><td>어드민 ID</td></tr>', '<tr><td>login_id</td><td>string</td><td>Yes</td><td>로그인 아이디</td></tr>')
    
    with open('api.html', 'w', encoding='utf-8') as f:
        f.write(html)

final_cleanup()
