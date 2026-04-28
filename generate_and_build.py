"""muscle-meal-girls 自動記事生成エントリ"""
from __future__ import annotations
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, r"C:\Users\atsus\000_ClaudeCode\007_自動投稿ブログ")
import fitness_auto_post_lib as lib  # noqa: E402

CLAUDE_MD = (HERE / "CLAUDE.md").read_text(encoding="utf-8") if (HERE / "CLAUDE.md").exists() else ""

CFG = {
    "site_dir": HERE,
    "blog_name": "筋トレ女子メシ",
    "site_url": "https://musclelove-777.github.io/muscle-meal-girls",
    "twitter_site": "@MuscleGirlLove7",
    "accent_color": "#4caf50",
    "categories": [
        "高タンパク外食メニュー", "コンビニ筋トレ飯", "自炊レシピ",
        "サプリメント解説", "減量・増量メシ", "コラム",
    ],
    "seed_topics": CLAUDE_MD,
    "image_query": "muscle meal high protein",
}

if __name__ == "__main__":
    res = lib.run(CFG)
    print(res)
