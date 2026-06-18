from fastapi import APIRouter
from pydantic import BaseModel

from services.resume_builder import build_resume

router = APIRouter()

class ResumeBuilderRequest(BaseModel):

    name: str
    email: str
    phone: str
    summary: str
    skills: str
    projects: str
    education: str

@router.post("/")
def create_resume(req: ResumeBuilderRequest):

    output_file = (
        "generated/professional_resume.pdf"
    )

    build_resume(
        req.name,
        req.email,
        req.phone,
        req.summary,
        req.skills,
        req.projects,
        req.education,
        output_file
    )

    return {
        "message": "Resume created successfully",
        "file": "professional_resume.pdf"
    }
