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
    # 1月分 (01-01 to 01-31)
    JANUARY_TASKS = [
        ("01-01", "New Year's Day", "元日：一年の始まりを祝う日。初日の出と門松。"),
        ("01-02", "Kakizome", "書き初め：年明けに初めて毛筆で文字や絵を書く行事。"),
        ("01-03", "Hakone Ekiden", "箱根駅伝：正月の風物詩である学生駅伝の熱気。"),
        ("01-04", "Stone Day", "石の日：地蔵や石像に触れて健康を願う日。"),
        ("01-05", "Strawberry Day", "いちごの日：旬のいちごを楽しみ、春の訪れを待つ日。"),
        ("01-06", "Epiphany", "公現祭（エピファニー）：東方の三博士がキリストを訪問したことを祝う。"),
        ("01-07", "Seven Herbs Day", "七草の日：春の七草粥を食べて無病息災を願う日。"),
        ("01-08", "Foreign Language Day", "外国語の日：新しい言葉や文化への好奇心を広げる日。"),
        ("01-09", "Quizzing Day", "クイズの日：知識と知恵を出し合い、楽しむ日。"),
        ("01-10", "Ten-ten Day", "110番の日：地域の安全と安心を考える日。"),
        ("01-11", "Kagami-biraki", "鏡開き：お正月に供えた鏡餅を割り、無病息災を願って食べる日。"),
        ("01-12", "Ski Day", "スキーの日：日本に初めて本格的なスキーが伝わった日。"),
        ("01-13", "Tabacco Day", "タバコの日：かつての文化を振り返り、現代の健康を考える。"),
        ("01-14", "Love Letter Day", "タロとジロの日：南極での絆と生命力を称える日。"),
        ("01-15", "Adult Day", "成人の日：大人の仲間入りをした若者たちの門出を祝う。"),
        ("01-16", "Enma-mairi", "初閻魔（閻魔参り）：地獄の王、閻魔様に一年の平穏を願う。"),
        ("01-17", "Disaster Prevention", "防災とボランティアの日：震災を忘れず、助け合いの精神を確認する。"),
        ("01-18", "Snow Day", "都バス記念日：都市の交通を支える風景を愛でる。"),
        ("01-19", "Karaoke Day", "のど自慢の日：歌を歌って、明るく健やかに過ごす日。"),
        ("01-20", "Twenty Day", "二十日正月：お正月の行事を締めくくり、日常に戻る日。"),
        ("01-21", "Cooking Day", "料理番組の日：美味しい料理と創造性を共有する日。"),
        ("01-22", "Curry Day", "カレーの日：国民食であるカレーライスを楽しむ日。"),
        ("01-23", "Electronic Mail Day", "電子メールの日：デジタルのメッセージが繋ぐ絆を祝う。"),
        ("01-24", "Gold Rush Day", "ゴールドラッシュの日：夢と冒険、新しい発見への挑戦。"),
        ("01-25", "Hot Cake Day", "ホットケーキの日：暖かくて甘いホットケーキで幸せを感じる日。"),
        ("01-26", "Cultural Property Protection", "文化財防火デー：貴重な文化遺産を火災から守る意識を高める日。"),
        ("01-27", "求婚の日 (Kyukon no Hi)", "求婚の日：愛の告白や大切な人への想いを伝える日。"),
        ("01-28", "Copy Day", "コピーライターの日：言葉の力で価値を伝える創造性を称える日。"),
        ("01-29", "Showa Base Day", "昭和基地開設記念日：南極観測の歴史と未知への探求。"),
        ("01-30", "Three-year-old Day", "3分間電話の日：コミュニケーションの大切さを再確認する。"),
        ("01-31", "Love Wife Day", "愛妻の日：大切なパートナーに感謝と愛情を伝える日。"),
    ]
    process_tasks(JANUARY_TASKS, max_workers=4)
