from fastapi import APIRouter
from pydantic import BaseModel

from database import SessionLocal
from sqlalchemy import text

from services.token_service import decode_token

router = APIRouter()


class SaveJobRequest(BaseModel):
    token: str
    job_id: int


@router.post("/add")
def save_job(req: SaveJobRequest):

    payload = decode_token(
        req.token
    )

    user_id = payload["user_id"]

    db = SessionLocal()

    db.execute(
        text(
            """
            INSERT INTO saved_jobs
            (
                user_id,
                job_id
            )
            VALUES
            (
                :user_id,
                :job_id
            )
            """
        ),
        {
            "user_id": user_id,
            "job_id": req.job_id
        }
    )

    db.commit()
    db.close()

    return {
        "message": "Job saved successfully"
    }


@router.get("/{token}")
def get_saved_jobs(token):

    payload = decode_token(
        token
    )

    user_id = payload["user_id"]

    db = SessionLocal()

    result = db.execute(
        text(
            """
            SELECT
                s.id,
                j.title,
                j.company,
                j.location,
                j.apply_url
            FROM saved_jobs s
            JOIN jobs j
                ON s.job_id = j.id
            WHERE s.user_id = :user_id
            ORDER BY s.id DESC
            """
        ),
        {
            "user_id": user_id
        }
    )

    rows = result.fetchall()

    db.close()

    return [
        {
            "saved_id": row[0],
            "title": row[1],
            "company": row[2],
            "location": row[3],
            "apply_url": row[4]
        }
        for row in rows
    ]


@router.delete("/{saved_id}")
def delete_saved_job(saved_id: int):

    db = SessionLocal()

    db.execute(
        text(
            """
            DELETE FROM saved_jobs
            WHERE id = :id
            """
        ),
        {
            "id": saved_id
        }
    )

    db.commit()
    db.close()

    return {
        "message": "Saved job removed successfully"
    }
