import re

def check_users():
    with open('api.html', 'r', encoding='utf-8') as f:
        html = f.read()

    match = re.search(r'(<span class="path">/users</span>.*?</table>)', html, re.DOTALL)
    if match:
        print(match.group(1))

check_users()
