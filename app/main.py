from fastapi import FastAPI
from app.schemas import InternshipInput, AnalysisResponse
from app.prompts import build_prompt
from app.ai_engine import analyze_profile
import json
import re

app = FastAPI(
    title="InternHub AI API",
    docs_url="/docs",
    redoc_url="/redoc",
    openapi_url="/openapi.json"
)

# -----------------------------
# Utility: Safe JSON extraction
# -----------------------------
def extract_json(text: str):
    try:
        text = re.sub(r"```json|```", "", text).strip()
        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())
    except Exception:
        pass
    return None

# --------------------------------
# Deterministic logic-based fallback
# --------------------------------
def deterministic_fallback(student, jd_text):
    jd_lower = jd_text.lower()

    matched = [
        skill for skill in student.skills
        if skill.lower() in jd_lower
    ]

    jd_keywords = [
        "machine learning", "statistics", "deep learning",
        "data analysis", "python", "sql"
    ]

    missing = [
        kw for kw in jd_keywords
        if kw in jd_lower and kw not in [s.lower() for s in matched]
    ]

    score = int((len(matched) / max(len(jd_keywords), 1)) * 100)

    return {
        "match_summary": (
            f"The student matches {len(matched)} key skills required "
            f"for the internship based on the provided profile."
        ),
        "skill_gaps": missing,
        "confidence_score": score,
        "recommendations": (
            "Strengthen the missing skills to improve internship alignment."
        ),
        "resume": (
            f"{student.name}\n"
            f"Education: {student.education}\n"
            f"Skills: {', '.join(student.skills)}"
        )
    }

# -----------------------------
# Main API Endpoint
# -----------------------------
@app.post("/analyze", response_model=AnalysisResponse)
def analyze(data: InternshipInput):
    prompt = build_prompt(data.student, data.internship_description)

    try:
        ai_output = analyze_profile(prompt)
        parsed = extract_json(ai_output)
        if parsed:
            return parsed
    except Exception:
        pass  # Move to deterministic fallback

    return deterministic_fallback(
        data.student,
        data.internship_description
    )

@app.get("/")
def root():
    return {
        "message": "InternHub AI API is running",
        "docs": "/docs"
    }



