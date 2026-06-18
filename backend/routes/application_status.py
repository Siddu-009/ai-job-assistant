from fastapi import APIRouter
from pydantic import BaseModel

from database import SessionLocal
from sqlalchemy import text

router = APIRouter()

class StatusRequest(BaseModel):
    application_id: int
    status: str

@router.post("/update")
def update_status(req: StatusRequest):

    db = SessionLocal()

    db.execute(
        text(
            """
            UPDATE applications
            SET status = :status
            WHERE id = :id
            """
        ),
        {
            "status": req.status,
            "id": req.application_id
        }
    )

    db.commit()
    db.close()

    return {
        "message": "Status updated successfully"
    }


@router.get("/{application_id}")
def get_status(application_id: int):

    db = SessionLocal()

    result = db.execute(
        text(
            """
            SELECT
                id,
                status,
                created_at
            FROM applications
            WHERE id = :id
            """
        ),
        {
            "id": application_id
        }
    )

    row = result.fetchone()

    db.close()

    if not row:
        return {
            "error": "Application not found"
        }

    return {
        "application_id": row[0],
        "status": row[1],
        "created_at": str(row[2])
    }
