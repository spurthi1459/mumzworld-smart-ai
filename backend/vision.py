import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-pro")


def describe_image(image_bytes):
    try:
        response = model.generate_content([
            "Describe this product briefly for shopping search",
            {"mime_type": "image/jpeg", "data": image_bytes}
        ])

        return response.text

    except Exception as e:
        print("VISION ERROR:", e)

        # ✅ fallback (VERY IMPORTANT)
        return "baby product"