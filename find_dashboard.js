const fs = require('fs');
const path = require('path');

function search(dir) {
    let results = [];
    const files = fs.readdirSync(dir);
    for (const file of files) {
        if (file === 'node_modules' || file === '.git') continue;
        const fullPath = path.join(dir, file);
        try {
            const stat = fs.statSync(fullPath);
            if (stat.isDirectory()) {
                results = results.concat(search(fullPath));
            } else {
                if (path.basename(fullPath) === 'dashboard.html') {
                    results.push(fullPath);
                } else {
                    const content = fs.readFileSync(fullPath, 'utf8');
                    if (content.includes('Welcome, 홍길동')) {
                        results.push(fullPath);
                    }
                }
            }
        } catch (e) {
            // ignore
        }
    }
    return results;
}

const res = search('C:\\\\Users\\\\user\\\\Documents\\\\VSCode\\\\CellbigCMS\\\\CellbigCMS\\\\');
console.log(Array.from(new Set(res)).join('\\n'));
