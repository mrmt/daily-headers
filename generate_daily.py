import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

# .env ファイルから環境変数をロード
load_dotenv()

def generate_daily(date_str: str, prompt_theme: str, description: str, output_path: str):
    api_key = os.environ.get("VERTEX_API_KEY")

    if not api_key:
        print("Error: VERTEX_API_KEY is not set in .env")
        sys.exit(1)

    # Gemini Client 初期化 (Google AI Studio モード)
    client = genai.Client(api_key=api_key, vertexai=False)

    # Issue #1 の要件を厳密に反映したプロンプト
    prompt = (
        f"A beautiful, minimalist daily header illustration for '{prompt_theme}'. "
        "The overall tone must be very pale, featuring soft pastel colors and a gentle, dreamy atmosphere. "
        "Strictly no text, no letters, no numbers, and no characters. "
        "Composition is optimized for a Notion cover image with an ultra-wide 15:4 aspect ratio (1500x400 pixels). "
        "Clean, modern, and inspiring aesthetic."
    )

    print(f"Generating image for {date_str} with theme: '{prompt_theme}'...")

    try:
        # 画像生成
        response = client.models.generate_content(
            model="gemini-3.1-flash-image-preview",
            contents=prompt,
            config=types.GenerateContentConfig(
                image_config=types.ImageConfig(
                    aspect_ratio="4:1",
                    image_size="1K"
                )
            )
        )

        image_found = False
        if hasattr(response, 'generated_images') and response.generated_images:
            response.generated_images[0].image.save(output_path)
            image_found = True
        else:
            for part in response.candidates[0].content.parts:
                if part.inline_data:
                    with open(output_path, "wb") as f:
                        f.write(part.inline_data.data)
                    image_found = True
                    break
        
        if image_found:
            print(f"Success! Daily header saved to: {output_path}")
            # 説明文の保存
            txt_path = output_path.replace(".jpg", ".txt")
            with open(txt_path, "w", encoding="utf-8") as f:
                f.write(description)
            print(f"Description saved to: {txt_path}")
        else:
            print("No image data found in the response.")

    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # 引数: MM-DD theme description
    if len(sys.argv) < 4:
        print("Usage: uv run generate-daily <MM-DD> <theme> <description>")
        sys.exit(1)
        
    date_arg = sys.argv[1]
    theme_arg = sys.argv[2]
    desc_arg = sys.argv[3]
    
    target_path = f"assets/{date_arg}.jpg"
    generate_daily(date_arg, theme_arg, desc_arg, target_path)

if __name__ == "__main__":
    main()
