from fastapi import APIRouter

from database import SessionLocal
from sqlalchemy import text

from services.token_service import decode_token

router = APIRouter()

@router.get("/{token}")
def dashboard(token):

    payload = decode_token(token)

    user_id = payload["user_id"]

    db = SessionLocal()

    applications = db.execute(
        text(
            """
            SELECT COUNT(*)
            FROM applications
            WHERE user_id = :user_id
            """
        ),
        {
            "user_id": user_id
        }
    ).scalar()

    interviews = db.execute(
        text(
            """
            SELECT COUNT(*)
            FROM applications
            WHERE user_id = :user_id
            AND status = 'Interview Scheduled'
            """
        ),
        {
            "user_id": user_id
        }
    ).scalar()

    selected = db.execute(
        text(
            """
            SELECT COUNT(*)
            FROM applications
            WHERE user_id = :user_id
            AND status = 'Selected'
            """
        ),
        {
            "user_id": user_id
        }
    ).scalar()

    rejected = db.execute(
        text(
            """
            SELECT COUNT(*)
            FROM applications
            WHERE user_id = :user_id
            AND status = 'Rejected'
            """
        ),
        {
            "user_id": user_id
        }
    ).scalar()

    recent_jobs = db.execute(
        text(
            """
            SELECT
                j.title,
                j.company,
                a.status
            FROM applications a
            JOIN jobs j
                ON a.job_id = j.id
            WHERE a.user_id = :user_id
            ORDER BY a.id DESC
            LIMIT 5
            """
        ),
        {
            "user_id": user_id
        }
    ).fetchall()

    db.close()

    return {
        "applications": applications,
        "interviews": interviews,
        "selected": selected,
        "rejected": rejected,
        "recent_jobs": [
            {
                "title": row[0],
                "company": row[1],
                "status": row[2]
            }
            for row in recent_jobs
        ]
    }
