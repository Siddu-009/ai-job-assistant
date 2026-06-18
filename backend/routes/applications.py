from fastapi import APIRouter
from pydantic import BaseModel

from database import SessionLocal
from sqlalchemy import text

from services.token_service import decode_token

router = APIRouter()

class ApplyRequest(BaseModel):
    token: str
    job_id: int

@router.post("/apply")
def apply(req: ApplyRequest):

    payload = decode_token(req.token)

    user_id = payload["user_id"]

    db = SessionLocal()

    db.execute(
        text(
            """
            INSERT INTO applications
            (
                user_id,
                job_id,
                status
            )
            VALUES
            (
                :user_id,
                :job_id,
                'Applied'
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
        "message": "Application submitted successfully"
    }

class ApplicationHistoryRequest(BaseModel):
    token: str

@router.post("/my-applications")
def my_applications(req: ApplicationHistoryRequest):

    payload = decode_token(req.token)

    user_id = payload["user_id"]

    db = SessionLocal()

    result = db.execute(
        text(
            """
            SELECT
                a.id,
                j.title,
                j.company,
                a.status,
                a.created_at
            FROM applications a
            JOIN jobs j
                ON a.job_id = j.id
            WHERE a.user_id = :user_id
            ORDER BY a.id DESC
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
            "application_id": row[0],
            "job_title": row[1],
            "company": row[2],
            "status": row[3],
            "created_at": str(row[4])
        }
        for row in rows
    ]
