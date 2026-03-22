# Daily Headers

Google DeepMind の Gemini 3.1 Flash Image (Nano Banana 2) を活用して、日替わりのヘッダー画像を自動生成し、アセットとして管理するプロジェクトです。

## 概要

本プロジェクトは、特定の日付のテーマに基づき、Notion のカバー画像などに最適なヘッダー画像を生成します。生成された画像は `/assets` ディレクトリに保存され、月ごとに整理された一覧が自動生成されます。

## セットアップ

本プロジェクトでは、Python パッケージマネージャーとして [uv](https://github.com/astral-sh/uv) を使用しています。

1. **環境変数の設定**
   `.env.example` をコピーして `.env` を作成し、必要な API キーを設定してください。
   ```bash
   cp .env.example .env
   ```
   `.env` 内に以下の値を設定します：
   - `VERTEX_API_KEY`: Google AI Studio の API キー
   - `GOOGLE_CLOUD_PROJECT`: Google Cloud プロジェクト ID

2. **環境の構築**
   ```bash
   uv sync
   ```

## 使い方

### 1. 日替わりヘッダーの生成

特定の日付のテーマに基づき、画像（.jpg）と説明文（.txt）を生成します。

```bash
uv run python generate_daily.py <MM-DD> "<Theme>" "<Description>"
```
- 例: `uv run python generate_daily.py 04-01 "April Fools Day" "エイプリルフールのためのユニークなヘッダー画像"`

生成される画像は 4:1 のアスペクト比で、パステルカラーのソフトなトーンに最適化されています。

### 2. アセット一覧 (README) の更新

`/assets` ディレクトリ内の画像と説明文をスキャンし、月ごとに整理された一覧を `/assets/README.md` に生成・更新します。

```bash
uv run python update_assets_readme.py
```

## 生成されたアセットについて

本プロジェクトで生成された画像の一覧は、[assets/README.md](assets/README.md) で確認できます。

## Assets and AI-Generated Content

本リポジトリに含まれる一部の画像アセット（`/assets` ディレクトリ内など）は、Google の Gemini Nano Banana を使用して生成されています。
これらの画像は、プロジェクトの視覚的補助を目的としています。

AI 生成物の著作権および利用条件については、[Google Generative AI Additional Terms of Service](https://ai.google.dev/gemini-api/terms) に準拠します。
コード部分に適用される MIT License とは、権利の性質が異なる場合がある点にご注意ください。
