import os

def update_notice_list():
    base_dir = r"CMS-webpage\wireframe_site"
    path = os.path.join(base_dir, 'notice-list.html')
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    # headers
    html = html.replace('<th>Type</th>', '<th>Importance</th>')
    
    # row data
    html = html.replace('<td><span class="badge" style="background:#e0f2fe;color:#1e3a8a">Info</span></td>', '<td><span class="badge" style="background:#e0f2fe;color:#1e3a8a">NORMAL</span></td>')
    html = html.replace('<td><span class="badge" style="background:#fef3c7;color:#9a3412">Update</span></td>', '<td><span class="badge" style="background:#fef3c7;color:#9a3412">URGENT</span></td>')
    html = html.replace('<td><span class="badge" style="background:#fee2e2;color:#991b1b">Warning</span></td>', '<td><span class="badge" style="background:#fee2e2;color:#991b1b">URGENT</span></td>')
    
    html = html.replace('<td>All Devices</td>', '<td>ALL (DASHBOARD)</td>')
    html = html.replace('<td>Specific Stores</td>', '<td>STORE (POPUP)</td>')
    
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Updated notice-list.html")

update_notice_list()