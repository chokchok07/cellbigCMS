const fs = require('fs');

let text = fs.readFileSync('CMS-webpage/wireframe_site/device-editor.html', 'utf8');
text = text.replace('(Offline)', '(Inactive)');
fs.writeFileSync('CMS-webpage/wireframe_site/device-editor.html', text);

let detail = fs.readFileSync('CMS-webpage/wireframe_site/device-detail.html', 'utf8');
detail = detail.replace(/<span class="status-indicator status-online"><\/span>[\s\n]*Online/g, '<span class="badge active">Active</span>');
fs.writeFileSync('CMS-webpage/wireframe_site/device-detail.html', detail);

let overviewFile = 'CMS-webpage/wireframe_site/overview.html';
if (fs.existsSync(overviewFile)) {
    let overview = fs.readFileSync(overviewFile, 'utf8');
    overview = overview.replace(/Online/g, 'Active');
    overview = overview.replace(/Offline/g, 'Inactive');
    overview = overview.replace(/Idle/g, 'Inactive');
    fs.writeFileSync(overviewFile, overview);
}

let indexFile = 'CMS-webpage/wireframe_site/index.html';
if (fs.existsSync(indexFile)) {
    let indexData = fs.readFileSync(indexFile, 'utf8');
    indexData = indexData.replace(/Online/g, 'Active');
    indexData = indexData.replace(/Offline/g, 'Inactive');
    indexData = indexData.replace(/Idle/g, 'Inactive');
    fs.writeFileSync(indexFile, indexData);
}

console.log('Update finished!');
