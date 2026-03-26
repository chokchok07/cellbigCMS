const fs = require('fs');
const path = require('path');

const historyDir = 'C:/Users/user/AppData/Roaming/Code/User/History';
const searchStrings = ['Welcome, 홍길동', 'welcome, 홍길동', '환영합니다, 홍길동'];

function walkDir(dir) {
    let results = [];
    try {
        const list = fs.readdirSync(dir);
        list.forEach(file => {
            const fullPath = path.join(dir, file);
            const stat = fs.statSync(fullPath);
            if (stat && stat.isDirectory()) {
                results = results.concat(walkDir(fullPath));
            } else {
                results.push(fullPath);
            }
        });
    } catch (e) {}
    return results;
}

const allFiles = walkDir(historyDir);
const entriesFiles = allFiles.filter(f => f.endsWith('entries.json'));

const entryMap = new Map();
entriesFiles.forEach(entryFile => {
    try {
        const content = fs.readFileSync(entryFile, 'utf8');
        const data = JSON.parse(content);
        const dir = path.dirname(entryFile);
        if (data.resource) {
            // Some versions of VS Code encode resource as an object, others as a string URI
            let resource = data.resource;
            if (typeof resource === 'string') {
                resource = decodeURIComponent(resource.replace('file:///', ''));
            }
            entryMap.set(dir, resource);
        }
    } catch (e) {
    }
});

const found = [];
allFiles.forEach(file => {
    if (file.endsWith('.json')) return; // skip entries.json
    try {
        const content = fs.readFileSync(file, 'utf8');
        if (searchStrings.some(s => content.includes(s))) {
            const dir = path.dirname(file);
            const original = entryMap.get(dir) || 'Unknown';
            found.push({ file, original });
        }
    } catch (e) {
    }
});

console.log(JSON.stringify(found, null, 2));