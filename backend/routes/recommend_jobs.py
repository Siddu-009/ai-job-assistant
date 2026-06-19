from fastapi import APIRouter
from pydantic import BaseModel

from services.token_service import decode_token
from services.job_recommender import recommend_jobs

from database import SessionLocal
from sqlalchemy import text

router = APIRouter()


class RecommendRequest(BaseModel):
    token: str


@router.post("/")
def recommend(req: RecommendRequest):

    payload = decode_token(
        req.token
    )

    user_id = payload["user_id"]

    db = SessionLocal()

    result = db.execute(
        text(
            """
            SELECT generated_resume
            FROM generated_resumes
            WHERE user_id = :user_id
            ORDER BY id DESC
            LIMIT 1
            """
        ),
        {
            "user_id": user_id
        }
    )

    row = result.fetchone()

    db.close()

    if not row:

        return {
            "error": "No resume found"
        }

    resume_text = row[0]

    skills_db = [
        "aws",
        "docker",
        "kubernetes",
        "terraform",
        "jenkins",
        "ansible",
        "linux",
        "prometheus",
        "grafana",
        "git",
        "github"
    ]

    found_skills = []

    for skill in skills_db:

        if skill in resume_text.lower():

            found_skills.append(
                skill
            )

    recommendations = recommend_jobs(
        found_skills
    )

    return {
        "skills_found": found_skills,
        "recommended_jobs": recommendations[:10]
    }
