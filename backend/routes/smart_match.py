from fastapi import APIRouter
from pydantic import BaseModel

from services.parser import extract_text
from services.resume_skill_extractor import extract_skills

from database import SessionLocal
from sqlalchemy import text

router = APIRouter()

class SmartMatchRequest(BaseModel):
    filename: str

@router.post("/")
def smart_match(req: SmartMatchRequest):

    filepath = f"uploads/{req.filename}"

    resume_text = extract_text(
        filepath
    )

    skills = extract_skills(
        resume_text
    )

    db = SessionLocal()

    result = db.execute(
        text(
            """
            SELECT
                id,
                title,
                company,
                location,
                skills,
                apply_url
            FROM jobs
            """
        )
    )

    jobs = result.fetchall()

    db.close()

    matches = []

    for job in jobs:

        job_skills = [
            skill.strip().lower()
            for skill in job[4].split(",")
        ]

        matched = len(
            set(skills)
            &
            set(job_skills)
        )

        score = int(
            (
                matched /
                len(job_skills)
            ) * 100
        )

        matches.append(
            {
                "job_id": job[0],
                "title": job[1],
                "company": job[2],
                "location": job[3],
                "score": score,
                "apply_url": job[5]
            }
        )

    matches.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return {
        "skills_found": skills,
        "matches": matches
    }
