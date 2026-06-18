from fastapi import APIRouter
from pydantic import BaseModel

from services.skill_gap_analyzer import (
    analyze_skill_gap
)

router = APIRouter()

class SkillGapRequest(BaseModel):
    resume_text: str
    job_description: str

@router.post("/")
def skill_gap(req: SkillGapRequest):

    result = analyze_skill_gap(
        req.resume_text,
        req.job_description
    )

    return result
