const fs = require('fs');

// ==== 1. Fix content-list.html ====
const listPath = 'CMS-webpage/wireframe_site/content-list.html';
let listText = fs.readFileSync(listPath, 'utf8');

// remove content view modal
listText = listText.replace(/<!-- Content Detail View Modal -->[\s\S]*?(?=<script>)/, '');
listText = listText.replace(/function openContentViewModal[\s\S]*?function closeContentViewModal[\s\S]*?}/, '');

// replace View buttons 
listText = listText.replace(/onclick="openContentViewModal\(this\)"/g, 'onclick="window.location.href=\'content-editor.html?id=101\'"');

fs.writeFileSync(listPath, listText);
console.log('List patched');

// ==== 2. Fix content-editor.html ====
const editPath = 'CMS-webpage/wireframe_site/content-editor.html';
let editText = fs.readFileSync(editPath, 'utf8');

// Find h1 Title and give it an ID if it doesn't have one
editText = editText.replace(/<h1 class="page-title">.*?<\/h1>/, '<h1 class="page-title" id="pageMainTitle">🎬 Content Editor</h1>');

// Move versionsSection to Right Column
const versionsRegex = /<div class="card" id="versionsSection" style="display:none;">[\s\S]*?<\/div>\s*<\/div>\s*<\/div>\n/;
const match = editText.match(versionsRegex);

if (match) {
    let extracted = match[0];
    editText = editText.replace(versionsRegex, '');
    
    // Insert into Right Column at the top
    const rightColPattern = /(<!-- Right Column -->\s*<div style="[^"]*">)/;
    editText = editText.replace(rightColPattern, '$1\n\n            <!-- Moved Versions Section -->\n' + extracted);
}

// Modify JS so that Detail Mode sets Title and "Create New Content" mode doesn't
const jsRegex = /if \(isEditMode\) {[\s\S]*?(?=function generateContentId)/;
const jsMatch = editText.match(jsRegex);

if (jsMatch) {
    let jsBlock = jsMatch[0];
    
    // Change Title and Desc
    const newTitles = `
      // Set to Detail View Mode texts
      const pageMainTitle = document.getElementById('pageMainTitle');
      if(pageMainTitle) pageMainTitle.textContent = '🎬 콘텐츠 상세정보';
      document.getElementById('pageMode').textContent = '콘텐츠의 상세 정보를 확인하고 수정합니다';
`;
    
    // Replace the default pageMode logic
    jsBlock = jsBlock.replace(/document\.getElementById\('pageMode'\)\.textContent = 'Edit: Content ' \+ urlParams\.get\('id'\);/, newTitles);
    
    editText = editText.replace(jsRegex, jsBlock);
}

fs.writeFileSync(editPath, editText);
console.log('Editor patched');
