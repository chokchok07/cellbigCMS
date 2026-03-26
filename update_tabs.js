const fs = require('fs');
const file = 'CMS-webpage/wireframe_site/device-list.html';
let html = fs.readFileSync(file, 'utf8');

const tabsHtml = `
        <div style="margin-bottom: 20px; border-bottom: 1px solid #e5e7eb; display: flex; gap: 24px;">
            <div style="padding-bottom: 8px; font-weight: 600; color: #3b82f6; border-bottom: 2px solid #3b82f6; cursor: pointer;">전체 (All)</div>
            <div style="padding-bottom: 8px; font-weight: 500; color: #6b7280; cursor: pointer;">네트워크형 (Online)</div>
            <div style="padding-bottom: 8px; font-weight: 500; color: #6b7280; cursor: pointer;">스탠드얼론 (Offline)</div>
        </div>
`;

if (!html.includes('네트워크형 (Online)')) {
    html = html.replace('<div class="table-card">', tabsHtml + '\n        <div class="table-card">');
    fs.writeFileSync(file, html);
    console.log('Tabs added to device-list.html');
}
