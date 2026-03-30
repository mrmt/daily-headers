# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

Gemini 3.1 Flash Image を使い、366日分の日替わりヘッダー画像(Notion カバー用、15:4 / 1500x400px)を生成・管理するプロジェクト。

## コマンド

```bash
# 依存関係インストール
uv sync

# 単一画像の生成
uv run python generate_daily.py <MM-DD> "<Theme英語>" "<説明文日本語>"

# アセット一覧(月別README)の更新
uv run python update_assets_readme.py
```

## 環境変数

`.env` ファイルに以下を設定(`.env.example` 参照):

- `VERTEX_API_KEY` - Google AI Studio API キー
- `GOOGLE_CLOUD_PROJECT` - GCP プロジェクトID

## アーキテクチャ

- **generate_daily.py** - 単一日付の画像生成(メインエントリポイント)。`gemini-3.1-flash-image-preview` モデルを使用し、`assets/MM-DD.jpg` と `assets/MM-DD.txt` を出力
- **generate_header.py** - カスタムプロンプトによる汎用ヘッダー生成
- **generate_batch.py** - 日付範囲の一括生成(ThreadPoolExecutor、max_workers=4)
- **generate_monthly_parallel.py** - 月単位の並列生成(テーマ・説明文をハードコード)
- **update_assets_readme.py** - `assets/` を走査し、月別 `.md` ファイルとインデックス `README.md` を自動生成

## assets/ ディレクトリ

- `MM-DD.jpg` - 生成画像(366ファイル、うるう年対応)
- `MM-DD.txt` - 画像の日本語説明文
- `MM.md` - 月別マークダウン(画像プレビュー+説明テーブル)
- `README.md` - 月別ファイルへのインデックス

## 画像生成プロンプト仕様

- 淡いパステルカラー、ソフトトーン、ドリーミーな雰囲気
- テキスト・文字・数字は一切含めない
- アスペクト比 4:1、解像度 1K
- テーマは英語、説明文は日本語で指定

## ワークフロー

1. 「今日は何の日」を調べる
2. `generate_daily.py` で画像生成
3. `update_assets_readme.py` で一覧更新
4. Git コミット
