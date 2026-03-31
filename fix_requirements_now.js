const fs = require('fs');
const path = require('path');

const listPath = path.join(__dirname, 'CMS-webpage/wireframe_site/content-list.html');
const detailPath = path.join(__dirname, 'CMS-webpage/wireframe_site/content-detail.html');

// 1. Fix content-list.html
let listText = fs.readFileSync(listPath, 'utf-8');
listText = listText.replace(/onclick="openContentViewModal\(this\)"/g, `onclick="location.href='content-detail.html'"`);

// Remove modal
listText = listText.replace(/<!-- Content View Modal -->[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\s*<\/div>/, '');

fs.writeFileSync(listPath, listText);

// 2. Fix content-detail.html
let detailText = fs.readFileSync(detailPath, 'utf-8');
detailText = detailText.replace(/🎬 Content Detail/g, '🎬 콘텐츠 상세정보');
detailText = detailText.replace(/View or Edit Content/g, '콘텐츠의 상세 정보를 확인하고 수정합니다');

// Extract versionsSection
const versionsRegex = /(<div class="card" id="versionsSection"[\s\S]*?<!-- Right Column -->\s*<div style="[^\"]*">)/;

const match = detailText.match(versionsRegex);
if(match) {
    let extracted = match[1];
    
    // remove it from original place
    // wait, we need carefully split it. 
    // it's better to use cheerio or just simple string replacements.
}
