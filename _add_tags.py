# -*- coding: utf-8 -*-
"""Add tags front matter to all article markdown files in content/.

Keyword matching based on title + category. Skips _index, privacy, contact.
Writes UTF-8 without BOM. ASCII-safe only.
"""
import os
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")

CONTENT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "content")

# keyword groups -> tag name (checked in order, first match wins per group)
KEYWORD_TAGS = [
    (["economy", "stock", "farm", "shop", "investment", "money"], "Economy"),
    (["gambit"], "Gambits"),
    (["boss"], "Bosses"),
    (["seed"], "Seeds"),
    (["pawn"], "Pawns"),
    (["knight"], "Knights"),
    (["rook"], "Rooks"),
    (["bishop"], "Bishops"),
    (["queen"], "Queens"),
    (["card", "piece"], "Pieces & Cards"),
    (["beginner", "how to play", "rules", "start", "first 3 turns", "first runs"], "Beginner"),
    (["difficulty", "easy", "progress"], "Difficulty"),
    (["walkthrough", "step-by-step"], "Walkthrough"),
    (["tier", "meta", "build", "archetype", "ranked", "rating"], "Meta & Builds"),
    (["achievement"], "Achievements"),
    (["collection", "unlock"], "Collection"),
    (["combo", "chain", "synergy", "loop", "cycle", "combination"], "Combos & Synergy"),
    (["recovery", "salvage", "mistake", "emergency", "crashing", "backfired",
      "survive", "die", "lose", "lost", "wrong"], "Recovery & Mistakes"),
    (["crumble"], "Crumble Mode"),
    (["board", "4x4", "6x6", "8x8", "tile", "space"], "Board & Tiles"),
    (["tip", "trick", "tricks"], "Tips"),
    (["strategy", "tactics", "sacrifice", "win rate", "decision"], "Strategy"),
    (["endgame", "final", "closing", "post-boss", "stage 4"], "Endgame"),
]

SKIP = {"_index", "privacy", "contact"}


def extract_category(text):
    """Return category value from front matter (singular `category:` key)."""
    m = re.search(r"(?m)^category:\s*[\"']?(.+?)[\"']?\s*$", text[:2000])
    if m:
        return m.group(1).strip().strip('"').strip("'")
    return None


def pick_tags(title, category):
    """Return 1-4 tags for an article."""
    tags = []
    low = title.lower()
    for keywords, tag in KEYWORD_TAGS:
        for kw in keywords:
            if kw in low:
                if tag not in tags:
                    tags.append(tag)
                break
    if category:
        cat_tag = category.replace(" & ", " & ").strip()
        if cat_tag not in tags:
            tags.insert(0, cat_tag)
    # cap at 4
    return tags[:4]


def insert_tags(text, tags):
    """Insert `tags:` block before the `title:` line in front matter."""
    idx = text.find("title:")
    if idx < 0 or idx > 3000:
        return None
    line_start = text.rfind("\n", 0, idx) + 1
    block = "tags:\n" + "".join('  - "%s"\n' % t for t in tags)
    return text[:line_start] + block + text[line_start:]


def main():
    changed = 0
    skipped = 0
    for fname in sorted(os.listdir(CONTENT_DIR)):
        if not fname.endswith(".md"):
            continue
        slug = fname[:-3]
        if slug in SKIP:
            skipped += 1
            continue
        path = os.path.join(CONTENT_DIR, fname)
        with open(path, "r", encoding="utf-8") as f:
            text = f.read()
        if re.search(r"(?m)^tags:", text[:2000]):
            print("SKIP (already has tags): %s" % fname)
            skipped += 1
            continue
        title_m = re.search(r"(?m)^title:\s*[\"']?(.+?)[\"']?\s*$", text[:2000])
        title = title_m.group(1) if title_m else fname
        category = extract_category(text)
        tags = pick_tags(title, category)
        if not tags:
            tags = ["Strategy"]
        new_text = insert_tags(text, tags)
        if new_text is None:
            print("WARN no title found: %s" % fname)
            skipped += 1
            continue
        with open(path, "w", encoding="utf-8", newline="\n") as f:
            f.write(new_text)
        print("OK %s -> tags=%s (cat=%s)" % (fname, tags, category))
        changed += 1
    print("done: %d changed, %d skipped" % (changed, skipped))


if __name__ == "__main__":
    main()
