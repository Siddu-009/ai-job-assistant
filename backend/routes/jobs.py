from fastapi import APIRouter
from pydantic import BaseModel

from database import SessionLocal
from sqlalchemy import text

router = APIRouter()

class JobRequest(BaseModel):
    title: str
    company: str
    location: str
    skills: str
    apply_url: str

@router.post("/add")
def add_job(req: JobRequest):

    db = SessionLocal()

    db.execute(
        text(
            """
            INSERT INTO jobs
            (
                title,
                company,
                location,
                skills,
                apply_url
            )
            VALUES
            (
                :title,
                :company,
                :location,
                :skills,
                :apply_url
            )
            """
        ),
        {
            "title": req.title,
            "company": req.company,
            "location": req.location,
            "skills": req.skills,
            "apply_url": req.apply_url
        }
    )

    db.commit()
    db.close()

    return {
        "message": "Job added successfully"
    }

@router.get("/list")
def list_jobs():

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
            ORDER BY id DESC
            """
        )
    )

    rows = result.fetchall()

    db.close()

    return [
        {
            "id": row[0],
            "title": row[1],
            "company": row[2],
            "location": row[3],
            "skills": row[4],
            "apply_url": row[5]
        }
        for row in rows
    ]
