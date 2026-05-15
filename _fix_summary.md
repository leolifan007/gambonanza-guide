# Task Summary: Gambonanza Guide 404 + 5项改动修复

**时间**: 2026-05-14 ~22:04
**目标**: 修复首页404并补全5项视觉改动

## 根因分析

**首页404原因**：
1. 之前的5项改动在 `deploy-v2` 分支提交（`d47f33f`），推到了远程 `origin/gh-pages`
2. 但在 compaction 后的新 session 中，我试图重新构建并部署时，误操作了 gh-pages 分支（从本地旧 commit `81131bb` 重建），导致写入了错误的部署（不含完整 public/ 内容）
3. 同时 Python 脚本错误地将源码目录（themes/layouts/content）也删除了

**5项改动未完成的原因**：
1. 原来的 `d47f33f` commit 的 CSS 包含像素字体和 hero 背景，但**包含的是旧版卡片样式**（无渐变深色背景，hex `1a0f1a` 实际是 `rgba(26,15,26,...)` 格式）
2. Google Fonts `Press Start 2P` 引用从未加入 `baseof.html` 的 `<head>` 中
3. lang-bar 从未从 `header.html` 中移除（只移除了 `baseof.html` 中的 hreflang）

## 修复内容

| 编号 | 改动 | 文件 |
|------|------|------|
| 1 | 子页面 hero 背景图 | themes/.../style.css `.page-hero` (hero-bg.webp + 渐变遮罩 + 底部淡出) |
| 2 | 删除 Google Translator lang-bar | layouts/partials/header.html (移除整个 .lang-bar div) |
| 3 | 卡片全热区 + 渐变背景 | themes/.../style.css `.guide-card` (26,15,26 渐变 + absolute a 标签 + 悬停效果) |
| 4 | 像素风格字体 (Press Start 2P) | layouts/_default/baseof.html (+ Google Fonts CDN)、CSS var `--font-display` |
| 5 | 正文不变 | --font-body 保持 Inter |

## 当前状态

- **main 分支**: ✅ 完整源码 + 全部5项改动（commit `2af6a2e`）
- **本地 gh-pages 分支**: ✅ 正确部署文件（commit `ef73ff2`）
- **远程 main/gh-pages**: ⚠️ 因沙箱网络限制，未能 push 成功（Recv failure: Connection was reset / SIGKILL）
- **用户看到**: 网站已恢复，但内容为旧版本（因为远程 gh-pages 还是旧的）

## 待用户操作

```bash
cd ~/.qclaw/workspace-agent-d2068023/projects/gambonanza-guide
git push origin main --force
git push origin gh-pages --force
```

或者手动：
1. GitHub → Settings → Pages → 确保 gh-pages 分支 / (root)
2. 推送 main 到远程后确认

## 备注
- `deploy-v2` 分支已被合并（手动 cherry-pick CSS）
- 所有临时文件和部署脚本已清理
