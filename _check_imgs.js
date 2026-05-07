const sharp = require('sharp');
const fs = require('fs');
const dir = 'C:\\Users\\ROG\\.qclaw\\media\\inbound\\';
const files = [
  'paste_1778171907449_acwzpe.png',
  'paste_1778171996418_qata31.png',
  'paste_1778172008315_jhi41d.png',
  'paste_1778172023178_w8rtwg.png',
  'paste_1778172035082_zbybxi.png',
  'paste_1778172049844_q9c852.png',
];
(async () => {
  for (const f of files) {
    const fp = dir + f;
    const m = await sharp(fp).metadata();
    const stat = fs.statSync(fp);
    console.log(f.slice(22,34) + ': ' + m.width + 'x' + m.height + ' | ' + (stat.size/1024).toFixed(1) + 'KB');
  }
})();
