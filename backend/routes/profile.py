from fastapi import APIRouter
from pydantic import BaseModel

from database import SessionLocal
from sqlalchemy import text

from services.token_service import decode_token

router = APIRouter()


class ProfileRequest(BaseModel):
    token: str


@router.post("/")
def get_profile(req: ProfileRequest):

    payload = decode_token(
        req.token
    )

    user_id = payload["user_id"]

    db = SessionLocal()

    user = db.execute(
        text(
            """
            SELECT
                id,
                name,
                email,
                created_at
            FROM users
            WHERE id = :id
            """
        ),
        {
            "id": user_id
        }
    ).fetchone()

    resume_count = db.execute(
        text(
            """
            SELECT COUNT(*)
            FROM resumes
            WHERE user_id = :id
            """
        ),
        {
            "id": user_id
        }
    ).scalar()

    generated_count = db.execute(
        text(
            """
            SELECT COUNT(*)
            FROM generated_resumes
            WHERE user_id = :id
            """
        ),
        {
            "id": user_id
        }
    ).scalar()

    db.close()

    if not user:

        return {
            "error": "User not found"
        }

    return {
        "id": user[0],
        "name": user[1],
        "email": user[2],
        "created_at": str(user[3]),
        "uploaded_resumes": resume_count,
        "generated_resumes": generated_count
    }
