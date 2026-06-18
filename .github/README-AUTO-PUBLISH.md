# 自动发布流程

## 工作原理

1. **GitHub Actions cron 触发** `scheduled-release.yml`
   - 每天 09:11 CST (01:11 UTC) 检查一次
   - 工作日 13:48 / 17:23 补充检查
   - 支持手动触发 (`workflow_dispatch`)

2. **工作流程**：
   - Checkout `content-polishing` 分支
   - Merge `main` 到 `content-polishing`
   - 运行 `auto-publish.py`：扫描所有 `hidden: true` + `publishDate <= today` 的文章 → 解除隐藏
   - 重新构建 Hugo（确认站点正常）
   - 部署到 gh-pages
   - Push `content-polishing` 分支
   - Merge `content-polishing` 到 `main`

3. **文章发布条件**：
   - 前端：`hidden: true`
   - 发布日期：`publishDate: "YYYY-MM-DD"`
   - 当 `publishDate <= today` 时自动发布

## 已发现的 bug 和修复

### Bug 1: REPO_DIR 路径错误 (已修复)
- `auto-publish.py` 中 `REPO_DIR` 计算少了一层 `dirname`
- 原来：`.github/scripts/` → `.github/`
- 正确：`.github/scripts/` → `.github/` → `repo-root/`
- 修复：增加一个 `os.path.dirname()` 调用

### Bug 2: Cron 不支持周末 (已修复)
- 原来 cron 只跑工作日（`1-5`），但 `pawn-economy-loop.md` 定在周六发布
- 修复：增加每天 09:11 CST 的 cron（`11 1 * * *`）

### Bug 3: 卡片变成"长条" (已修复)
- `layouts/index.html` 的 "Latest Guides" 部分缺少 `<div class="latest-articles">` 包装器
- 修复：还原到 d692cd9 版本（硬编码卡片）

## 剩余文章

| 文件 | publishDate | 星期 | 状态 |
|------|-------------|------|------|
| gambit-synergy-chains.md | 2026-05-30 | 周六 | ✅ 已发布 |
| comeback-zero-stock.md | 2026-06-01 | 周一 | ⏳ 等待 |
| jester-boss-guide.md | 2026-06-03 | 周三 | ⏳ 等待 |
| pawn-economy-loop.md | 2026-06-06 | 周六 | ⏳ 等待 |

## 注意事项

- 新文章添加到 `content-polishing` 分支时，确保：
  1. 文件在 `content/` 目录
  2. 前端添加 `hidden: true`
  3. 前端添加 `publishDate: "YYYY-MM-DD"`
  4. 同时合并到 `main` 分支（文章不显示，因为 `hidden: true`）
- 避免在文章中使用 em-dash (`—`)、emojis 等非 ASCII 字符（Windows GBK 下乱码）
