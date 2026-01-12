def build_prompt(student, jd):
    return f"""
You are an AI assistant for an internship platform called InternHub.

Student Profile:
Skills: {', '.join(student.skills)}
Interests: {', '.join(student.interests)}
Education: {student.education}

Internship Description:
{jd}

Return ONLY valid JSON in the following format.
Do not add explanations or markdown.

{{
  "match_summary": "string",
  "skill_gaps": ["string"],
  "confidence_score": number_between_0_and_100,
  "recommendations": "string",
  "resume": "string"
}}
"""
