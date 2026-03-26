const fs = require('fs');
const path = require('path');
const os = require('os');

const appData = process.env.APPDATA || path.join(os.homedir(), 'AppData', 'Roaming');
const dirsToTry = [
    path.join(appData, 'Code', 'User', 'History'),
    path.join(appData, 'Code - Insiders', 'User', 'History')
];

let historyDir = '';
for (const dir of dirsToTry) {
    if (fs.existsSync(dir)) {
        historyDir = dir;
        break;
    }
}

if (!historyDir) {
    fs.writeFileSync('search_result.txt', 'History directory not found');
    process.exit(0);
}

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
        let resource = data.resource;
        if (resource) {
            if (typeof resource === 'string') {
                resource = decodeURIComponent(resource.replace('file:///', ''));
            }
            entryMap.set(path.dirname(entryFile), resource);
        }
    } catch (e) {}
});

const found = [];
allFiles.forEach(file => {
    if (file.endsWith('.json')) return;
    try {
        const content = fs.readFileSync(file, 'utf8');
        for (const s of searchStrings) {
            if (content.indexOf(s) !== -1) {
                const dir = path.dirname(file);
                const original = entryMap.get(dir) || 'Unknown';
                // push if not already in found
                if (!found.find(f => f.file === file)) {
                    found.push({ file, original });
                }
            }
        }
    } catch (e) {}
});

fs.writeFileSync('search_result.txt', JSON.stringify(found, null, 2));