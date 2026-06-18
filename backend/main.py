from fastapi import FastAPI

from cors import setup_cors

from routes.auth import router as auth_router
from routes.resume import router as resume_router
from routes.job import router as job_router
from routes.jobs import router as jobs_router
from routes.match import router as match_router
from routes.generate import router as generate_router
from routes.download import router as download_router
from routes.history import router as history_router
from routes.resume_details import router as resume_details_router
from routes.job_matcher import router as job_matcher_router
from routes.auto_match import router as auto_match_router
from routes.smart_match import router as smart_match_router

app = FastAPI(
    title="AI Job Assistant",
    version="1.0.0"
)

setup_cors(app)

app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

app.include_router(
    resume_router,
    prefix="/resume",
    tags=["Resume"]
)

app.include_router(
    job_router,
    prefix="/job",
    tags=["Job Description"]
)

app.include_router(
    jobs_router,
    prefix="/jobs",
    tags=["Jobs"]
)

app.include_router(
    match_router,
    prefix="/match",
    tags=["Match"]
)

app.include_router(
    generate_router,
    prefix="/generate",
    tags=["AI Resume"]
)

app.include_router(
    download_router,
    prefix="/download",
    tags=["Download"]
)

app.include_router(
    history_router,
    prefix="/history",
    tags=["History"]
)

app.include_router(
    resume_details_router,
    prefix="/resume-details",
    tags=["Resume Details"]
)

app.include_router(
    job_matcher_router,
    prefix="/job-matcher",
    tags=["Job Matcher"]
)

app.include_router(
    auto_match_router,
    prefix="/auto-match",
    tags=["Auto Match"]
)

app.include_router(
    smart_match_router,
    prefix="/smart-match",
    tags=["Smart Match"]
)

@app.get("/")
def root():
    return {
        "message": "AI Job Assistant API Running",
        "status": "success",
        "version": "1.0.0"
    }
