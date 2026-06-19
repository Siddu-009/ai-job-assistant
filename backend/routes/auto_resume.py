from fastapi import APIRouter
from pydantic import BaseModel

from services.parser import extract_text

from services.resume_parser_ai import (
    extract_resume_details
)

from services.ats_resume_generator import (
    generate_ats_content
)

from services.resume_builder import (
    build_resume
)

router = APIRouter()


class AutoResumeRequest(BaseModel):

    filename: str
    job_description: str


@router.post("/")
def auto_resume(req: AutoResumeRequest):

    filepath = f"uploads/{req.filename}"

    resume_text = extract_text(
        filepath
    )

    details = extract_resume_details(
        resume_text
    )

    ats_content = generate_ats_content(
        details,
        req.job_description
    )

    build_resume(
        name=details["name"],
        email=details["email"],
        phone=details["phone"],
        linkedin=details["linkedin"],
        github=details["github"],
        summary=ats_content,
        skills=details["skills"],
        projects=details["projects"],
        certifications="DevOps Training, Naresh IT",
        education=details["education"],
        output_file="generated/ats_resume.pdf"
    )

    return {
        "message": "ATS Resume Generated Successfully",
        "candidate": details["name"],
        "file": "ats_resume.pdf"
    }
