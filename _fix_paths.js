const fs = require("fs");
const path = require("path");

const publicDir = path.join(__dirname, "public");
const siteRoot = "/gambonanza-guide"; // GitHub Pages repo name

function fixHtml(filePath) {
  let html = fs.readFileSync(filePath, "utf-8");
  const rel = path.relative(publicDir, path.dirname(filePath));
  const depth = rel ? rel.split(path.sep).length : 0;
  const prefix = depth === 0 ? "." : "../".repeat(depth);
  
  // Fix href="/xxx/" style links
  html = html.replace(
    /href="\/([^"]+?)"/g,
    (m, p1) => `href="${prefix}/${p1}"`
  );
  
  // Fix src="/css/..." and src="/images/..." for assets
  html = html.replace(
    /src="\/(css\/|images\/|fonts\/)([^"]+?)"/g,
    (m, p1, p2) => `src="${prefix}/${p1}${p2}"`
  );
  
  fs.writeFileSync(filePath, html, "utf-8");
  console.log(`Fixed: ${filePath} (depth=${depth}, prefix="${prefix}")`);
}

function walk(dir) {
  const files = fs.readdirSync(dir);
  for (const f of files) {
    const full = path.join(dir, f);
    if (fs.statSync(full).isDirectory()) {
      walk(full);
    } else if (f.endsWith(".html")) {
      fixHtml(full);
    }
  }
}

walk(publicDir);
console.log("\nDone fixing paths.");
