import re

def update_device_detail():
    path = "CMS-webpage/wireframe_site/device-detail.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Update Buttons (Edit Device -> Save)
    content = content.replace(
        '<button class="btn btn-secondary" onclick="location.href=\'device-editor.html\'">Edit Device</button>',
        '<button class="btn btn-primary" onclick="if(confirm(\'수정 내용을 저장하시겠습니까?\')) { alert(\'수정되었습니다.\'); }">Save</button>'
    )
    content = content.replace(
        '<button class="btn btn-secondary" style="color:#dc2626; border-color:#fca5a5;" onclick="showDeleteModal()">Delete Device</button>',
        '<button class="btn btn-secondary" style="color:#dc2626; border-color:#fca5a5;" onclick="showDeleteModal()">Delete</button>'
    )

    # 2. Convert Basic Info to inputs
    # MAC
    content = content.replace(
        '<div class="info-value" style="color: #111827; background: #f3f4f6; padding: 6px 12px; border-radius: 6px; min-height: 20px; font-family: monospace;">00:1A:2B:3C:4D:5E</div>',
        '<input type="text" class="input" style="width:100%; font-family:monospace" value="00:1A:2B:3C:4D:5E">'
    )
    # Store
    content = content.replace(
        '<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;"><a href="store-detail.html" style="color:#2563eb;text-decoration:none">Store-01 (Main)</a>, Store-02</div>',
        '''<select class="input" style="width:100%;">
                  <option value="store-01" selected>Store-01 (Main)</option>
                  <option value="store-02">Store-02</option>
                </select>'''
    )
    # Products (Optional/Removed or left as select for logic)
    content = content.replace(
        '<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;">CMS Player, Content Viewer</div>',
        '''<input type="text" class="input" style="width:100%" value="CMS Player, Content Viewer">'''
    )
    
    # Tags
    content = re.sub(
        r'<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Tags:</div>.*?<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;"><span class="badge".*?</div>',
        '<div class="info-label" style="font-weight: 600; color: #4b5563; text-align: right; padding-top: 4px;">Name:</div>\n                <input type="text" class="input" style="width:100%" value="Device-A">',
        content,
        flags=re.DOTALL
    )

    # Convert Meta to inputs
    meta_replacements = [
        ('Intel Core i7-12700', 'CPU', 'Intel Core i7-12700'),
        ('NVIDIA RTX 3060', 'GPU', 'NVIDIA RTX 3060'),
        ('16GB', 'RAM', '16GB'),
        ('450 GB', 'Disk Free', '450 GB'),
        ('Windows 10 Pro IoT', 'OS', 'Windows 10 Pro IoT'),
        ('1920x1080', 'Resolution', '1920x1080')
    ]
    
    for old_val, label, default in meta_replacements:
        content = re.sub(
            rf'<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;">{old_val}</div>',
            rf'<input type="text" class="input" style="width:100%" value="{default}">',
            content
        )

    # 3. Compress Installed Packages
    # Replace Right Column: Installed packages div structure to add scroll
    content = content.replace(
        '<div class="card">\n              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px">\n                <h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px; width: 100%;">📦 설치된 패키지</h2>\n              </div>',
        '<div class="card" style="display:flex; flex-direction:column;">\n              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px">\n                <h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; padding-bottom: 12px; width: 100%;">📦 설치된 패키지</h2>\n              </div>\n              <div style="flex:1; overflow-y:auto; max-height:400px; padding-right:8px; margin-bottom:16px;">'
    )
    
    # After the packages, close the scrollable div.
    # We find the end of the package list:
    content = content.replace(
        '''onclick="location.href='package-detail.html'">View Package</button>\n              </div>\n            </div>''',
        '''onclick="location.href='package-detail.html'">View Package</button>\n              </div>\n            </div>\n            </div>'''
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

update_device_detail()
