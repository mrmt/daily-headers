# Daily Headers

日替わりのヘッダー画像(Notion のカバー画像などに使う 15:4 / 約 1500x400px)を 366 日分アセットとして管理するリポジトリです。

## 概要

`assets/MM/DD.jpg` に日付ごとの画像、`assets/MM/DD.txt` にそのテーマを置いています。月ごとの一覧は自動生成されます。

画像生成用のスクリプト群 (Gemini 3.1 Flash Image を使った自動生成) は保守を終了し削除しました。現在は**画像を外部で生成し、このリポジトリには手動で登録する**運用です。

## 使い方

### アセットの登録

1. 対象日の `assets/MM/DD.jpg` を新しい画像(JPEG)で置き換える
2. `assets/MM/DD.txt` の内容をその画像のテーマ文字列に置き換える
3. アセット一覧を再生成する

### アセット一覧 (README) の更新

`assets/` 配下の画像と説明文をスキャンし、月別 `assets/MM/README.md` とインデックス `assets/README.md` を生成・更新します。

```bash
python3 update_assets_readme.py
```

標準ライブラリのみを使うため、追加の依存関係や仮想環境は不要です。

## 生成されたアセットについて

画像の一覧は [assets/README.md](assets/README.md) で確認できます。

## 生成コストについて (参考記録)

初回に全 366 枚を Gemini で生成した際にかかった費用です(2026/3/20 時点、税抜)。

- **生成枚数**: 366 枚
- **使用モデル**: Gemini 3.1 Flash Image (Image Output)
- **使用量**: 411,040 count
- **費用**: 3,860 JPY

## Assets and AI-Generated Content

本リポジトリに含まれる一部の画像アセット(`/assets` ディレクトリ内など)は、Google の Gemini Nano Banana を使用して生成されています。
これらの画像は、プロジェクトの視覚的補助を目的としています。

AI 生成物の著作権および利用条件については、[Google Generative AI Additional Terms of Service](https://ai.google.dev/gemini-api/terms) に準拠します。
コード部分に適用される MIT License とは、権利の性質が異なる場合がある点にご注意ください。
