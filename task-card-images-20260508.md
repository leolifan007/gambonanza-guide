# 任务记录 — 2026-05-08 00:41

## 任务
用户提供的 6 张像素风格卡片图替换首页 guide-card SVG 图标。

## 完成的工作

### 图片规格统一
- 提供的 6 张原图尺寸不统一（410-414 × 156-161）
- 用 sharp 统一 resize 到 **414×160**，WebP 格式，quality 85
- 6 张总计 **50.2KB**（对比原 PNG ~750KB）

| 文件名 | 对应页面 | 大小 |
|--------|---------|------|
| beginner.webp | Beginner's Guide | 6.4KB |
| gambits.webp | Gambits | 10.5KB |
| bosses.webp | Bosses | 8.2KB |
| economy.webp | Economy | 9.6KB |
| achievements.webp | Achievements | 7.0KB |
| strategy.webp | Strategy | 8.5KB |

### CSS 响应式改造
- **移除** `.guide-card-image` 在 768px/480px 断点的硬编码高度（100px/80px）
- **改为** `img { width: 100%; height: auto }` 让图片自然撑高，保持 414:160 比例
- **移除** 旧的 `.guide-card-image svg.outline-svg` 规则
- **移除** 6 个 `:nth-child()` 渐变背景（图片自带深色背景）
- 保留 `image-rendering: pixelated` 确保像素图标锐利

### 模板更新
- `themes/gambonanza-theme/layouts/index.html`：6 处 `<svg>` → `<img src="images/cards/xxx.webp" width="414" height="160">`

### 清理
- 删除 `static/images/cards/*.png`（8 个冗余 PNG，不再需要）
- 删除 `cards.webp` / `faq.webp`（第一版 831×128 的错误裁切）

### 部署
- main 分支：Hugo 源文件已更新
- gh-pages 分支：构建并推送（commit 1dc59ad）
- 网址：https://leolifan007.github.io/gambonanza-guide/

## 关键教训
- **用户裁图更精准**：只保留图标区域，不带底部文字标签
- **响应式原则**：永远不用硬编码高度限制图片容器，用 `width:100% + height:auto` 让图片自然撑高
- **移动优先**：MEMORY.md 已有完整守则，每次改 CSS 必须检查三个断点（1024/768/480）

## 待完成
- 用户反馈页面效果后可能还需微调线框尺寸
