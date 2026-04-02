import re

def enlarge_modal():
    with open('CMS-webpage/wireframe_site/package-detail.html', 'r', encoding='utf-8') as f:
        html = f.read()

    # 1. Update the modal container style
    if '<div class="modal"' in html:
        # replace any inline style width with the huge one
        new_html = re.sub(
            r'(<div class="modal")[^>]*>',
            r'\1 style="width: 1400px; max-width: 95vw; height: 90vh; display: flex; flex-direction: column;">',
            html
        )
        
        # 2. Make sure the content wrapper has scroll limits
        # It's currently `<div class="border rounded px-3 py-2 bg-light">`
        new_html = re.sub(
            r'<div class="border rounded px-3 py-2 bg-light"[^>]*>',
            r'<div class="border rounded px-3 py-2 bg-light" style="flex-grow: 1; overflow-y: auto; overflow-x: hidden; max-height: calc(90vh - 200px); min-height: 400px;">',
            new_html
        )

        with open('CMS-webpage/wireframe_site/package-detail.html', 'w', encoding='utf-8') as f:
            f.write(new_html)
        print("Updated package-detail.html")
    else:
        print("Could not find <div class=\"modal\"")

enlarge_modal()
