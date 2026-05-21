#!/bin/bash
set -e

echo "=== Auto-Publish: Scanning for hidden/draft articles ==="

# Find articles with hidden: true in front matter
HIDDEN_ARTICLES=$(grep -rl "^hidden: true" content/ --include="*.md" 2>/dev/null || true)

if [ -z "$HIDDEN_ARTICLES" ]; then
  echo "No hidden articles found. Nothing to publish."
  exit 0
fi

echo "Found hidden articles:"
echo "$HIDDEN_ARTICLES" | while read -r f; do echo "  - $f"; done

# Randomly select 1 to promote
SELECTED=$(echo "$HIDDEN_ARTICLES" | shuf -n 1)
echo ""
echo "=== Publishing: $SELECTED ==="

# Update front matter: hidden: true -> hidden: false
sed -i 's/^hidden: true/hidden: false/' "$SELECTED"
# Also check and fix draft: true -> draft: false
sed -i 's/^draft: true/draft: false/' "$SELECTED"

# Generate non-round timestamp
MINUTE=$(date +%-M)           # e.g. 23, not 023
RANDOM_OFFSET=$(( (RANDOM % 30) - 15 ))  # +/- 15 minutes
NEW_MINUTE=$(( (10#$MINUTE + RANDOM_OFFSET) % 60 ))
[ "$NEW_MINUTE" -lt 0 ] && NEW_MINUTE=$(( NEW_MINUTE + 60 ))
NEW_MINUTE=$(printf "%02d" "$NEW_MINUTE")
FORMATTED=$(date -u +"%Y-%m-%dT%H:${NEW_MINUTE}:%S+08:00")

# Remove existing lastmod line and add new one
if grep -q "^lastmod:" "$SELECTED"; then
  sed -i "/^lastmod:/d" "$SELECTED"
  # Insert before closing ---
  awk -v ts="$FORMATTED" '{
    print
    if ($0 ~ /^---$/ && inserted == "") {
      print "lastmod: " ts
      inserted = "yes"
    }
  }' "$SELECTED" > "${SELECTED}.tmp" && mv "${SELECTED}.tmp" "$SELECTED"
else
  # No existing lastmod, add before closing ---
  awk -v ts="$FORMATTED" '{
    print
    if ($0 ~ /^---$/ && inserted == "") {
      print "lastmod: " ts
      inserted = "yes"
    }
  }' "$SELECTED" > "${SELECTED}.tmp" && mv "${SELECTED}.tmp" "$SELECTED"
fi

echo "Updated lastmod: $FORMATTED"
echo ""

# Also handle TTL: check if any article has been hidden >7 days
echo "=== TTL Check: Force-publish articles hidden >7 days ==="
CURRENT_EPOCH=$(date +%s)
for f in $HIDDEN_ARTICLES; do
  # Get git last commit timestamp for this file
  FILE_DATE=$(git log -1 --format="%at" -- "$f" 2>/dev/null || echo "0")
  AGE_DAYS=$(( (CURRENT_EPOCH - FILE_DATE) / 86400 ))
  if [ "$AGE_DAYS" -gt 7 ]; then
    echo "  TTL expired for $f ($AGE_DAYS days old) — force publishing"
    sed -i 's/^hidden: true/hidden: false/' "$f"
    # Also update its lastmod
    sed -i "/^lastmod:/d" "$f"
    awk -v ts="$FORMATTED" '{
      print
      if ($0 ~ /^---$/ && inserted == "") {
        print "lastmod: " ts
        inserted = "yes"
      }
    }' "$f" > "${f}.tmp" && mv "${f}.tmp" "$f"
  fi
done

# Commit changes
echo ""
echo "=== Committing changes ==="
git add content/
git commit -m "auto-publish: $(date -u +'%Y-%m-%d %H:%M UTC')" || echo "No content changes"
echo "=== Auto-publish done ==="
