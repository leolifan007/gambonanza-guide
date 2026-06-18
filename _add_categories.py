"""Add category field to all article frontmatter."""
import os, re

CONTENT_DIR = r"C:\Users\ROG\.qclaw\workspace-x74fgmx0vyb8p5is\gambonanza-guide\content"

# Mapping: filename (without extension) -> category
CATEGORIES = {
    # Beginner
    "beginner": "beginner",
    "how-to-play": "beginner",
    "tips": "beginner",
    "faq": "beginner",
    "10-common-mistakes": "beginner",
    
    # Gambits
    "gambits": "gambits",
    "afks-gambit-guide": "gambits",
    "enigmas-gambit-guide": "gambits",
    "gambit-synergy-chains": "gambits",
    "gambit-chain-recovery-guide": "gambits",
    "deterministic-gambits-guide": "gambits",
    "combo-chain-guide": "gambits",
    
    # Boss Battles
    "bosses": "boss",
    "boss-strategy-guide": "boss",
    "jester-boss-guide": "boss",
    "blitzking-boss-guide": "boss",
    "king-of-spades-guide": "boss",
    "queen-supremacy-guide": "boss",
    
    # Economy
    "economy": "economy",
    "pawn-economy-loop": "economy",
    "come-back-zero-stock": "economy",
    "economy-recovery-guide": "economy",
    "4x4-fast-farm-guide": "economy",
    "recommended-seeds": "economy",
    "best-seeds": "economy",
    
    # Pieces & Cards
    "cards": "pieces",
    "master-the-knight-guide": "pieces",
    "rook-gambit-build-guide": "pieces",
    "knight-rush-opener": "pieces",
    "piece-sacrifice-guide": "pieces",
    "rook-bishop-guide": "pieces",
    "pawn-promotion-sustainability-guide": "pieces",
    "tile-control-guide": "pieces",
    "crumble-mechanic-guide": "pieces",
    
    # Strategy
    "strategy": "strategy",
    "complete-walkthrough": "strategy",
    "gambonanza-tier-list": "strategy",
    "endgame-killer-tips": "strategy",
    "decision-framework-guide": "strategy",
    "board-size-strategy": "strategy",
    "pick-right-build-archetype": "strategy",
    "3-simple-habits-win-rate": "strategy",
    "5-emergency-strategies-salvage": "strategy",
    "stop-making-5-mistakes": "strategy",
    "achievements": "strategy",
}

# Don't add to utility pages
SKIP_FILES = {"contact", "privacy", "tactical-sacrifice-guide", "test"}

CATEGORY_LABELS = {
    "beginner": "Beginner",
    "gambits": "Gambits",
    "boss": "Boss Battles",
    "economy": "Economy",
    "pieces": "Pieces & Cards",
    "strategy": "Strategy & Guides",
}

COUNT = 0
for fname in os.listdir(CONTENT_DIR):
    if not fname.endswith(".md"):
        continue
    slug = fname[:-3]
    if slug in SKIP_FILES:
        continue
    if slug not in CATEGORIES:
        print(f"  SKIP: {fname} (no category mapping)")
        continue
    
    fpath = os.path.join(CONTENT_DIR, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()
    
    cat = CATEGORIES[slug]
    label = CATEGORY_LABELS[cat]
    
    # Check if category already exists in frontmatter
    if re.search(r'^category:\s*', content, re.MULTILINE):
        # Update existing
        content = re.sub(
            r'^category:\s*.*$',
            f'category: "{label}"',
            content,
            count=1,
            flags=re.MULTILINE
        )
        action = "UPDATED"
    else:
        # Add after title (after the first --- line)
        # Find the second ---
        parts = content.split("---", 2)
        if len(parts) >= 3:
            parts[1] = f'category: "{label}"\n' + parts[1]
            content = "---".join(parts)
            action = "ADDED"
        else:
            print(f"  SKIP: {fname} (no frontmatter)")
            continue
    
    with open(fpath, "w", encoding="utf-8") as f:
        f.write(content)
    COUNT += 1
    print(f"  {action}: {fname} -> {label}")

print(f"\nDone. Updated {COUNT} articles.")
