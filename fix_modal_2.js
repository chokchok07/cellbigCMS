const fs = require('fs');

// list
let t = fs.readFileSync('CMS-webpage/wireframe_site/content-list.html', 'utf8');
t = t.replace(/<!-- Content View Modal -->[\s\S]*?(?=<\/main>)/, '');
t = t.replace(/<div id="contentViewModal"[\s\S]*?(?=<\/main>|<script>)/, '');
fs.writeFileSync('CMS-webpage/wireframe_site/content-list.html', t);

console.log("Cleaned list");
