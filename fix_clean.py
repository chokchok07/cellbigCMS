import glob, re

for f in glob.glob('CMS-webpage/wireframe_site/*list.html'):
    if 'notice' in f or 'user' in f or 'serial' in f: continue
    
    text = open(f, 'r', encoding='utf-8').read()
    
    # Remove double onclicks
    text = re.sub(
        r'(onclick=[\'\"](?:location\.href=|window\.location\.href=)[\'\"][^\'\"]*?[\'\"])[\s]*onclick=[\'\"][^\'\"]*[\'\"]',
        r'\1', text
    )

    text = re.sub(
        r'onclick=[\'\"](location\.href=)[\'\"]([^\'\"]*)\.html[\'\"]([^\'\"]*)\.html[\'\"][\'\"]',
        r'onclick=\"\1\'\2.html\'\"', text
    )

    text = re.sub(
        r'onclick="location\.href=\'([^\']*?)\'"([a-zA-Z0-9\-\.]*\.html)[\'\"]',
        r'onclick="location.href=\'\1\'"', text
    )
    
    text = re.sub(
        r'onclick="location\.href=\'([^\']*?)\'"\s*onclick="[^"]*"',
        r'onclick="location.href=\'\1\'"', text
    )

    text = re.sub(
        r'class="(action-btn|btn btn-primary|btn-primary)"onclick',
        r'class="\1" onclick', text
    )

    with open(f, 'w', encoding='utf-8') as file:
        file.write(text)
print('Fixed!')
