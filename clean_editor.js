const fs = require('fs');

const path = 'CMS-webpage/wireframe_site/content-editor.html';
let t = fs.readFileSync(path, 'utf8');

// The section is something like <div class="card" id="initialUploadSection"> ... </div></div>
// Let's use string manipulation rather than risky regex
const start = t.indexOf('<div class="card" id="initialUploadSection"');
if(start !== -1) {
    // Find the next card or end of list. Usually initialUploadSection is before Package Usages.
    const end = t.indexOf('<!-- Package Usages (Read only view) -->');
    if(end !== -1) {
        t = t.substring(0, start) + t.substring(end);
        fs.writeFileSync(path, t);
        console.log('Removed initialUploadSection');
    } else {
        const nextCard = t.indexOf('<div class="card"', start + 50);
        if(nextCard !== -1) {
            t = t.substring(0, start) + t.substring(nextCard);
            fs.writeFileSync(path, t);
            console.log('Removed initialUploadSection (fallback to next card)');
        }
    }
}
