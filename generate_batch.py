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
    days_in_month = {8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    all_tasks = []
    
    for m in month_list:
        for d in range(1, days_in_month[m] + 1):
            date = f"{m:02d}-{d:02d}"
            # すでにファイルが存在するかチェック（以前のセッションで生成済みの場合に備えて）
            if not os.path.exists(f"assets/{date}.jpg"):
                all_tasks.append((date, f"Month {m} Day {d}", f"{m}月{d}日のヘッダー画像。季節の移り変わりと風景。"))
        
    return all_tasks

if __name__ == "__main__":
    tasks = get_tasks_for_range([8, 9, 10, 11, 12])
    process_tasks(tasks, max_workers=4)
