from fastapi import APIRouter
from database import SessionLocal
from sqlalchemy import text

router = APIRouter()

@router.post("/sample")
def import_jobs():

    jobs = [
        {
            "title": "DevOps Engineer",
            "company": "Amazon",
            "location": "Hyderabad",
            "skills": "AWS,Docker,Kubernetes,Terraform",
            "apply_url": "https://amazon.jobs"
        },
        {
            "title": "Cloud Engineer",
            "company": "Microsoft",
            "location": "Bangalore",
            "skills": "AWS,Azure,Docker,Kubernetes",
            "apply_url": "https://careers.microsoft.com"
        },
        {
            "title": "Site Reliability Engineer",
            "company": "Google",
            "location": "Remote",
            "skills": "Linux,Kubernetes,GCP,Docker",
            "apply_url": "https://careers.google.com"
        }
    ]

    db = SessionLocal()

    for job in jobs:

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
            job
        )

    db.commit()
    db.close()

    return {
        "message": "Sample jobs imported",
        "count": len(jobs)
    }
