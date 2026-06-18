from fastapi import APIRouter
from pydantic import BaseModel

from services.resume_skill_extractor import extract_skills

from database import SessionLocal
from sqlalchemy import text

router = APIRouter()

class ResumeRequest(BaseModel):
    resume_text: str

@router.post("/")
def auto_match(req: ResumeRequest):

    extracted_skills = extract_skills(
        req.resume_text
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
            set(extracted_skills)
            &
            set(job_skills)
        )

        score = int(
            (matched / len(job_skills))
            * 100
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
        "skills_found": extracted_skills,
        "matches": matches
    }
