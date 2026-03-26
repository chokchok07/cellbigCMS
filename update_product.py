import re

def update_product_detail():
    path = "CMS-webpage/wireframe_site/product-detail.html"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Change Edit to Save
    content = content.replace(
        '<button class="btn btn-secondary">Edit</button>',
        '<button class="btn btn-primary" onclick="if(confirm(\'수정 내용을 저장하시겠습니까?\')) { alert(\'수정되었습니다.\'); }">Save</button>'
    )
    content = content.replace('style="color:#dc2626; border-color:#fca5a5;">Delete</button>', 'style="color:#dc2626; border-color:#fca5a5;" onclick="showDeleteModal()">Delete</button>')

    # Basic Info to Inputs
    content = content.replace(
        '<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;">SandCraft</div>',
        '<input type="text" class="input" style="width:100%" value="SandCraft">'
    )
    # Convert Description
    content = content.replace(
        '<div class="info-value" style="color: #111827; background: #f9fafb; padding: 6px 12px; border-radius: 6px; min-height: 20px;">샌드크래프트 제품군</div>',
        '<textarea class="input" style="width:100%; height:60px; resize:vertical;">샌드크래프트 제품군</textarea>'
    )
    
    # Compress right column (Contents Section)
    content = content.replace(
        '<div class="card" style="margin-bottom:20px">\n              <h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 12px;">📝 포함된 콘텐츠 (8)</h2>\n              <table class="section-table">',
        '<div class="card" style="display:flex; flex-direction:column; margin-bottom:20px;">\n              <h2 style="font-size: 18px; color: #111827; margin-top: 0; margin-bottom: 12px;">📝 포함된 콘텐츠 (8)</h2>\n              <div style="flex:1; overflow-y:auto; max-height:400px; padding-right:8px;">\n              <table class="section-table">'
    )
    # Close the new div
    content = content.replace(
        '</tbody>\n              </table>\n            </div> <!-- Close Content Card div -->',
        '</tbody>\n              </table>\n              </div>\n            </div> <!-- Close Content Card div -->'
    )

    # Compress Left column (Packages section)
    content = content.replace(
        '<div class="card" style="margin-bottom:20px">\n              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">\n                <h2 style="font-size: 18px; color: #111827; margin:0">📦 연결된 패키지 <span id="packageCount">(3)</span></h2>\n                <button type="button" class="btn btn-primary" onclick="openPackageSelectionModal()">+ Add Package</button>\n              </div>\n          <table class="section-table">',
        '<div class="card" style="display:flex; flex-direction:column; margin-bottom:20px;">\n              <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px">\n                <h2 style="font-size: 18px; color: #111827; margin:0">📦 연결된 패키지 <span id="packageCount">(3)</span></h2>\n                <button type="button" class="btn btn-primary" onclick="openPackageSelectionModal()">+ Add Package</button>\n              </div>\n              <div style="flex:1; overflow-y:auto; max-height:400px; padding-right:8px;">\n          <table class="section-table">'
    )
    content = content.replace(
        '            </tbody>\n          </table>\n            </div> <!-- Close Package Section div -->',
        '            </tbody>\n          </table>\n              </div>\n            </div> <!-- Close Package Section div -->'
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

update_product_detail()