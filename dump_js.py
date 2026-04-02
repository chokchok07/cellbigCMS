import re
with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.findall(r'<script>[\s\S]*?<\/script>', text)
with open('DUMP_SCRIPTS.txt', 'w', encoding='utf-8') as f:
    f.write("\n\n=======\n\n".join(m))
