import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def _call_gemini(model_name: str, prompt: str) -> str:
    response = client.models.generate_content(
        model=model_name,
        contents=prompt
    )
    return response.text

def analyze_profile(prompt: str) -> str:
    # 1️⃣ Try Gemini 2.0 Flash
    try:
        return _call_gemini("gemini-2.0-flash", prompt)
    except Exception:
        pass

    # 2️⃣ Fallback to Gemini 1.5 Flash
    try:
        return _call_gemini("gemini-1.5-flash", prompt)
    except Exception:
        pass

    # 3️⃣ If both fail → raise error
    raise RuntimeError("All Gemini models failed")
