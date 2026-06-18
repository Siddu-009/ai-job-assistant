from fastapi import APIRouter
from fastapi.responses import FileResponse
import os

router = APIRouter()

@router.get("/pdf")
def download_pdf():

    filepath = "generated/generated_resume.pdf"

    if not os.path.exists(filepath):
        return {
            "error": "PDF not generated yet"
        }

    return FileResponse(
        filepath,
        filename="generated_resume.pdf",
        media_type="application/pdf"
    )

@router.get("/txt")
def download_txt():

    filepath = "generated/generated_resume.txt"

    if not os.path.exists(filepath):
        return {
            "error": "TXT not generated yet"
        }

    return FileResponse(
        filepath,
        filename="generated_resume.txt",
        media_type="text/plain"
    )
