import re

with open('schema.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Add product_id to tb_content
target = '<tr><td><span class="pk">content_id</span></td><td><span class="type-badge">VARCHAR(50)</span></td><td>PK</td><td>콘텐츠 고유 식별자</td></tr>'
replacement = r"""<tr><td><span class="pk">content_id</span></td><td><span class="type-badge">VARCHAR(50)</span></td><td>PK</td><td>콘텐츠 고유 식별자</td></tr>
            <tr><td><a href="#tb-product" class="fk-link" style="color:var(--pk-color);">🔗 product_id</a></td><td><span class="type-badge">VARCHAR(50)</span></td><td>FK</td><td>연결할 제품 ID</td></tr>"""

text = text.replace(target, replacement)

# Update ERD for Product and Content
erd_target = 'tb_product ||--o{ tb_package : "defines"'
erd_replacement = """tb_product ||--o{ tb_package : "defines"
    tb_product ||--o{ tb_content : "owns"""

text = text.replace(erd_target, erd_replacement)

with open('schema.html', 'w', encoding='utf-8') as f:
    f.write(text)
print("Updated schema.html")
