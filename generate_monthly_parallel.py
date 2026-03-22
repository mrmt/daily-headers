import os
import sys
import concurrent.futures
from dotenv import load_dotenv
from generate_daily import generate_daily

# .env ファイルから環境変数をロード
load_dotenv()

# 4月のデータリスト
APRIL_TASKS = [
    ("04-01", "April Fools Day", "エイプリルフール：嘘をついても良いとされる日。創造的で楽しい嘘やいたずらを楽しむ日。"),
    ("04-02", "International Children's Book Day", "国際子どもの本の日：アンデルセンの誕生日にちなみ、子どもの本への関心を高める日。"),
    ("04-03", "Sea-Serpent Day (Shi-sa)", "シーサーの日：沖縄の守り神「シーサー」を記念する日。"),
    ("04-04", "Piano Tuner's Day", "ピアノ調律の日：調律の基準音 A=440Hz にちなみ、ピアノの音を整える技術を称える日。"),
    ("04-05", "Haircut Day", "ヘアカットの日：明治政府が断髪を許可した日。新しい自分に生まれ変わるイメージ。"),
    ("04-06", "Castle Day", "城の日：「し(4)ろ(6)」の語呂合わせ。日本の伝統的な城郭建築を愛でる日。"),
    ("04-07", "World Health Day", "世界保健デー：世界保健機関 (WHO) の発足を記念し、健康への意識を高める日。"),
    ("04-08", "Hana-matsuri (Flower Festival)", "花まつり：お釈迦様の降誕を祝う行事。色とりどりの花で飾られた花御堂が象徴。"),
    ("04-09", "Great Buddha Day", "大仏の日：奈良・東大寺の大仏開眼供養が行われた日。平和と安寧を願う。"),
    ("04-10", "Yacht Day", "ヨットの日：「ヨ(4)ット(10)」の語呂合わせ。海と風を感じるスポーツを記念する日。"),
    ("04-11", "Guts-pose Day", "ガッツポーズの日：勝利の喜びを表現する「ガッツポーズ」という言葉が広まった日。"),
    ("04-12", "International Day of Human Space Flight", "世界宇宙飛行の日：ガガーリンが人類初の宇宙飛行に成功した日。宇宙へのロマン。"),
    ("04-13", "Coffee House Day", "喫茶店の日：日本初の本格的な喫茶店が開業した日。ゆったりとした時間を楽しむ。"),
    ("04-14", "Orange Day", "オレンジデー：大切な人との絆を深めるため、オレンジ色のものを贈り合う日。"),
    ("04-15", "Helicopter Day", "ヘリコプターの日：ダ・ヴィンチの誕生日にちなみ、空飛ぶ機械への夢を馳せる日。"),
    ("04-16", "Chaplin Day", "チャップリンデー：喜劇王チャップリンの誕生日にちなみ、笑いと平和を考える日。"),
    ("04-17", "Dinosaur Day", "恐竜の日：初めて恐竜の卵の化石が発見された日。太古の地球への想像力。"),
    ("04-18", "Invention Day", "発明の日：現在の特許制度の元となる条例が公布された日。新しいアイデアを祝う日。"),
    ("04-19", "Map Day", "地図の日：伊能忠敬が日本地図作成のために初めて測量に出発した日。"),
    ("04-20", "Postal Day", "郵政記念日：近代郵便制度が始まった日。手紙が運ぶ心と繋がりを記念する日。"),
    ("04-21", "Game Boy Day", "ゲームボーイの日：任天堂が携帯ゲーム機「ゲームボーイ」を発売した日。遊びの革新。"),
    ("04-22", "Earth Day", "アースデイ（地球の日）：地球環境について考え、感謝し、行動する日。"),
    ("04-23", "Children's Reading Day", "子ども読書の日：子どもたちが本に親しみ、読書の楽しさを知るための日。"),
    ("04-24", "Botany Day", "植物学の日：植物学者・牧野富太郎の誕生日にちなみ、身近な草花を愛でる日。"),
    ("04-25", "World Penguin Day", "世界ペンギンの日：アデリーペンギンが北へ移動する時期にちなみ、ペンギンを保護する日。"),
    ("04-26", "World Intellectual Property Day", "世界知的財産の日：創造性とイノベーションを支える知的財産の役割を考える日。"),
    ("04-27", "Philosophy Day", "哲学の日：古代ギリシャの哲学者ソクラテスの命日にちなみ、真理を追求する心を持つ日。"),
    ("04-28", "Elephant Day", "象の日：日本に初めて象がやってきた日。力強く優しい動物への親しみ。"),
    ("04-29", "Showa Day", "昭和の日：激動の日々を経て、復興を遂げた昭和の時代を顧み、国の将来に思いを馳せる日。"),
    ("04-30", "Library Day", "図書館記念日：図書館法が公布された日。知識の宝庫である図書館に親しむ日。"),
]

def process_task(task):
    date_str, theme, description = task
    output_path = f"assets/{date_str}.jpg"
    
    # すでにファイルが存在する場合はスキップ（再実行時の効率化）
    if os.path.exists(output_path):
        print(f"Skipping {date_str}, already exists.")
        return f"{date_str}: Skipped"
    
    try:
        generate_daily(date_str, theme, description, output_path)
        return f"{date_str}: Success"
    except Exception as e:
        return f"{date_str}: Failed ({e})"

def main():
    # assets ディレクトリの確認
    os.makedirs("assets", exist_ok=True)
    
    print(f"Starting parallel generation for {len(APRIL_TASKS)} tasks...")
    
    # 並列実行 (max_workers は API の制限に合わせて調整、5程度が安全)
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(process_task, APRIL_TASKS))
    
    print("\nGeneration Summary:")
    for result in results:
        print(result)

if __name__ == "__main__":
    main()
