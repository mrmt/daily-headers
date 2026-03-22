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

if __name__ == "__main__":
    # 3月分 (03-01 to 03-22)
    MARCH_REMAINING = [
        ("03-01", "March First", "3月1日。春の始まりを感じる日。"),
        ("03-02", "Miniatures Day", "ミニの日。ミニチュアや小さいものを愛でる日。"),
        ("03-03", "Hina-matsuri", "ひな祭り。女の子の健やかな成長を願う行事。"),
        ("03-04", "Magazine Day", "雑誌の日。新しい情報や文化に触れる日。"),
        ("03-05", "Coral Day", "珊瑚の日。海の宝石、サンゴ礁を保護する日。"),
        ("03-06", "Brother's Day", "弟の日。兄弟の絆を大切にする日。"),
        ("03-07", "Sauna Day", "サウナの日。心身を整え、リラックスする日。"),
        ("03-08", "International Women's Day", "国際女性デー。ミモザの花と共に女性の功績を称える日。"),
        ("03-09", "Thank You Day", "ありがとうの日。感謝の気持ちを伝える日。"),
        ("03-10", "Sugar Day", "砂糖の日。甘いお菓子で幸せを感じる日。"),
        ("03-11", "Hope and Bond", "震災復興と絆。希望と祈りを捧げる日。"),
        ("03-12", "Wallet Day", "財布の日。新しい財布で金運や良縁を願う日。"),
        ("03-13", "Sandwich Day", "サンドイッチの日。手軽で楽しい食事を楽しむ日。"),
        ("03-14", "White Day", "ホワイトデー。贈り物で想いを返す日。"),
        ("03-15", "Shoes Day", "靴の日。新しい一歩を踏み出す日。"),
        ("03-16", "National Park Day", "国立公園指定記念日。豊かな自然を保護し、愛でる日。"),
        ("03-17", "Comic Magazine Day", "漫画週刊誌の日。日本の漫画文化を祝う日。"),
        ("03-18", "Braille Day", "点字ブロックの日。誰もが安心して歩ける社会を願う日。"),
        ("03-19", "Music Day", "ミュージックの日。音楽の力を感じる日。"),
        ("03-20", "Spring Equinox", "春分の日。自然を称え、生物を慈しむ日。"),
        ("03-21", "World Poetry Day", "世界詩歌デー。言葉の美しさと表現を祝う日。"),
        ("03-22", "World Water Day", "世界水の日。大切な資源である水を考える日。"),
    ]
    process_tasks(MARCH_REMAINING, max_workers=4)
