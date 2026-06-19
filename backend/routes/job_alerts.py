from fastapi import APIRouter
from pydantic import BaseModel

from database import SessionLocal
from sqlalchemy import text

from services.token_service import decode_token
from services.email_service import send_email

router = APIRouter()


class SubscribeRequest(BaseModel):
    token: str


@router.post("/subscribe")
def subscribe(req: SubscribeRequest):

    payload = decode_token(
        req.token
    )

    user_id = payload["user_id"]
    email = payload["email"]

    db = SessionLocal()

    db.execute(
        text(
            """
            INSERT INTO user_alerts
            (
                user_id,
                email,
                enabled
            )
            VALUES
            (
                :user_id,
                :email,
                TRUE
            )
            """
        ),
        {
            "user_id": user_id,
            "email": email
        }
    )

    db.commit()
    db.close()

    return {
        "message": "Email alerts enabled"
    }


class TestEmailRequest(BaseModel):
    email: str


@router.post("/send-test")
def send_test(req: TestEmailRequest):

    send_email(
        req.email,
        "AI Job Assistant Test",
        "Email notifications are working."
    )

    return {
        "message": "Test email sent"
    }


@router.get("/status/{token}")
def status(token):

    payload = decode_token(
        token
    )

    user_id = payload["user_id"]

    db = SessionLocal()

    result = db.execute(
        text(
            """
            SELECT enabled
            FROM user_alerts
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
            "enabled": False
        }

    return {
        "enabled": row[0]
    }
