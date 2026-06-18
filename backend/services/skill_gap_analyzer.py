KNOWN_SKILLS = [
    "aws",
    "docker",
    "kubernetes",
    "terraform",
    "jenkins",
    "ansible",
    "linux",
    "github actions",
    "git",
    "python",
    "prometheus",
    "grafana",
    "eks",
    "ec2",
    "s3",
    "iam",
    "route53",
    "rds",
    "argocd",
    "helm",
    "devops"
]


def analyze_skill_gap(
    resume_text,
    job_description
):

    resume_text = resume_text.lower()
    job_description = job_description.lower()

    resume_skills = []
    job_skills = []

    for skill in KNOWN_SKILLS:

        if skill in resume_text:
            resume_skills.append(skill)

        if skill in job_description:
            job_skills.append(skill)

    matched = list(
        set(resume_skills)
        &
        set(job_skills)
    )

    missing = list(
        set(job_skills)
        -
        set(resume_skills)
    )

    if len(job_skills) == 0:
        score = 0
    else:
        score = int(
            (
                len(matched)
                /
                len(job_skills)
            ) * 100
        )

    recommendations = []

    for skill in missing:
        recommendations.append(
            f"Learn {skill.title()}"
        )

    return {
        "match_score": score,
        "matched_skills": matched,
        "missing_skills": missing,
        "recommendations": recommendations
    }
