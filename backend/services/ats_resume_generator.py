import requests

OLLAMA_URL = "http://ollama:11434/api/generate"


def generate_ats_content(
    resume_data,
    job_description
):

    prompt = f"""
Rewrite ONLY the professional summary.

Job Description:
{job_description}

Candidate Skills:
{resume_data.get("skills","")}

Candidate Projects:
{resume_data.get("projects","")}

Rules:
- Maximum 4 lines
- Maximum 80 words
- ATS optimized
- No headings
- No explanations
- No markdown
- Return ONLY summary text
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"].strip()
