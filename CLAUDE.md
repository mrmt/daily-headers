# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## プロジェクト概要

366日分の日替わりヘッダー画像(Notion カバー用、15:4 / 1500x400px)をアセットとして管理するリポジトリ。

画像生成スクリプト群 (Gemini 3.1 Flash Image を使った自動生成) は保守終了により削除済み。現在は**画像を外部で生成し、手動で登録する**運用。

## コマンド

```bash
# アセット一覧(月別README)の更新
python3 update_assets_readme.py
```

標準ライブラリ (`os` / `glob` / `collections`) のみを使うため、依存関係のインストールや仮想環境は不要。

## アーキテクチャ

- **update_assets_readme.py** - `assets/` を走査し、月別 `assets/MM/README.md` とインデックス `assets/README.md` を自動生成

## assets/ ディレクトリ

月ごとにサブディレクトリで整理:

- `assets/MM/DD.jpg` - 画像(366ファイル、うるう年対応)
- `assets/MM/DD.txt` - 画像のテーマ文字列(日本語)
- `assets/MM/README.md` - 月別マークダウン(画像プレビュー+説明テーブル)。自動生成
- `assets/README.md` - 月別ディレクトリへのインデックス。自動生成

## 画像の仕様

- 淡いパステルカラー、ソフトトーン、ドリーミーな雰囲気
- テキスト・文字・数字は一切含めない
- アスペクト比 4:1 (既存アセットは 2064x512)

## ワークフロー

1. 「今日は何の日」を調べてテーマを決める
2. 画像を外部で生成する(このリポジトリの範囲外)
3. `assets/MM/DD.jpg` を新しい画像のJPEG変換で置き換える
4. `assets/MM/DD.txt` をテーマ文字列で置き換える
5. `python3 update_assets_readme.py` で一覧更新
6. Git コミット(コミットメッセージはテーマ文字列)
