const fs = require('fs');
const filepath = 'CMS-webpage/wireframe_site/content-list.html';
let text = fs.readFileSync(filepath, 'utf8');

// View Button
text = text.replace(/onclick=".*?(?:openContentViewModal.*?|content-detail\.html).*?"/g, 'onclick="window.location.href=\'content-editor.html\'"');

// New Button
text = text.replace(/onclick="openNewContentModal\(\)"/g, 'onclick="window.location.href=\'content-create.html\'"');

fs.writeFileSync(filepath, text);
console.log('Fixed list links!');
