import json

with open('CMS-webpage/wireframe_site/content-versions.html', 'r', encoding='utf-8') as f:
    html = f.read()

res = {
    'changeStatusModal': 'id="changeStatusModal"' in html,
    'viewModal': 'id="viewModal"' in html,
    'simulateDownload_btn': 'onclick="simulateDownload' in html,
    'changeStatus_btn': 'openChangeStatusModal(' in html,
    'view_btn': 'openViewModal(' in html
}

with open('log_temp.json', 'w', encoding='utf-8') as f:
    json.dump(res, f, indent=2)
