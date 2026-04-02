const fs = require('fs');
let html = fs.readFileSync('CMS-webpage/wireframe_site/content-editor.html', 'utf8');

html = html.replace(/<div id="newVersionModal"[\s\S]*?<\/form>\s*<\/div>\s*<\/div>/, '');
html = html.replace(/function openNewVersionModal\(\)[\s\S]*?\}/, '');
html = html.replace(/function closeNewVersionModal\(\)[\s\S]*?\}/, '');
html = html.replace(/function submitNewVersion\(\)[\s\S]*?\n\s*\}/, '');

fs.writeFileSync('CMS-webpage/wireframe_site/content-editor.html', html, 'utf8');
