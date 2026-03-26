import re

def main():
    filepath = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site\localarea-list.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to remove the "Edit" and "Delete" buttons in the actions column.
    # The user says: "View와 Active/Inactive 버튼만 있으면 될거같으니까 수정해줘"
    # Looking at the table, there are different combinations.
    # We can match the entire <td> for actions.
    
    # Let's replace:
    # <button class="btn-action" onclick="editLocalArea('...')">Edit</button>
    content = re.sub(
        r'\s*<button class="btn-action"[^>]*>Edit</button>',
        '',
        content
    )

    # For "Delete" buttons, replace them with "Inactive" button or keep if they already have Active/Inactive.
    # If the row has "bg-green-100" meaning Active, the action could be "Inactive" toggle.
    # If it is inactive, the toggle could be "Active".
    # Wait, some are <button class="btn-action btn-danger">Delete</button>
    content = re.sub(
        r'\s*<button class="btn-action btn-danger">Delete</button>',
        '',
        content
    )

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Done")

if __name__ == '__main__':
    main()
