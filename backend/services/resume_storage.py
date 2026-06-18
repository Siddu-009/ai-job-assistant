from database import SessionLocal
from sqlalchemy import text

def save_resume(
    user_id,
    job_description,
    generated_resume
):

    db = SessionLocal()

    db.execute(
        text(
            """
            INSERT INTO generated_resumes
            (
                user_id,
                job_description,
                generated_resume
            )
            VALUES
            (
                :user_id,
                :job_description,
                :generated_resume
            )
            """
        ),
        {
            "user_id": user_id,
            "job_description": job_description,
            "generated_resume": generated_resume
        }
    )

    db.commit()

    db.close()
