# InternHub – AI Internship Match Assistant

## Overview
InternHub AI is a simple backend API that evaluates how well a student profile matches an internship description. It uses AI reasoning where available and deterministic logic as a fallback to ensure reliability.

## What I Built
- A FastAPI-based backend service
- AI-powered internship matching using Google Gemini
- Skill gap analysis and confidence (ATS-style) scoring
- Resume generation tailored to the internship description
- Multi-level fallback to handle AI unavailability

## How It Works
1. The API accepts a student profile and internship description.
2. It first attempts to analyze the match using Gemini 2.0 Flash.
3. If unavailable, it falls back to Gemini 1.5 Flash.
4. If both AI models fail, a deterministic skill-matching algorithm is used.
5. The API always returns a structured JSON response.

## API Endpoint
### POST `/analyze`
**Input**
```json
{
  "student": {
    "name": "Mukul Kumar",
    "skills": ["Python", "SQL", "Pandas"],
    "interests": ["Data Science"],
    "education": "B.Tech CSE"
  },
  "internship_description": "Internship JD text"
}

## 📌 Sample API Response

```json
{
  "match_summary": "The student matches key skills required for the internship.",
  "skill_gaps": ["machine learning", "statistics"],
  "confidence_score": 16,
  "recommendations": "Strengthen the missing skills to improve internship alignment.",
  "resume": "Rahul Sharma\nEducation: B.Tech CSE\nSkills: Python, SQL, Pandas"
}

🚀 How to Run Locally
Start the FastAPI development server:
uvicorn app.main:app --reload
Open your browser and navigate to:
http://127.0.0.1:8000/docs
Use the interactive Swagger UI to test the APIs.

👤 Candidate Details 
Name: MUKUL KUMAR
Enrollment: E22CSEU1118
Batch: 2026
University: Bennett University
Role Applied For: AI Developer

📊 Output Explanation

match_summary – High-level summary of how well the candidate matches the role
skill_gaps – Missing or weak skills required for the internship
confidence_score – Numerical score representing overall alignment
recommendations – Suggestions to improve internship suitability
resume – Parsed resume content used for analysis
