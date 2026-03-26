import io

fp = "CMS-webpage/wireframe_site/product-editor.html"
with io.open(fp, 'r', encoding='utf-8') as f:
    html = f.read()

# Since product-editor wasn't fixed by the previous value match, let's fix it properly using re
import re

html = re.sub(
    r'<input type="text" class="input" style="width:100%" id="productName" maxlength="100"\s*value="">',
    '<input type="text" class="input" style="width:100%" id="productName" maxlength="100" value="" placeholder="예: 샌드크래프트 (SandCraft)">',
    html
)
html = re.sub(
    r'<input type="text" class="input" style="width:100%" id="productName" value="">',
    '<input type="text" class="input" style="width:100%" id="productName" value="" placeholder="예: 샌드크래프트 (SandCraft)">',
    html
)
html = re.sub(
    r'<textarea class="input" style="width:100%; height:80px; resize:vertical;" id="description"></textarea>',
    '<textarea class="input" style="width:100%; height:80px; resize:vertical;" id="description" placeholder="예: 아이들이 모래를 만지며 즐길 수 있는 AR 인터랙티브 제품입니다."></textarea>',
    html
)

with io.open(fp, 'w', encoding='utf-8') as f:
    f.write(html)
print("fixed product editor placeholder")
