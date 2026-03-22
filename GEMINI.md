# Gemini CLI Project Skills: daily-headers

本プロジェクトでは、Google DeepMind の Gemini 3.1 Flash Image (Nano Banana 2) を活用して、日替わりのヘッダー画像を自動生成し、アセットとして管理します。

## 1. 日替わりヘッダーの生成 (Generate Daily Header)

特定の日付のテーマに基づき、Notion カバー画像に最適化されたヘッダー画像と説明文を生成します。

### 実行コマンド
```bash
uv run python generate_daily.py <MM-DD> "<Theme>" "<Description>"
```

- **MM-DD**: 日付（例: `04-01`）
- **Theme**: 生成する画像のテーマ（英語推奨）
- **Description**: 画像の説明文（日本語）

### 仕様
- **モデル**: `gemini-3.1-flash-image-preview` (Nano Banana 2)
- **アスペクト比**: 4:1 (15:4 に最適化)
- **スタイル**: 淡いパステルカラー、ソフトトーン、文字なし
- **出力**: `/assets/MM-DD.jpg` および `/assets/MM-DD.txt`

---

## 2. アセット一覧の更新 (Update Assets README)

`/assets/` ディレクトリ内の画像と説明文をスキャンし、月ごとに整理された `README.md` を生成・更新します。

### 実行コマンド
```bash
uv run python update_assets_readme.py
```

### 仕様
- `/assets/MM-DD.jpg` と `/assets/MM-DD.txt` を紐付け、マークダウン形式のテーブルを出力。
- プレビュー画像を表示。

---

## 3. 環境設定 (Environment Setup)

実行には以下の環境変数が設定された `.env` ファイルがルートディレクトリに必要です。

```env
VERTEX_API_KEY=your_api_key
GOOGLE_CLOUD_PROJECT=your_project_id
```

---

## ワークフロー例

1.  Wikipedia 等で「今日は何の日」を調べる。
2.  `generate_daily.py` で画像を生成。
3.  `update_assets_readme.py` で一覧を更新。
4.  Git にコミットする。
