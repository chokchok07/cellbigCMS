import re

def update_user_api():
    with open('api.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update the POST /users table
    post_users_old = """<tr><td>username</td><td>string</td><td>Yes</td><td>로그인 ID</td></tr>
                    <tr><td>password</td><td>string</td><td>Yes</td><td>초기 비밀번호</td></tr>
                    <tr><td>fullName</td><td>string</td><td>Yes</td><td>이름</td></tr>
                    <tr><td>role</td><td>string</td><td>Yes</td><td>super_admin | local_manager | store_manager</td></tr>
                    <tr><td>scopeIds</td><td>array</td><td>No</td><td>관리 대상 ID 목록 (지역ID 또는 스토어ID)</td></tr>"""
                    
    post_users_new = """<tr><td>login_id</td><td>string</td><td>Yes</td><td>로그인 아이디</td></tr>
                    <tr><td>password</td><td>string</td><td>Yes</td><td>암호화된 초기 비밀번호</td></tr>
                    <tr><td>user_name</td><td>string</td><td>Yes</td><td>유저 이름</td></tr>
                    <tr><td>email</td><td>string</td><td>Yes</td><td>연락처 이메일</td></tr>
                    <tr><td>description</td><td>string</td><td>No</td><td>사용자 계정 정보 (설명)</td></tr>
                    <tr><td>role</td><td>enum</td><td>Yes</td><td>Super / Operation / Local / Technician</td></tr>
                    <tr><td>scopeIds</td><td>array</td><td>No</td><td>관리 대상 ID 목록 (지역ID 또는 스토어ID)</td></tr>"""

    if "username" in html and "fullName" in html:
        html = html.replace(post_users_old, post_users_new)

    # 2. Update the PUT /users/{userId} table
    # Let's find it using regex
    put_users_old_match = re.search(r'(<span class="path">/users/\{userId\}.*?<h4>Parameters.*?<table>\s*<tr>.*?</tr>)(.*?)(\s*</table>)', html, re.DOTALL)
    if put_users_old_match:
        put_users_new_rows = """
                    <tr><td>user_name</td><td>string</td><td>No</td><td>변경할 유저 이름</td></tr>
                    <tr><td>email</td><td>string</td><td>No</td><td>변경할 연락처 이메일</td></tr>
                    <tr><td>password</td><td>string</td><td>No</td><td>변경할 비밀번호</td></tr>
                    <tr><td>description</td><td>string</td><td>No</td><td>사용자 계정 정보 (설명) 수정</td></tr>
                    <tr><td>role</td><td>enum</td><td>No</td><td>역할 권한 (Super / Operation / Local / Technician)</td></tr>
                    <tr><td>scopeIds</td><td>array</td><td>No</td><td>관리할 지역(LocalArea) 또는 스토어 ID 목록</td></tr>
                    <tr><td>status</td><td>enum</td><td>No</td><td>계정 상태 (Active, Suspended)</td></tr>"""
        html = html[:put_users_old_match.start(2)] + put_users_new_rows + html[put_users_old_match.end(2):]

    # 3. Update User Response Example in GET /users
    res_old = """"userId": "u1",
      "username": "manager_seoul",
      "role": "local_manager","""
    res_new = """"user_id": "u1",
      "login_id": "manager_seoul",
      "user_name": "서울 관리자",
      "email": "manager_seoul@example.com",
      "description": "서울 지역 총괄 관리자 계정",
      "role": "Local","""
    html = html.replace(res_old, res_new)
    
    # And there's also the /auth/me or similar, let's just do a blind replace for login_id, user_name
    html = html.replace('"username": "manager_seoul"', '"login_id": "manager_seoul",\n      "user_name": "서울 관리자",\n      "email": "manager_seoul@example.com"')
    html = html.replace('"fullName": "김관리",', '"description": "테스트 계정입니다.",')
    
    with open('api.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("User ERD synced")

update_user_api()
