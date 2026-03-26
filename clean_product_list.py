import re
import glob

def clean_action_btns():
    for filepath in glob.glob("CMS-webpage/wireframe_site/*-list.html"):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        content = re.sub(
            r'\s*<button class="action-btn">Edit</button>',
            '',
            content,
            flags=re.IGNORECASE
        )
        content = re.sub(
            r'\s*<button class="action-btn">Del</button>',
            '',
            content,
            flags=re.IGNORECASE
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)

clean_action_btns()
