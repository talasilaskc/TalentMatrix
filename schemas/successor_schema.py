from pydantic import BaseModel
from typing import List


class SuccessorRecommendation(BaseModel):
    employee_id: str
    employee_name: str
    readiness_score: float
    matching_skills: List[str]
    missing_skills: List[str]