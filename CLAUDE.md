# 筋トレ女子メシ - 自動更新ガイド

## サイト概要
- **サイト名**: 筋トレ女子メシ
- **運営**: MuscleLove
- **URL**: https://musclelove-777.github.io/muscle-meal-girls/
- **テーマ**: 筋トレする女性向けの高タンパクレシピ・筋肉飯・ミールプレップ情報

## 記事カテゴリ
1. **レシピ (recipe)** - 高タンパク・低脂質の自炊レシピ
2. **コンビニ飯 (convenience)** - セブン・ファミマ・ローソンの高タンパク商品
3. **プロテイン (protein)** - プロテインドリンク・スムージーレシピ
4. **ミールプレップ (mealprep)** - 作り置き・週末まとめ調理
5. **PFCバランス (pfc)** - 栄養バランス・マクロ管理
6. **サプリ (supplement)** - BCAA、クレアチンなどサプリ情報

## 記事テンプレート

### ファイル名規則
`articles/YYYY-MM-DD-slug.html` (例: `articles/2026-04-05-tofu-steak.html`)

### 記事HTML構造
```html
<!DOCTYPE html>
<html lang="ja">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>【記事タイトル】 | 筋トレ女子メシ</title>
  <meta name="description" content="記事の要約（120文字以内）">
  <meta property="og:title" content="記事タイトル | 筋トレ女子メシ">
  <meta property="og:description" content="記事の要約">
  <meta property="og:image" content="Unsplash画像URL?w=1200&h=630&fit=crop">
  <meta property="og:url" content="https://musclelove-777.github.io/muscle-meal-girls/articles/ファイル名.html">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@MuscleGirlLove7">
  <link rel="canonical" href="https://musclelove-777.github.io/muscle-meal-girls/articles/ファイル名.html">
  <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;500;700;900&display=swap" rel="stylesheet">
  <!-- index.htmlと同じstyleをコピー + 記事用追加スタイル -->
  <style>
    /* index.htmlの:root変数とbody基本スタイルをコピー */
    * { margin:0; padding:0; box-sizing:border-box; }
    :root { --bg-primary:#0d1117; --bg-secondary:#161b22; --bg-card:#1c2128; --accent:#4caf50; --accent-light:#66bb6a; --text-primary:#e6edf3; --text-secondary:#8b949e; --border:#30363d; }
    body { font-family:'Noto Sans JP',sans-serif; background:var(--bg-primary); color:var(--text-primary); line-height:1.8; }
    a { color:var(--accent-light); text-decoration:none; }

    .article-container { max-width:780px; margin:0 auto; padding:2rem 1.5rem; }
    .back-link { display:inline-block; margin-bottom:1.5rem; font-size:0.9rem; }
    .article-hero { width:100%; height:300px; object-fit:cover; border-radius:12px; margin-bottom:1.5rem; }
    .article-title { font-size:1.8rem; font-weight:900; margin-bottom:0.5rem; line-height:1.4; }
    .article-date { font-size:0.8rem; color:var(--text-secondary); margin-bottom:1.5rem; }
    .article-body { font-size:1rem; line-height:2; }
    .article-body h2 { font-size:1.3rem; font-weight:700; margin:2rem 0 1rem; padding-left:0.8rem; border-left:3px solid var(--accent); }
    .article-body h3 { font-size:1.1rem; font-weight:700; margin:1.5rem 0 0.8rem; }
    .article-body p { margin-bottom:1rem; }
    .article-body ul, .article-body ol { margin:0.5rem 0 1rem 1.5rem; }
    .article-body li { margin-bottom:0.3rem; }
    .pfc-table { width:100%; border-collapse:collapse; margin:1rem 0; }
    .pfc-table th, .pfc-table td { padding:0.5rem; border:1px solid var(--border); text-align:center; font-size:0.9rem; }
    .pfc-table th { background:var(--bg-secondary); font-weight:700; }
  </style>
</head>
<body>
  <div class="article-container">
    <a href="../index.html" class="back-link">← トップに戻る</a>
    <img src="Unsplash画像URL?w=800&h=400&fit=crop" alt="記事タイトル" class="article-hero" loading="lazy">
    <h1 class="article-title">記事タイトル</h1>
    <div class="article-date">2026-XX-XX</div>
    <div class="article-body">
      <!-- 記事本文 -->
    </div>
    <hr style="border-color:var(--border); margin:2rem 0;">
    <a href="../index.html" class="back-link">← トップに戻る</a>
  </div>
</body>
</html>
```

## 記事作成ルール

### 基本ルール
- **言語**: 日本語
- **文字数**: 200〜400文字（本文のみ）
- **トーン**: 実用的で親しみやすい。筋トレ女子の友達に話すような感じ
- **画像**: 必ずUnsplash画像をヒーロー画像として使用（`?w=800&h=400&fit=crop`付き）

### PFC情報の書き方
レシピ記事には必ず以下を含める：
```
| 栄養素 | 量 |
|--------|-----|
| カロリー | ○○○kcal |
| タンパク質(P) | ○○g |
| 脂質(F) | ○○g |
| 炭水化物(C) | ○○g |
```

### Unsplash画像の使い方
- 検索: `https://unsplash.com/s/photos/キーワード`
- 画像URL形式: `https://images.unsplash.com/photo-XXXX?w=800&h=400&fit=crop`
- 必ずalt属性を日本語で記述
- 食事・料理・健康食系の画像を選ぶ

## index.html更新手順

新記事を追加したら：

1. `index.html` の `.blog-grid` セクションに新しいカードを追加（最新が先頭）
2. 記事が4本以上になったら古いものを削除（常に最新3本を表示）
3. 必要に応じてレシピカードも追加・更新

### レシピカードの追加形式
```html
<div class="recipe-card" data-category="カテゴリ">
  <div class="accent-bar" style="background:var(--tag-カテゴリ)"></div>
  <div class="recipe-card-body">
    <h3>レシピ名</h3>
    <div class="recipe-meta">
      <span>🔥 ○○○kcal</span>
      <span>💪 タンパク質 ○○g</span>
      <span>⏱ ○○分</span>
    </div>
    <div class="recipe-tags">
      <span class="tag tag-カテゴリ">タグ名</span>
    </div>
  </div>
</div>
```

## sitemap.xml更新
新記事追加時は `sitemap.xml` にURLを追加すること。

## Git操作
```bash
git add -A
git commit -m "Add articles: 記事タイトル1, 記事タイトル2, ..."
git push origin master
```
