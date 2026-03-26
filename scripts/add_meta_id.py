import glob, re

files = glob.glob('CMS-webpage/wireframe_site/*-detail.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        t = file.read()
    
    # Give the card containing Metadata or 메타데이터 an ID
    if 'id="metadataSection"' not in t:
        t = re.sub(
            r'<div class="card"(?:\s+style="[^"]*")?>\s*(<h2[^>]*>.*?(?:Metadata|메타데이터).*?</h2>)', 
            r'<div class="card" id="metadataSection">\1', 
            t, 
            flags=re.IGNORECASE
        )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(t)
    print("Done:", f)
