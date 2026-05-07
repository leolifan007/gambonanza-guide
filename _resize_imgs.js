const sharp = require('sharp');
const fs = require('fs');

const srcDir = 'C:\\Users\\ROG\\.qclaw\\media\\inbound\\';
const outDir = 'C:\\Users\\ROG\\.qclaw\\workspace-agent-d2068023\\projects\\gambonanza-guide\\static\\images\\cards\\';

const mapping = [
  { src: 'paste_1778171907449_acwzpe.png', dest: 'beginner.webp' },
  { src: 'paste_1778171996418_qata31.png',   dest: 'gambits.webp' },
  { src: 'paste_1778172008315_jhi41d.png',   dest: 'bosses.webp' },
  { src: 'paste_1778172023178_w8rtwg.png',   dest: 'economy.webp' },
  { src: 'paste_1778172035082_zbybxi.png',   dest: 'achievements.webp' },
  { src: 'paste_1778172049844_q9c852.png',   dest: 'strategy.webp' },
];

const TARGET_W = 414;
const TARGET_H = 160;

(async () => {
  fs.mkdirSync(outDir, { recursive: true });
  let total = 0;
  for (const {src, dest} of mapping) {
    const buf = await sharp(srcDir + src)
      .resize(TARGET_W, TARGET_H, { fit: 'contain', background: { r: 10, g: 18, b: 38, alpha: 1 } })
      .webp({ quality: 85 })
      .toFile(outDir + dest);
    total += buf.size;
    console.log(`${dest}: ${TARGET_W}x${TARGET_H} | ${(buf.size/1024).toFixed(1)}KB`);
  }
  console.log(`\nTotal: ${(total/1024).toFixed(1)}KB`);
})();
