# SOP 07 (v2): 自动发布流程

## 概述
本文档定义了完全自动化的内容发布流程，确保文章发布后自动出现在首页 Latest Guides 区域。

## 前置条件
- Hugo 已安装
- GitHub Actions 已配置
- content-polishing 分支已创建

## 发布机制

### 触发方式
1. **自动触发**：GitHub Actions 按 schedule 运行（见 scheduled-release.yml）
2. **手动触发**：GitHub Actions workflow_dispatch

### 等待发布的文章标记
```yaml
---
title: "文章标题"
hidden: true  # ← 这是关键标记
---
```

注意：使用 `hidden: true`，不是 `date` 字段。date 只影响显示，不控制发布。

## 自动发布流程（全部自动化）

### Step 1: GitHub Actions 触发
- 读取 scheduled-release.yml 的 cron 表达式
- 非整点随机时间运行

### Step 2: auto-publish.sh 执行
1. 扫描 content/ 目录下所有 `hidden: true` 的文章
2. 随机选择 1 篇发布
3. 将 `hidden: true` 改为 `hidden: false`
4. 生成非整点时间戳更新 `lastmod`
5. **自动更新 layouts/index.html 的 Latest Guides 卡片**
6. 提交更改

### Step 3: Hugo 站点重建
```bash
hugo --minify
```
这会重新生成整个站点，确保新文章的所有页面正确生成。

### Step 4: 部署
- Actions GH Pages 自动部署 public/ 目录

### Step 5: 推送到主分支
- 将 content-polishing 合并到 main
- 同步 layouts/index.html 的更改

## 首页入口自动更新原理

### auto-publish.sh 的更新逻辑
```bash
# 自动识别文章分类
ARTICLE_CATEGORY="Strategy"  # 默认
if echo "$ARTICLE_TITLE" | grep -qi "boss"; then
  ARTICLE_CATEGORY="Boss"
elif echo "$ARTICLE_TITLE" | grep -qi "economy"; then
  ARTICLE_CATEGORY="Economy"
# ... 其他分类规则

# 生成卡片 HTML
NEW_CARD="<a href=\"${ARTICLE_URL}\" class=\"latest-article-card\">
  <span class=\"new-badge\">NEW</span>
  <div class=\"latest-article-meta\">
    <span class=\"phase-tag phase-mid\">${ARTICLE_CATEGORY}</span>
    <span class=\"date-badge\">${PUB_DATE}</span>
  </div>
  <h3>${ARTICLE_TITLE}</h3>
  <p>${ARTICLE_DESC}</p>
</a>"

# 自动插入到 index.html
sed -i "/<div class=\"latest-articles\">/a\\${NEW_CARD}" layouts/index.html
```

### 分类自动识别规则
| 关键词 | 分类 |
|--------|------|
| boss/kos/blitzking/queen | Boss |
| economy/stock/farm/money | Economy |
| gambit/combo | Gambits |
| piece/queen/rook/bishop/knight/pawn | Pieces |
| crumble/tile/control | Mechanics |
| 其他 | Strategy |

## 文件清单

| 文件 | 作用 |
|------|------|
| `.github/workflows/scheduled-release.yml` | GitHub Actions 触发配置 |
| `.github/scripts/auto-publish.sh` | 自动发布脚本（含首页更新） |
| `layouts/index.html` | 首页模板 |

## 验证

发布后可验证：
1. 访问文章 URL（如 /queen-supremacy-guide/）- 文章已公开
2. 访问首页 - 新文章出现在 Latest Guides 区域，带 NEW 标签
3. 查看 GitHub commit - 确认 index.html 已更新

## 注意事项

1. **不要使用 date 字段控制发布** - 只影响显示，不控制发布
2. **使用 hidden: true 标记待发布文章** - 这是唯一的发布触发器
3. **分类自动识别是基于标题关键词** - 见上文表格
4. **日期显示为发布当天日期** - 由脚本自动生成