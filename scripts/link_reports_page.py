import os

# Define the target directory and the string to replace
target_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'CMS-webpage', 'wireframe_site')
target_string = '<div class="sidebar-item">📈 Reports</div>'
target_string_active = '<div class="sidebar-item active">📈 Reports</div>' # Just in case it existed somewhere differently

# Walk through the directory
for root, dirs, files in os.walk(target_dir):
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            
            # Read the file content
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Determine the replacement string
            if file == 'report-content-usage.html':
                # For the report page itself, make it active
                # The user said they already hardcoded it in report-content-usage.html, 
                # but to be safe and consistent as requested:
                # "Replaces it with: <div class="sidebar-item {active_class}" data-page="report-content-usage.html">📈 Reports</div>"
                # If the user already hardcoded it, we might find the new string there already.
                # But let's check for the old string first.
                replacement_string = '<div class="sidebar-item active" data-page="report-content-usage.html">📈 Reports</div>'
            else:
                # For other pages, regular link
                replacement_string = '<div class="sidebar-item" data-page="report-content-usage.html">📈 Reports</div>'
            
            # Perform the replacement
            if target_string in content:
                new_content = content.replace(target_string, replacement_string)
                
                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated: {file}")
            elif target_string_active in content and file != 'report-content-usage.html':
                 # Handle case where it might have been active (unlikely for Reports content unless it was copy pasted)
                new_content = content.replace(target_string_active, replacement_string)
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated (was active): {file}")
            else:
                print(f"Skipped (target not found or already updated): {file}")

