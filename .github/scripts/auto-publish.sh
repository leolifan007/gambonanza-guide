#!/bin/bash
# SOP 08 定时发布脚本
# 按 publishDate 判断到期文章，到期后自动发布

set -e

echo "=== SOP 08 Auto-Publish: Checking for due articles ==="

# 获取当前日期（ISO 格式）
CURRENT_DATE=$(date +%Y-%m-%d)
CURRENT_EPOCH=$(date +%s)

# 扫描所有 hidden: true 且有 publishDate 的文章
DUE_ARTICLES=$(grep -l "^hidden: true" content/*.md 2>/dev/null || true)

if [ -z "$DUE_ARTICLES" ]; then
  echo "No hidden articles found. Nothing to publish."
  exit 0
fi

echo "Found hidden articles, checking publishDate..."

# 检查每篇文章的 publishDate 是否已到期
SELECTED_ARTICLE=""
for article in $DUE_ARTICLES; do
  # 提取 publishDate（格式: 2026-05-25）
  PUBLISH_DATE=$(grep "^publishDate:" "$article" | sed 's/.*publishDate: *"\([^"]*\)".*/\1/' | cut -d'T' -f1)
  
  if [ -z "$PUBLISH_DATE" ]; then
    # 没有 publishDate，跳过
    continue
  fi
  
  # 比较日期
  PUBLISH_EPOCH=$(date -d "$PUBLISH_DATE" +%s 2>/dev/null || echo "0")
  
  if [ "$PUBLISH_EPOCH" -le "$CURRENT_EPOCH" ]; then
    echo "  -> $article is due (publishDate: $PUBLISH_DATE)"
    SELECTED_ARTICLE="$article"
    break  # 只发布一篇
  fi
done

if [ -z "$SELECTED_ARTICLE" ]; then
  echo "No articles due for publication today."
  exit 0
fi

echo ""
echo "=== Publishing: $SELECTED_ARTICLE ==="

# 1. 将 hidden: true 改为 hidden: false
sed -i 's/^hidden: true/hidden: false/' "$SELECTED_ARTICLE"

# 2. 删除 publishDate 字段（发布后不再需要）
sed -i '/^publishDate:/d' "$SELECTED_ARTICLE"

# 3. 生成非整点时间戳更新 lastmod
MINUTE=$(date +%-M)
RANDOM_OFFSET=$(( (RANDOM % 30) - 15 ))
NEW_MINUTE=$(( (10#$MINUTE + RANDOM_OFFSET) % 60 ))
[ "$NEW_MINUTE" -lt 0 ] && NEW_MINUTE=$(( NEW_MINUTE + 60 ))
NEW_MINUTE=$(printf "%02d" "$NEW_MINUTE")
FORMATTED=$(date -u +"%Y-%m-%dT%H:${NEW_MINUTE}:%S+08:00")

# 更新 lastmod
if grep -q "^lastmod:" "$SELECTED_ARTICLE"; then
  sed -i "/^lastmod:/d" "$SELECTED_ARTICLE"
fi
awk -v ts="$FORMATTED" '{
  print
  if ($0 ~ /^---$/ && inserted == "") {
    print "lastmod: " ts
    inserted = "yes"
  }
}' "$SELECTED_ARTICLE" > "${SELECTED_ARTICLE}.tmp" && mv "${SELECTED_ARTICLE}.tmp" "$SELECTED_ARTICLE"

echo "Updated: hidden=false, removed publishDate, lastmod=$FORMATTED"

# 4. 提交更改
echo ""
echo "=== Committing changes ==="
git add "$SELECTED_ARTICLE"
git commit -m "auto-publish: $(basename "$SELECTED_ARTICLE") - $(date -u +'%Y-%m-%d %H:%M UTC')" || echo "No content changes"

echo "=== Auto-publish done ==="
