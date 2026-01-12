from pydantic import BaseModel
from typing import List, Optional

class StudentProfile(BaseModel):
    name: str
    skills: List[str]
    interests: List[str]
    education: str

class InternshipInput(BaseModel):
    student: StudentProfile
    internship_description: str

class AnalysisResponse(BaseModel):
    match_summary: str
    skill_gaps: List[str]
    confidence_score: int
    recommendations: str
    resume: Optional[str]
