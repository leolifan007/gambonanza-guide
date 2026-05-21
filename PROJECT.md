# Gambonanza Guide 项目运维手册

## 网站信息
- **网址**: https://gambonanzaguide.com/
- **仓库**: https://github.com/leolifan007/gambonanza-guide
- **主分支**: main
- **内容分支**: content-polishing

## GitHub Actions 部署自动化

### 工作流文件
- `.github/workflows/scheduled-release.yml` - 定时自动发布

### 触发方式
1. **手动触发 (需要 gh CLI 登录)**:
   ```powershell
   gh run workflow dispatch scheduled-release.yml -f ref=main
   ```

2. **手动网页触发**:
   - 打开 https://github.com/leolifan007/gambonanza-guide/actions
   - 点击 scheduled-release → Run workflow → Branch: main → Run

### 自动触发规则
- Schedule: 非整点随机时间 (09:11, 13:48, 17:23 CST)
- workflow_dispatch: 支持手动

## gh CLI 认证

需要 GitHub CLI 登录后才能远程触发部署：

```powershell
gh auth login
# 流程:
# 1. GitHub.com → HTTPS
# 2. 登录浏览器 → 已授权设备
# 3. 建议也勾选 "SSH密钥" 用于 git 操作
```

登录后可以用:
```powershell
gh run list --repo leolifan007/gambonanza-guide        # 查看最近部署
gh run view <run-id> --log                      # 查看构建日志
```

## 代码修改后手动部署流程

```powershell
# 1. 确保在 main 分支
git checkout main

# 2. 修改内容/样式后提交
git add .
git commit -m "描述改动"

# 3. 推送到 origin main
git push origin main

# 4. 触发部署 (需要 gh CLI 登录后)
gh run workflow dispatch scheduled-release.yml -f ref=main

# 5. 或者网页触发: https://github.com/leolifan007/gambonanza-guide/actions
```

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

最后更新: 2026-05-21