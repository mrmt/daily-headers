import os
import glob
from collections import defaultdict

def update_assets_readme():
    assets_dir = "assets"
    index_readme_path = os.path.join(assets_dir, "README.md")
    
    # jpg ファイルを検索
    jpg_files = sorted(glob.glob(os.path.join(assets_dir, "[0-1][0-9]-[0-3][0-9].jpg")))
    
    # 月ごとにグループ化
    monthly_data = defaultdict(list)
    for jpg_path in jpg_files:
        filename = os.path.basename(jpg_path)
        month = filename[:2]
        monthly_data[month].append(filename)
    
    # インデックス (README.md) の作成
    index_content = "# Daily Headers Assets\n\n"
    index_content += "AI によって生成された日替わりヘッダー画像を月ごとに整理しています。\n\n"
    index_content += "| 月 | リンク |\n"
    index_content += "| :--- | :--- |\n"
    
    # 月ごとに個別ファイルを作成
    for month in sorted(monthly_data.keys()):
        month_int = int(month)
        month_filename = f"{month}.md"
        month_path = os.path.join(assets_dir, month_filename)
        
        index_content += f"| {month_int}月 | [{month_int}月のヘッダー一覧](./{month_filename}) |\n"
        
        month_content = f"# {month_int}月のヘッダー画像\n\n"
        month_content += "| 日付 | 画像プレビュー | 説明 |\n"
        month_content += "| :--- | :--- | :--- |\n"
        
        for filename in monthly_data[month]:
            date_str = filename.replace(".jpg", "")
            txt_filename = filename.replace(".jpg", ".txt")
            txt_path = os.path.join(assets_dir, txt_filename)
            
            # 説明文の読み込み
            description = "（説明文なし）"
            if os.path.exists(txt_path):
                with open(txt_path, "r", encoding="utf-8") as f:
                    description = f.read().strip()
            
            # 月次ファイル内のリンクは相対パス
            month_content += f"| {date_str} | ![{date_str}]({filename}) | {description} |\n"
        
        with open(month_path, "w", encoding="utf-8") as f:
            f.write(month_content)
        print(f"Generated: {month_path}")
    
    with open(index_readme_path, "w", encoding="utf-8") as f:
        f.write(index_content)
    
    print(f"Successfully updated index: {index_readme_path}")

if __name__ == "__main__":
    update_assets_readme()
