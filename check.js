const fs = require('fs');
const text = fs.readFileSync('CMS-webpage/wireframe_site/content-detail.html', 'utf-8');
const v = text.indexOf('id="versionsSection"');
const p = text.indexOf('id="packagesSection"');
console.log('Versions Index:', v, 'Packages Index:', p, 'Is Versions first?:', v < p);
