from fastapi import APIRouter
from pydantic import BaseModel
from services.token_service import decode_token
from database import SessionLocal
from sqlalchemy import text

router = APIRouter()

class HistoryRequest(BaseModel):
    token: str

@router.post("/")
def get_history(req: HistoryRequest):

    payload = decode_token(
        req.token
    )

    user_id = payload["user_id"]

    db = SessionLocal()

    result = db.execute(
        text(
            """
            SELECT
                id,
                created_at
            FROM generated_resumes
            WHERE user_id = :user_id
            ORDER BY id DESC
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
            "id": row[0],
            "created_at": str(row[1])
        }
        for row in rows
    ]
