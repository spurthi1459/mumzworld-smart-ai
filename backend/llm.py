import google.generativeai as genai
import os
from dotenv import load_dotenv
from backend.prompts import SYSTEM_PROMPT


load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("models/gemini-pro")


def call_llm(query, products):
    prompt = f"""
    {SYSTEM_PROMPT}

    User query: {query}

    Products:
    {products}
    """

    try:
        response = model.generate_content(prompt)
        return response.text

    except Exception as e:
        print("LLM Error:", e)

        # ✅ Fallback response (VERY IMPORTANT)
        return "Here are some recommended products based on your search."