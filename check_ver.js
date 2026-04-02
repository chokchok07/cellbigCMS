const fs = require('fs');

const dlist = fs.readFileSync('CMS-webpage/wireframe_site/device-list.html', 'utf-8');
const clist = fs.readFileSync('CMS-webpage/wireframe_site/content-list.html', 'utf-8');

console.log('Device list has Ver:', dlist.includes('Ver</button>'));
console.log('Content list has Ver:', clist.includes('Ver</button>'));
