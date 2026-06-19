from database import SessionLocal
from sqlalchemy import text

def recommend_jobs(user_skills):

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
            """
        )
    )

    jobs = result.fetchall()

    recommendations = []

    resume_skills = [
        skill.strip().lower()
        for skill in user_skills
    ]

    print("Resume Skills:", resume_skills)

    for job in jobs:

        job_skills = [
            skill.strip().lower()
            for skill in job[4].split(",")
        ]

        print("Job Skills:", job_skills)

        matched = len(
            set(resume_skills) &
            set(job_skills)
        )

        score = int(
            (matched / len(job_skills)) * 100
        )

        print(
            f"Job={job[1]} Matched={matched} Score={score}"
        )

        recommendations.append(
            {
                "job_id": job[0],
                "title": job[1],
                "company": job[2],
                "location": job[3],
                "score": score,
                "apply_url": job[5],
                "reason": "Debug Mode"
            }
        )

    db.close()

    recommendations.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    print("Recommendations:", recommendations)

    return recommendations
