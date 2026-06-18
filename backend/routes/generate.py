from fastapi import APIRouter
from pydantic import BaseModel
from services.ollama_resume import generate_resume
from services.pdf_generator import create_pdf
from services.resume_storage import save_resume
from services.token_service import decode_token
import os

router = APIRouter()

GENERATED_DIR = "generated"

os.makedirs(GENERATED_DIR, exist_ok=True)

class GenerateRequest(BaseModel):
    token: str
    resume: str
    job_description: str

@router.post("/")
def generate(req: GenerateRequest):

    payload = decode_token(
        req.token
    )

    user_id = payload["user_id"]

    print(f"User ID: {user_id}")

    result = generate_resume(
        req.resume,
        req.job_description
    )

    txt_path = os.path.join(
        GENERATED_DIR,
        "generated_resume.txt"
    )

    with open(
        txt_path,
        "w",
        encoding="utf-8"
    ) as f:
        f.write(result)

    print(f"TXT file saved: {txt_path}")

    pdf_path = os.path.join(
        GENERATED_DIR,
        "generated_resume.pdf"
    )

    create_pdf(
        result,
        pdf_path
    )

    print(f"PDF file saved: {pdf_path}")

    save_resume(
        user_id,
        req.job_description,
        result
    )

    print("Resume saved to PostgreSQL")

    return {
        "status": "success",
        "user_id": user_id,
        "generated_resume": result,
        "txt_file": "generated_resume.txt",
        "pdf_file": "generated_resume.pdf"
    }
