import os
import glob
from collections import defaultdict

def update_assets_readme():
    assets_dir = "assets"
    readme_path = os.path.join(assets_dir, "README.md")
    
    # jpg ファイルを検索
    jpg_files = sorted(glob.glob(os.path.join(assets_dir, "[0-1][0-9]-[0-3][0-9].jpg")))
    
    # 月ごとにグループ化
    monthly_data = defaultdict(list)
    for jpg_path in jpg_files:
        filename = os.path.basename(jpg_path)
        month = filename[:2]
        monthly_data[month].append(filename)
    
    content = "# Daily Headers Assets\n\n"
    content += "本ディレクトリには、AIによって生成された日替わりヘッダー画像と、そのテーマに関する説明が格納されています。\n\n"
    
    # 月ごとにセクションを作成
    for month in sorted(monthly_data.keys()):
        content += f"## {int(month)}月\n\n"
        content += "| 日付 | 画像プレビュー | 説明 |\n"
        content += "| :--- | :--- | :--- |\n"
        
        for filename in monthly_data[month]:
            date_str = filename.replace(".jpg", "")
            txt_filename = filename.replace(".jpg", ".txt")
            txt_path = os.path.join(assets_dir, txt_filename)
            
            # 説明文の読み込み
            description = "（説明文なし）"
            if os.path.exists(txt_path):
                with open(txt_path, "r", encoding="utf-8") as f:
                    description = f.read().strip()
            
            # テーブル行の追加 (Notion等のプレビューを考慮して画像を表示)
            content += f"| {date_str} | ![{date_str}]({filename}) | {description} |\n"
        
        content += "\n"
    
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write(content)
    
    print(f"Successfully updated: {readme_path}")

if __name__ == "__main__":
    update_assets_readme()
