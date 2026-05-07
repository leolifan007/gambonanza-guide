const fs = require('fs');
const f = 'C:\\Users\\ROG\\.qclaw\\workspace-agent-d2068023\\projects\\gambonanza-guide\\themes\\gambonanza-theme\\layouts\\index.html';
let c = fs.readFileSync(f, 'utf8');

// Replace each guide-card-image div that has an inline style + SVG with a clean img version
const replacements = [
  { name: 'beginner', alt: 'Beginners Guide' },
  { name: 'gambits', alt: 'Gambits Guide' },
  { name: 'bosses', alt: 'Boss Battle Guide' },
  { name: 'economy', alt: 'Stock Market Guide' },
  { name: 'achievements', alt: 'Achievement Guide' },
  { name: 'strategy', alt: 'Advanced Strategy Guide' },
];

// Pattern: <div class="guide-card-image" style="background:..."><svg ...></svg></div>
const pattern = /<div class="guide-card-image"\s+style="[^"]*"><svg[\s\S]*?<\/svg><\/div>/g;

let idx = 0;
c = c.replace(pattern, () => {
  const r = replacements[idx];
  idx++;
  return `<div class="guide-card-image"><img src="images/cards/${r.name}.webp" alt="${r.alt}" loading="lazy" width="831" height="128"></div>`;
});

fs.writeFileSync(f, c, 'utf8');
console.log(`Replaced ${idx} guide-card-image SVGs with WebP imgs`);
