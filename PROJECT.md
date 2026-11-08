# Gambonanza Guide 项目运维手册

## 网站信息
- **网址**: https://gambonanzaguide.com/
- **仓库**: https://github.com/leolifan007/gambonanza-guide
- **主分支**: main

## GitHub Actions 部署（现行唯一链路）

- 唯一工作流：`.github/workflows/deploy.yml`，push 到 `main` 时自动执行 `hugo --minify`，并用 peaceiris/actions-gh-pages 把 `./public` 部署到 gh-pages。
- **定时自动发布已彻底弃用并删除（2026-11-08）**：`scheduled-release.yml`、`auto-publish.py` / `.sh`、`content-polishing` 分支流程、`.github/README-AUTO-PUBLISH.md` 均已移除。不要再配置、引用或建议启用。
- 上线方式：QA 通过后由人工一次性提交源码并 `git push origin main`，**不排期、不分批、不等定时**。

### 部署流程

```powershell
# 1. 确保在 main 分支
git checkout main

# 2. 只暂存源码（不要 git add .，避免把 public/ 带进去）
git add content/ static/ hugo.toml layouts/
git commit -m "描述改动"

# 3. 推送即自动部署
git push origin main
```

部署由 CI 自动触发，无需手动操作。推送后用 `gh run list --limit 3` 确认 `Deploy to GitHub Pages` success，再拉取线上 sitemap / 首页复核。
**只提交源码，不提交 `public/`**：仓库里跟踪的 `public/` 是历史产物，CI 不读取它。

## 文章管理

### 最近文章更新 (2026-05-21)
| 文章 | 路径 | 状态 |
|-------|------|------|
| 4x4 Fast Farm Guide v1.2.0 | content/4x4-fast-farm-guide.md | 已发布 |
| Gambit Chain Recovery | content/gambit-chain-recovery-guide.md | hidden |
| Piece Sacrifice | content/piece-sacrifice-guide.md | hidden |
| Economy Recovery | content/economy-recovery-guide.md | hidden |

### 待深化文章排期
- 5/22: Queen Supremacy Guide
- 5/24: 完成推送
- 5/25: Tile Control Guide
- 5/27: 完成推送
- 5/29: Blitzking Guide
- 6/1: 完成推送

## 主题样式修改

- 样式文件: `themes/gambonanza-theme/static/css/style.css`
- 常用修改: 
  - 子标题 h3: 当前 14px，正文字体
  - 底部版权: 居中，无边框

---

最后更新: 2026-11-08
