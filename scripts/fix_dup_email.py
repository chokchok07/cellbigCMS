import re

def fix_auth_register():
    with open('api.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # Define the old block that is currently in the file
    pattern = r'<h4>Parameters \(Body\)</h4>\s*<table>\s*<tr><th>Field</th><th>Type</th><th>Required</th><th>Description</th></tr>\s*<tr><td>username</td><td>string</td><td>Yes</td><td>로그인 ID</td></tr>\s*<tr><td>password</td><td>string</td><td>Yes</td><td>비밀번호</td></tr>\s*<tr><td>email</td><td>string</td><td>Yes</td><td>이메일 \(연락처 및 ID 찾기용\)</td></tr>\s*<tr><td>user_name</td><td>string</td><td>Yes</td><td>유저 이름</td></tr>\s*<tr><td>email</td><td>string</td><td>Yes</td><td>연락처 이메일</td></tr>\s*<tr><td>description</td><td>string</td><td>No</td><td>사용자 계정 정보 \(설명\)</td></tr>\s*</table>'
    
    new_block = """<h4>Parameters (Body)</h4>
                <table>
                    <tr><th>Field</th><th>Type</th><th>Required</th><th>Description</th></tr>
                    <tr><td>login_id</td><td>string</td><td>Yes</td><td>로그인 아이디</td></tr>
                    <tr><td>password</td><td>string</td><td>Yes</td><td>암호화된 계정 비밀번호</td></tr>
                    <tr><td>user_name</td><td>string</td><td>Yes</td><td>유저 이름</td></tr>
                    <tr><td>email</td><td>string</td><td>Yes</td><td>연락처 이메일</td></tr>
                    <tr><td>description</td><td>string</td><td>No</td><td>사용자 계정 정보 (설명)</td></tr>
                </table>"""

    html = re.sub(pattern, new_block, html)

    with open('api.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print("Fixed dup email in auth/register")

fix_auth_register()
