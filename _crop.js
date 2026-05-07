const sharp = require('sharp');
const path = require('path');
const fs = require('fs');

const src = 'C:\\Users\\ROG\\.qclaw\\media\\inbound\\paste_1778170578513_s8ent4.png';
const outDir = 'C:\\Users\\ROG\\.qclaw\\workspace-agent-d2068023\\projects\\gambonanza-guide\\static\\images\\cards';
const tmpDir = 'C:\\Users\\ROG\\.qclaw\\workspace-agent-d2068023\\projects\\gambonanza-guide\\tmp';

fs.mkdirSync(outDir, { recursive: true });
fs.mkdirSync(tmpDir, { recursive: true });

const names = ['beginner','gambits','bosses','economy','achievements','cards','strategy','faq'];

async function cropAll() {
    const meta = await sharp(src).metadata();
    console.log(`Source: ${meta.width}x${meta.height} ${meta.format}`);
    
    const cw = Math.floor(meta.width / 2);   // cell width
    const ch = Math.floor(meta.height / 4);  // cell height
    console.log(`Grid: 2x4, cell=${cw}x${ch}`);

    // First pass: save ALL 8 full cells to tmp/ for inspection
    for (let row = 0; row < 4; row++) {
        for (let col = 0; col < 2; col++) {
            const idx = row * 2 + col;
            const x = col * cw, y = row * ch;
            const tmpPath = path.join(tmpDir, `${names[idx]}_full.png`);
            await sharp(src)
                .extract({ left: x, top: y, width: cw, height: ch })
                .png()
                .toFile(tmpPath);
        }
    }
    
    console.log('\nFull cells saved to tmp/');
    
    // Read one cell (beginner) as raw pixel data to analyze the dark region
    const { data, info } = await sharp(path.join(tmpDir, 'beginner_full.png'))
        .raw()
        .toBuffer({ resolveWithObject: true });
    
    const { width, height, channels } = info;
    console.log(`\nAnalyzing beginner cell: ${width}x${height} ch=${channels}`);
    
    // Find dark region boundaries by scanning from edges inward
    // Dark = RGB sum < threshold (screen is dark theme)
    const DARK_THRESHOLD = 200;
    
    // Find top boundary
    let top = 0;
    for (let y = 0; y < height; y++) {
        let darkCount = 0;
        for (let x = Math.floor(width * 0.2); x < Math.floor(width * 0.8); x++) {
            const idx = (y * width + x) * channels;
            const sum = data[idx] + data[idx + 1] + data[idx + 2];
            if (sum < DARK_THRESHOLD) darkCount++;
        }
        if (darkCount > (width * 0.3)) { top = y; break; }
    }
    
    // Find bottom boundary (scan upward from 80% height to find text line)
    let bottom = height - 1;
    let textTop = 0;
    // First, find where text starts by looking for light area below dark
    for (let y = Math.floor(height * 0.5); y < height; y++) {
        let lightCount = 0;
        for (let x = Math.floor(width * 0.1); x < Math.floor(width * 0.9); x++) {
            const idx = (y * width + x) * channels;
            const sum = data[idx] + data[idx + 1] + data[idx + 2];
            if (sum > 350) lightCount++; // text is bright
        }
        if (lightCount > 40) { textTop = y; break; }
    }
    bottom = textTop > 0 ? textTop - 4 : Math.floor(height * 0.78);
    
    // Find left boundary
    let left = 0;
    for (let x = 0; x < Math.floor(width * 0.3); x++) {
        let darkCount = 0;
        for (let y = Math.floor(height * 0.1); y < Math.floor(height * 0.7); y++) {
            const idx = (y * width + x) * channels;
            const sum = data[idx] + data[idx + 1] + data[idx + 2];
            if (sum < DARK_THRESHOLD) darkCount++;
        }
        if (darkCount > 10) { left = x; break; }
    }
    
    // Find right boundary
    let right = width - 1;
    for (let x = width - 1; x > Math.floor(width * 0.7); x--) {
        let darkCount = 0;
        for (let y = Math.floor(height * 0.1); y < Math.floor(height * 0.7); y++) {
            const idx = (y * width + x) * channels;
            const sum = data[idx] + data[idx + 1] + data[idx + 2];
            if (sum < DARK_THRESHOLD) darkCount++;
        }
        if (darkCount > 10) { right = x; break; }
    }
    
    // Apply to all 8 cells with conservative margins (crop tighter to the icon)
    // The dark area contains the icon + some padding. We want just the icon portion.
    // Let's add 10px margin to ensure we capture the full icon
    const cropLeft = Math.max(0, left + 5);
    const cropTop = Math.max(0, top - 5);
    const cropWidth = Math.min(cw - cropLeft, (right - left) + 20);
    const cropHeight = Math.min(ch - cropTop, (bottom - top) + 15);
    
    console.log(`\nDetected dark area: [${left},${top},${right},${bottom}]`);
    console.log(`Crop params (with margins): left=${cropLeft} top=${cropTop} w=${cropWidth} h=${cropHeight}`);
    
    // Second pass: crop the dark area from each cell and save as WebP
    let totalSize = 0;
    for (let row = 0; row < 4; row++) {
        for (let col = 0; col < 2; col++) {
            const idx = row * 2 + col;
            const x = col * cw + cropLeft;
            const y = row * ch + cropTop;
            
            // Ensure we don't go out of bounds
            const extractW = Math.min(cropWidth, meta.width - x);
            const extractH = Math.min(cropHeight, meta.height - y);
            
            const outPathWebp = path.join(outDir, `${names[idx]}.webp`);
            const outPathPng = path.join(outDir, `${names[idx]}.png`);
            
            // Save as WebP
            await sharp(src)
                .extract({ left: x, top: y, width: extractW, height: extractH })
                .webp({ quality: 85 })
                .toFile(outPathWebp);
            
            // Also save as PNG for comparison
            await sharp(src)
                .extract({ left: x, top: y, width: extractW, height: extractH })
                .png({ compressionLevel: 9, palette: true })
                .toFile(outPathPng);
            
            const webpStat = fs.statSync(outPathWebp);
            const pngStat = fs.statSync(outPathPng);
            totalSize += webpStat.size;
            console.log(`${names[idx]}: ${extractW}x${extractH} | webp=${(webpStat.size/1024).toFixed(1)}KB | png=${(pngStat.size/1024).toFixed(1)}KB`);
        }
    }
    
    console.log(`\nTotal WebP: ${(totalSize/1024).toFixed(1)}KB`);
}

cropAll().catch(e => { console.error(e); process.exit(1); });
