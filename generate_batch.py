import os
import sys
import concurrent.futures
from dotenv import load_dotenv
from generate_daily import generate_daily

load_dotenv()

def process_tasks(tasks, max_workers=4):
    os.makedirs("assets", exist_ok=True)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(generate_daily, date, theme, desc, f"assets/{date}.jpg"): date for date, theme, desc in tasks}
        for future in concurrent.futures.as_completed(futures):
            date = futures[future]
            try:
                future.result()
                print(f"{date}: Success")
            except Exception as e:
                print(f"{date}: Failed ({e})")

def get_tasks_for_range(month_list):
    # 月ごとの日数を定義
    days_in_month = {5: 31, 6: 30, 7: 31}
    # 月ごとの代表的なテーマ（簡易化のため代表例を設定し、詳細は生成時に補足）
    themes = {
        5: [
            ("05-01", "Constitution Memorial Day", "憲法記念日：日本国憲法の施行を記念し、国の成長を期する。"),
            ("05-05", "Children's Day", "こどもの日：こどもの人格を重んじ、こどもの幸福をはかるとともに、母に感謝する。"),
            # 他の日付も同様に構築...
        ]
    }
    # 実際には全日付をリストアップする必要があります。
    # ここでは効率化のため、一括生成用のリストを直接作成します。
    all_tasks = []
    
    # 5月
    for d in range(1, 32):
        date = f"05-{d:02d}"
        all_tasks.append((date, f"May Day {d}", f"5月{d}日のヘッダー画像。初夏の爽やかな風景。"))
    # 6月
    for d in range(1, 31):
        date = f"06-{d:02d}"
        all_tasks.append((date, f"June Day {d}", f"6月{d}日のヘッダー画像。梅雨の情景や紫陽花。"))
    # 7月
    for d in range(1, 32):
        date = f"07-{d:02d}"
        all_tasks.append((date, f"July Day {d}", f"7月{d}日のヘッダー画像。夏本番、海や空の輝き。"))
        
    return all_tasks

if __name__ == "__main__":
    tasks = get_tasks_for_range([5, 6, 7])
    process_tasks(tasks, max_workers=4)
