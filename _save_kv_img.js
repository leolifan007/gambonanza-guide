const sharp = require("sharp");
const fs = require("fs");
const path = require("path");

const src = "C:\\Users\\ROG\\.qclaw\\media\\inbound\\paste_1778174433634_y1lg53.png";
const dst = path.join(__dirname, "static", "images", "hero-bg.webp");

async function main() {
  try {
    const meta = await sharp(src).metadata();
    console.log("Source:", meta.width + "x" + meta.height, meta.format);
    
    const maxW = 1920, maxH = 1080;
    let w = meta.width, h = meta.height;
    if (w > maxW) { h = Math.round(h * maxW / w); w = maxW; }
    if (h > maxH) { w = Math.round(w * maxH / h); h = maxH; }
    
    await sharp(src)
      .resize(w, h, { fit: "inside", withoutEnlargement: true })
      .webp({ quality: 82, alphaQuality: 80 })
      .toFile(dst);
    
    const stats = fs.statSync(dst);
    console.log("Output:", dst, (stats.size / 1024).toFixed(1) + "KB");
  } catch (e) {
    console.error("Error:", e.message);
    process.exit(1);
  }
}

main();
