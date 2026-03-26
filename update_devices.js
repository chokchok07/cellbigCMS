const fs = require('fs');
const file = 'CMS-webpage/wireframe_site/device-list.html';
let html = fs.readFileSync(file, 'utf8');

// Update Select Options
html = html.replace(/<option value="Online">.*?<\/option>/g, '<option value="Active">Active</option>');
html = html.replace(/<option value="Idle">.*?<\/option>/g, '<option value="Inactive">Inactive</option>');
html = html.replace(/<option value="Offline">.*?<\/option>/g, '');

// Update Badges
html = html.replace(/<span class="badge badge-online">[\s\S]*?<\/span>[ \t]*\([\s\S]*?\)/g, '<span class="badge active">Active</span>');
html = html.replace(/<span class="badge badge-idle">[\s\S]*?<\/span>[ \t]*\([\s\S]*?\)/g, '<span class="badge inactive">Inactive</span>');
html = html.replace(/<span class="badge badge-error">[\s\S]*?<\/span>[ \t]*\([\s\S]*?\)/g, '<span class="badge inactive">Inactive</span>');
html = html.replace(/<span class="badge badge-offline">[\s\S]*?<\/span>[ \t]*\([\s\S]*?\)/g, '<span class="badge inactive">Inactive</span>');

fs.writeFileSync(file, html);
console.log('device-list.html updated successfully.');
