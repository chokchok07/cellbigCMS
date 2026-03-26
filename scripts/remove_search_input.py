import os

directory = r'c:\Users\user\Documents\VSCode\CellbigCMS\CellbigCMS\CMS-webpage\wireframe_site'
search_input_html = '<input class="input" placeholder="🔍 Search..." style="flex:1;max-width:300px">'

def remove_search():
    print("Removing search input from headers...")
    count = 0
    file_list = [f for f in os.listdir(directory) if f.endswith('.html')]

    for filename in file_list:
        filepath = os.path.join(directory, filename)
        
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            if search_input_html in content:
                new_content = content.replace(search_input_html, "")
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"  Updated {filename}")
                count += 1
            else:
                print(f"  Search input not found in {filename} (or slightly different?)")

        except Exception as e:
            print(f"  Error processing {filename}: {e}")

    print(f"Finished. Updated {count} files.")

if __name__ == "__main__":
    remove_search()
