import re

def main():
    filepath = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site\store-list.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # match Edit buttons
    content = re.sub(r'<button class="btn-action"[^>]*>Edit</button>\n\s*', '', content)

    # replace Delete with Inactive
    content = content.replace('<button class="btn-action btn-danger">Delete</button>', '<button  class="btn-action" style="color:#059669;border-color:#059669" onclick="openStatusModal(\'active\')">Active</button>')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Python execution Done")

if __name__ == '__main__':
    main()