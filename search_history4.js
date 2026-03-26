const fs = require('fs');
const path = require('path');

const historyDir = 'C:/Users/user/AppData/Roaming/Code/User/History';

const targetDirs = [];
const allResources = [];
const dirs = fs.readdirSync(historyDir);

for (const dir of dirs) {
    const dirPath = path.join(historyDir, dir);
    if (!fs.statSync(dirPath).isDirectory()) continue;
    const entriesPath = path.join(dirPath, 'entries.json');
    if (fs.existsSync(entriesPath)) {
        try {
            const entriesData = JSON.parse(fs.readFileSync(entriesPath, 'utf-8'));
            if (entriesData.resource) {
                allResources.push(entriesData.resource);
            }
            if (entriesData.resource && entriesData.resource.endsWith('index.html')) {
                if (entriesData.entries) {
                    for (const entry of entriesData.entries) {
                        const filePath = path.join(dirPath, entry.id);
                        if (fs.existsSync(filePath)) {
                            targetDirs.push({ filePath, timestamp: entry.timestamp, content: fs.readFileSync(filePath, 'utf-8') });
                        }
                    }
                }
            }
        } catch (e) {}
    }
}

targetDirs.sort((a, b) => b.timestamp - a.timestamp);

console.log(`Found ${targetDirs.length} versions of index.html`);
if (targetDirs.length > 0) {
    console.log('Most recent length:', targetDirs[0].content.length);
    console.log('Most recent content preview:', targetDirs[0].content.substring(0, 100));
    console.log('CONTENT_START');
    console.log(targetDirs[0].content);
    console.log('CONTENT_END');
}

console.log('Sample resources:', allResources.slice(0, 5));
