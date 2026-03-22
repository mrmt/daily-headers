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
    # 2月分 (02-01 to 02-29)
    FEBRUARY_TASKS = [
        ("02-01", "TV Broadcasting Day", "テレビ放送記念日：日本で初めてテレビ放送が開始された日。"),
        ("02-02", "Setsubun", "節分：豆まきをして邪気を払い、福を呼び込む伝統行事。"),
        ("02-03", "Risshun", "立春：暦の上で春が始まる日。新しい季節の訪れ。"),
        ("02-04", "World Cancer Day", "世界対がんデー：がんへの意識を高め、予防と治療を考える日。"),
        ("02-05", "Nishiko Day", "ニコニコの日：笑顔で過ごし、周囲に幸せを広げる日。"),
        ("02-06", "Match Day", "ブログの日：日々の想いや情報を綴るブログ文化を祝う。"),
        ("02-07", "Northern Territories Day", "北方領土の日：平和と領土について考える日。"),
        ("02-08", "Hari-kuyo", "針供養：折れた針を豆腐に刺して供養し、裁縫の上達を願う。"),
        ("02-09", "Meat Day", "肉の日：美味しいお肉料理を楽しみ、活力を養う日。"),
        ("02-10", "Nitto Day", "ニットの日：編み物の温もりと手作りの楽しさを感じる日。"),
        ("02-11", "National Foundation Day", "建国記念の日：国の成り立ちをしのび、国を愛する心を養う。"),
        ("02-12", "Darwin Day", "ダーウィンの日：進化論を提唱したダーウィンの功績と科学を祝う。"),
        ("02-13", "World Radio Day", "世界ラジオの日：情報を伝え、人々を繋ぐラジオの役割を称える。"),
        ("02-14", "Valentine's Day", "バレンタインデー：大切な人に愛や感謝を伝える日。"),
        ("02-15", "Hippopotamus Day", "世界カバの日：カバの生態を知り、保護について考える日。"),
        ("02-16", "Weather Map Day", "天気図記念日：日本で初めて天気図が作成された日。"),
        ("02-17", "Angelic Whispers Day", "天使のささやきの日：ダイヤモンドダストが見られる幻想的な日。"),
        ("02-18", "Air Mail Day", "エアメールの日：遠く離れた場所へ届く手紙と空の旅。"),
        ("02-19", "天地の日 (Tenchi no Hi)", "天地の日：コペルニクスの誕生日にちなみ、宇宙の理を考える。"),
        ("02-20", "歌舞伎の日 (Kabuki no Hi)", "歌舞伎の日：出雲の阿国が江戸で初めて歌舞伎を披露した日。"),
        ("02-21", "Language Day", "国際母語デー：言語の多様性と文化的な理解を深める日。"),
        ("02-22", "Cat Day", "猫の日：猫との暮らしを慈しみ、感謝する日。"),
        ("02-23", "Fuji-san Day", "富士山の日：日本の象徴である富士山を愛で、保護する日。"),
        ("02-24", "Railroad Day", "鉄道ストの日：かつての労働運動を振り返り、現代の労働を考える。"),
        ("02-25", "Clam Day", "ひざの日：健康な体を維持し、活動的に過ごすことを意識する。"),
        ("02-26", "Escape Day", "脱出の日：ナポレオンがエルバ島を脱出した日にちなみ、新しい道を探る。"),
        ("02-27", "絆の日 (Kizuna no Hi)", "絆の日：冬の寒さの中で、人との温かい繋がりを再確認する日。"),
        ("02-28", "Golden Day", "ビスケットの日：日本で初めてビスケットの製法が紹介された日。"),
        ("02-29", "Leap Day", "閏日：4年に一度の特別な日。ボーナスの1日を大切に過ごす。"),
    ]
    process_tasks(FEBRUARY_TASKS, max_workers=4)
