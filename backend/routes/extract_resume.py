from fastapi import APIRouter
from pydantic import BaseModel

from services.parser import extract_text
from services.resume_parser_ai import (
    extract_resume_details
)

router = APIRouter()

class ResumeExtractRequest(BaseModel):
    filename: str

@router.post("/")
def extract_resume(req: ResumeExtractRequest):

    filepath = f"uploads/{req.filename}"

    text = extract_text(
        filepath
    )

    details = extract_resume_details(
        text
    )

    return details
