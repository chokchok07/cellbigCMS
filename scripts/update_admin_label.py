import os

directory = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'
old_string = '👤 Admin'
new_string = '👤 Admin(SP)'

def update_admin_label():
    print("Updating 'Admin' label to 'Admin(SP)'...")
    count = 0
    file_list = [f for f in os.listdir(directory) if f.endswith('.html')]

    for filename in file_list:
        filepath = os.path.join(directory, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if old_string in content and new_string not in content:
                new_content = content.replace(old_string, new_string)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  Updated {filename}")
                count += 1
            else:
                if new_string in content:
                    print(f"  Already updated: {filename}")
                else:
                    print(f"  String not found in {filename}")

        except Exception as e:
            print(f"  Error processing {filename}: {e}")

    print(f"Finished. Updated {count} files.")

if __name__ == "__main__":
    update_admin_label()
