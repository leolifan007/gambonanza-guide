const fs = require('fs');
const f = 'C:\\Users\\ROG\\.qclaw\\workspace-agent-d2068023\\projects\\gambonanza-guide\\themes\\gambonanza-theme\\layouts\\index.html';
let c = fs.readFileSync(f, 'utf8');
c = c.replace(/width="831" height="128"/g, 'width="414" height="160"');
fs.writeFileSync(f, c, 'utf8');
console.log('img dims updated');
