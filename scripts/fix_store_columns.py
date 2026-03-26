import re

def fix_store_list_columns():
    file_path = 'CMS-webpage/wireframe_site/store-list.html'
    
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # 이미 배지(Open/Closed)가 있는 애들 뒤에 불필요하게 들어간 '-' 빈칸 제거
    # <td><span class="badge badge-online">Open</span></td>
    # <td><span style="color:#9ca3af">-</span></td> <- 이거 제거
    
    html = re.sub(
        r'(<span class="badge[^>]+>[^<]+</span></td>\s*)<td><span style="color:#9ca3af">-</span></td>',
        r'\1',
        html
    )

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(html)

if __name__ == '__main__':
    fix_store_list_columns()
    print("Store list fixed.")
