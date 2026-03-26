import re

def update_package_detail():
    path = "CMS-webpage/wireframe_site/package-detail.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Edit -> Save
    content = content.replace(
        '<button class="btn btn-secondary" onclick="editPackage()">Edit Package</button>',
        '<button class="btn btn-primary" onclick="if(confirm(\'수정 내용을 저장하시겠습니까?\')) { alert(\'수정되었습니다.\'); }">Save</button>'
    )
    
    # Product Select
    content = content.replace(
        '<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;"><a href="product-detail.html" style="color:#2563eb;text-decoration:none">SandCraft (product-sandcraft)</a></div>',
        '<select class="input" style="width:100%;"><option value="product-sandcraft" selected>SandCraft</option><option value="product-fish">FishWorld</option></select>'
    )
    
    # Name Input
    content = content.replace(
        '<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;">SandCraft - 11 Items</div>',
        '<input type="text" class="input" style="width:100%" value="SandCraft - 11 Items">'
    )
    
    # Description Input
    content = content.replace(
        '<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;">샌드크래프트 기본 11종 콘텐츠 패키지</div>',
        '<textarea class="input" style="width:100%; height:60px; resize:vertical;">샌드크래프트 기본 11종 콘텐츠 패키지</textarea>'
    )
    
    # Status Select
    content = content.replace(
        '<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;"><span class="status-badge status-published">Published</span></div>',
        '<select class="input" style="width:100%;"><option value="published" selected>Published</option><option value="draft">Draft</option></select>'
    )
    
    # Scrollable Target Devices
    content = content.replace(
        '<div class="card" style="margin-bottom: 24px;">\n              <div class="card-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">\n                <h2 style="font-size: 18px; color: #111827; margin: 0;">💻 배포 대상 디바이스 (45)</h2>\n                <button class="btn btn-outline" onclick="openAssignDeviceModal()">+ Assign Devices</button>\n              </div>\n              <div class="table-container">\n                <table class="data-table">',
        '<div class="card" style="margin-bottom: 24px; display:flex; flex-direction:column;">\n              <div class="card-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">\n                <h2 style="font-size: 18px; color: #111827; margin: 0;">💻 배포 대상 디바이스 (45)</h2>\n                <button class="btn btn-outline" onclick="openAssignDeviceModal()">+ Assign Devices</button>\n              </div>\n              <div style="flex:1; overflow-y:auto; max-height:400px;">\n              <div class="table-container">\n                <table class="data-table">'
    )
    content = content.replace(
        '</tbody>\n                </table>\n              </div>\n              <div style="margin-top: 16px; text-align: center;">\n                <button class="btn btn-outline">View All Devices</button>\n              </div>\n            </div>',
        '</tbody>\n                </table>\n              </div>\n              </div>\n              <div style="margin-top: 16px; text-align: center;">\n                <button class="btn btn-outline">View All Devices</button>\n              </div>\n            </div>'
    )
    
    # Contents layout change: if it exists
    content = content.replace(
        '<div class="card" style="margin-bottom: 24px;">\n              <div class="card-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">\n                <h2 style="font-size: 18px; color: #111827; margin: 0;">🎬 포함된 콘텐츠 (11)</h2>\n                <button class="btn btn-outline" onclick="manageContents()">Manage Contents</button>\n              </div>\n              <div class="list-container">',
        '<div class="card" style="margin-bottom: 24px; display:flex; flex-direction:column;">\n              <div class="card-header" style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px;">\n                <h2 style="font-size: 18px; color: #111827; margin: 0;">🎬 포함된 콘텐츠 (11)</h2>\n                <button class="btn btn-outline" onclick="manageContents()">Manage Contents</button>\n              </div>\n              <div style="flex:1; overflow-y:auto; max-height:400px; padding-right:8px;">\n              <div class="list-container">'
    )
    # the end of list-container inside package-detail
    content = re.sub(
        r'(</div>\n\s*</div>\n\s*<!-- List Item 4.*?</div>\n\s*</div>)',
        r'\1\n              </div>',
        content,
        flags=re.DOTALL
    ) 

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

update_package_detail()
