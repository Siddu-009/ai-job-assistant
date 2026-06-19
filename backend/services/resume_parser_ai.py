import re


def extract_resume_details(text):

    details = {
        "name": "",
        "email": "",
        "phone": "",
        "linkedin": "",
        "github": "",
        "summary": "",
        "skills": "",
        "projects": "",
        "education": "",
        "strengths": ""
    }

    lines = text.splitlines()

    # Name

    for line in lines:

        line = line.strip()

        if (
            line.isupper()
            and len(line) > 5
            and len(line) < 50
        ):
            details["name"] = line
            break

    # Email

    email_match = re.search(
        r'[\w\.-]+@[\w\.-]+',
        text
    )

    if email_match:
        details["email"] = email_match.group()

    # Phone

    phone_match = re.search(
        r'(\+91)?[\s\-]?\d{10}',
        text
    )

    if phone_match:
        details["phone"] = phone_match.group()

    # LinkedIn

    linkedin_match = re.search(
        r'linkedin\.com/[^\s|]+',
        text,
        re.IGNORECASE
    )

    if linkedin_match:
        details["linkedin"] = linkedin_match.group()

    # GitHub

    github_match = re.search(
        r'github\.com/[^\s|]+',
        text,
        re.IGNORECASE
    )

    if github_match:
        details["github"] = github_match.group()

    # Professional Summary

    if "PROFESSIONAL SUMMARY" in text:

        start = text.find(
            "PROFESSIONAL SUMMARY"
        )

        end = text.find(
            "TECHNICAL SKILLS"
        )

        if start != -1 and end != -1:

            details["summary"] = (
                text[start:end]
                .replace(
                    "PROFESSIONAL SUMMARY",
                    ""
                )
                .strip()
            )

    # Skills

    if "TECHNICAL SKILLS" in text:

        start = text.find(
            "TECHNICAL SKILLS"
        )

        end = text.find(
            "PROJECTS"
        )

        if start != -1 and end != -1:

            details["skills"] = (
                text[start:end]
                .replace(
                    "TECHNICAL SKILLS",
                    ""
                )
                .strip()
            )

    # Projects

    if "PROJECTS & HANDS-ON EXPERIENCE" in text:

        start = text.find(
            "PROJECTS & HANDS-ON EXPERIENCE"
        )

        end = text.find(
            "EDUCATION"
        )

        if start != -1 and end != -1:

            details["projects"] = (
                text[start:end]
                .replace(
                    "PROJECTS & HANDS-ON EXPERIENCE",
                    ""
                )
                .strip()
            )

    # Education

    if "EDUCATION" in text:

        start = text.find(
            "EDUCATION"
        )

        end = text.find(
            "STRENGTHS"
        )

        if start != -1 and end != -1:

            details["education"] = (
                text[start:end]
                .replace(
                    "EDUCATION",
                    ""
                )
                .strip()
            )

    # Strengths

    if "STRENGTHS" in text:

        start = text.find(
            "STRENGTHS"
        )

        if start != -1:

            details["strengths"] = (
                text[start:]
                .replace(
                    "STRENGTHS",
                    ""
                )
                .strip()
            )

    return details
