from pydantic import BaseModel
from typing import List


class CandidateRecommendation(BaseModel):
    employee_id: str
    employee_name: str
    fit_score: float


class MobilityRecommendation(BaseModel):
    target_role: str
    recommendations: List[CandidateRecommendation]