import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# .env ファイルから環境変数をロード
load_dotenv()

def generate_header(prompt: str, output_path: str = "generated_header.png"):
    # 環境変数の取得
    api_key = os.environ.get("VERTEX_API_KEY")
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT")
    location = os.environ.get("GOOGLE_CLOUD_LOCATION", "us-central1")

    if not api_key or not project_id:
        print("Error: VERTEX_API_KEY or GOOGLE_CLOUD_PROJECT is not set in .env")
        sys.exit(1)

    # Gemini Client の初期化 (Google AI Studio モード)
    # APIキーを使用する場合は vertexai=False にします
    client = genai.Client(
        api_key=api_key,
        vertexai=False
    )

    print(f"Generating image for prompt: '{prompt}' using Gemini 3.1 Flash Image (Nano Banana 2)...")

    try:
        # 画像生成リクエスト
        # Nano Banana 2 (Gemini 3.1 Flash Image) は generate_content で画像を生成します
        response = client.models.generate_content(
            model="gemini-3.1-flash-image-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                # ヘッダー画像に適したパラメータ（必要に応じて調整）
                candidate_count=1,
                # 検索グラウンディングを有効にする場合（任意）
                # tools=[types.Tool(google_search=types.GoogleSearch())]
            )
        )

        # 生成された画像を保存
        image_found = False
        for i, part in enumerate(response.candidates[0].content.parts):
            if part.inline_data:
                with open(output_path, "wb") as f:
                    f.write(part.inline_data.data)
                print(f"Success! Image saved to: {output_path}")
                image_found = True
                break
        
        if not image_found:
            print("No image data found in the response.")

    except Exception as e:
        print(f"An error occurred during generation: {e}")

if __name__ == "__main__":
    # デフォルトのプロンプト
    default_prompt = "A high-quality cinematic wide header background, abstract digital waves, sunset color palette, 4k resolution"
    
    # コマンドライン引数があればそれを使用
    prompt = sys.argv[1] if len(sys.argv) > 1 else default_prompt
    generate_header(prompt)
