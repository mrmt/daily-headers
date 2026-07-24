import os
import glob
from collections import defaultdict

def update_assets_readme():
    assets_dir = "assets"
    index_readme_path = os.path.join(assets_dir, "README.md")

    # 新レイアウト: assets/MM/DD.jpg
    jpg_files = sorted(glob.glob(os.path.join(assets_dir, "[0-1][0-9]", "[0-3][0-9].jpg")))

    # 月ごとにグループ化
    monthly_data = defaultdict(list)
    for jpg_path in jpg_files:
        # assets/MM/DD.jpg → month=MM, day_file=DD.jpg
        parts = jpg_path.split(os.sep)
        month = parts[-2]
        day_file = parts[-1]
        monthly_data[month].append(day_file)

    # インデックス (README.md)
    index_content = "# Daily Headers Assets\n\n"
    index_content += "AI によって生成された日替わりヘッダー画像を月ごとに整理しています。\n\n"
    index_content += "| 月 | リンク |\n"
    index_content += "| :--- | :--- |\n"

    for month in sorted(monthly_data.keys()):
        month_int = int(month)
        month_dir = os.path.join(assets_dir, month)
        month_readme_path = os.path.join(month_dir, "README.md")

        index_content += f"| {month_int}月 | [{month_int}月のヘッダー一覧](./{month}/README.md) |\n"

        month_content = f"# {month_int}月のヘッダー画像\n\n"
        month_content += "| 日付 | 画像プレビュー | 説明 |\n"
        month_content += "| :--- | :--- | :--- |\n"

        for day_file in monthly_data[month]:
            day = day_file.replace(".jpg", "")
            date_str = f"{month}-{day}"
            txt_path = os.path.join(month_dir, f"{day}.txt")

            description = "（説明文なし）"
            if os.path.exists(txt_path):
                with open(txt_path, "r", encoding="utf-8") as f:
                    description = f.read().strip()

            # 月次 README からは同ディレクトリの相対パス
            month_content += f"| {date_str} | ![{date_str}]({day_file}) | {description} |\n"

        with open(month_readme_path, "w", encoding="utf-8") as f:
            f.write(month_content)
        print(f"Generated: {month_readme_path}")

    with open(index_readme_path, "w", encoding="utf-8") as f:
        f.write(index_content)

    print(f"Successfully updated index: {index_readme_path}")

if __name__ == "__main__":
    update_assets_readme()
