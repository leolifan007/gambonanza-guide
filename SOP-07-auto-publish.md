# SOP 07 (v3): 自动发布流程

## 概述
本文档定义了完全自动化的内容发布流程。文章按预设日期自动发布，并自动出现在首页 Latest Guides 区域。

## 前置条件
- GitHub 仓库 `content-polishing` 分支已创建
- GitHub Actions `scheduled-release.yml` 已配置
- Cloudflare Pages 已连接 `content-polishing` 分支
- `layouts/partials/latest-articles.html` 动态卡片 partial 存在
- `layouts/index.html` 已调用 `{{ partial "latest-articles.html" . }}`

## 发布机制

### 触发方式
1. **自动触发**（定时）：GitHub Actions 按 schedule 运行
   - 每天 09:11 CST（01:11 UTC）
   - 周一三五 13:48 CST（05:48 UTC）
   - 周二四 17:23 CST（09:23 UTC）
2. **手动触发**：GitHub Actions → workflow_dispatch → `scheduled-release.yml`

### 等待发布的文章标记

```yaml
---
title: "文章标题"
hidden: true      # ← 关键标记：控制发布
publishDate: "2026-06-06"  # ← 指定发布日期（可选）
draft: true       # ← 可以加，脚本会自动移除
---
```

- **`hidden: true`** 是发布触发器。脚本扫描到 `hidden: true` + `publishDate <= today` 的文章就会自动发布
- **`publishDate`** 可选。不设置则立即发布；设置后到指定日期才发布
- **`draft: true`** 可选。脚本会自动移除

## 自动发布流程（全部自动化）

### Step 1: GitHub Actions 触发
- 按 `scheduled-release.yml` 的 cron 表达式定时触发
- 或通过 workflow_dispatch 手动触发

### Step 2: 同步分支
工作流先同步 `content-polishing` 和 `main` 分支，防止分叉导致冲突。

### Step 3: auto-publish.py 执行
Python 脚本扫描 `content/` 目录下所有 `.md` 文件：

1. 查找 `hidden: true` + `publishDate <= today` 的文章
2. 移除 `hidden: true`
3. 移除 `publishDate` 字段
4. 移除 `draft: true`
5. 添加 `date` 字段（用 publishDate 的值，或今天）
6. 更新 `lastmod` 为当前时间
7. `git add content/` → `git commit --no-verify` → `git push`

### Step 4: Hugo 站点重建
```bash
hugo --minify
```
自动重新生成整个站点。

### Step 5: 部署
工作流通过 `peaceiris/actions-gh-pages@v4` 部署到 gh-pages 分支。
Cloudflare Pages 读取 `content-polishing` 分支自动构建部署。

### Step 6: 首页卡片自动更新

**核心机制**：首页 Latest Guides 区域使用 `layouts/partials/latest-articles.html`（Hugo 动态 partial），**不修改 `layouts/index.html`**。

```go
// latest-articles.html 的核心逻辑
{{- $pages := where .Site.RegularPages "Draft" "==" false -}}  // 过滤草稿
{{- $pages = where $pages "Params.hidden" "!=" true -}}        // 过滤隐藏文章
{{/* 按日期排序，取最新 12 篇 */}}
{{- $latest := first 12 (sort ...) -}}
```

- 新文章发布后，Hugo 构建时会自动出现在 Latest Guides 区
- **不需要手动修改 `index.html`**
- 自动排序（按日期降序）
- 14 天内的文章自动带 `NEW` 标签
- 分类（Boss/Economy/Gambits/Pieces 等）自动从 front matter `category` 字段识别

### Step 7: 推送回 content-polishing
工作流将更新的 `layouts/index.html`（如有变化）推回 `content-polishing`。

### Step 8: 合并到 main
工作流将 `content-polishing` 合并回 `main` 分支。

## 文件清单

| 文件 | 作用 |
|------|------|
| `.github/workflows/scheduled-release.yml` | GitHub Actions 定时配置 |
| `.github/scripts/auto-publish.py` | 自动发布 Python 脚本 |
| `layouts/partials/latest-articles.html` | 首页动态卡片 partial |
| `layouts/index.html` | 首页模板（调用 latest-articles.html） |

## 验证

发布后可验证：

1. **文章是否公开**：访问 `https://gambonanzaguide.com/<slug>/` — 文章应正常显示
2. **首页 Latest Guides**：新文章出现在列表中，按日期倒序排列
3. **NEW 标签**：14 天内发布的文章带 `<span class="new-badge">NEW</span>`
4. **日期显示**：显示 front matter 中的 `date` 字段
5. **分类标签**：显示 `category` 字段对应的标签
6. **GitHub 提交**：确认 `auto-publish.py` 执行了 `git commit` + `git push`
7. **Cloudflare Pages**：确认部署成功（无 502 等错误）

## 常见问题排查

### auto-publish.py 找不到文章
```
[auto-publish] No articles to publish today.
```
- 检查文章是否有 `hidden: true`
- 检查 `publishDate` 是否 <= 今天
- 检查文章文件名是否以 `.md` 结尾

### Git commit 失败
- 本地 pre-commit hook 可能拒绝非 ASCII 字符
- 解决方法：运行 `git commit --no-verify` 或删除 `.git/hooks/pre-commit`
- GitHub Actions 上没有此限制

### 首页不显示新文章
- 确认 `layouts/partials/latest-articles.html` 存在
- 确认 `layouts/index.html` 调用了 `{{ partial "latest-articles.html" . }}`
- Hugo 构建需要重新运行

## 注意事项

1. **使用 `hidden: true` 标记待发布文章**
2. **`publishDate` 格式**：`"YYYY-MM-DD"`（带引号）
3. **`category` 字段**决定首页分类标签：boss/economy/gambit/piece/beginner
4. **不要硬编码首页卡片**——修改 `layouts/index.html` 添加新卡片不会自动更新，改用 `latest-articles.html` partial
5. **脚本在 commit 时加 `--no-verify`**——防止 pre-commit hook 干扰
6. **分支同步逻辑**：merge 失败时自动尝试 rebase，防止分支分叉
7. **Cloudflare Pages** 需要 2-3 分钟部署，且使用 `content-polishing` 分支
