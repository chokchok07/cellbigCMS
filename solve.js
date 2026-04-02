const fs = require('fs');
let list = fs.readFileSync('CMS-webpage/wireframe_site/content-list.html', 'utf8');
let editor = fs.readFileSync('CMS-webpage/wireframe_site/content-editor.html', 'utf8');
let detail = fs.readFileSync('CMS-webpage/wireframe_site/content-detail.html', 'utf8');

console.log('--- OUTPUT START ---');
console.log('List links to Editor?', list.includes('content-editor.html'));
console.log('List links to Detail?', list.includes('content-detail.html'));
console.log('Editor includes name?', editor.includes('name'));
console.log('Detail includes content_nm (kr)?', detail.includes('콘텐츠 이름') || detail.includes('콘텐츠명'));
console.log('Editor h1:', editor.match(/<h1.*?>.*?<\/h1>/)?.[0]);
console.log('Detail h1:', detail.match(/<h1.*?>.*?<\/h1>/)?.[0]);
console.log('--- OUTPUT END ---');
