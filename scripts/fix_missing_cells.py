import re

def fix_missing_cells():
    # 1. LocalArea
    p1 = 'CMS-webpage/wireframe_site/localarea-list.html'
    with open(p1, 'r', encoding='utf-8') as f: html = f.read()
    html = re.sub(
        r'(<td>US</td>\s*)<td><span class="store-count">',
        r'\1<td><span style="color:#9ca3af">-</span></td>\n              <td><span class="store-count">',
        html
    )
    with open(p1, 'w', encoding='utf-8') as f: f.write(html)
    
    # 2. Store
    p2 = 'CMS-webpage/wireframe_site/store-list.html'
    with open(p2, 'r', encoding='utf-8') as f: html = f.read()
    html = re.sub(
        r'(</td>\s*)<td><span class="device-count">',
        r'\1<td><span style="color:#9ca3af">-</span></td>\n              <td><span class="device-count">',
        html
    )
    with open(p2, 'w', encoding='utf-8') as f: f.write(html)
    
    # 3. Device
    p3 = 'CMS-webpage/wireframe_site/device-list.html'
    with open(p3, 'r', encoding='utf-8') as f: html = f.read()
    html = re.sub(
        r'(<td>1 min ago</td>\s*)<td>\s*<button class="btn-action"',
        r'\g<1><td><span style="color:#9ca3af">-</span></td>\n                          <td>\n                              <button class="btn-action"',
        html
    )
    with open(p3, 'w', encoding='utf-8') as f: f.write(html)

if __name__ == '__main__':
    fix_missing_cells()
    print("Cells fixed.")
