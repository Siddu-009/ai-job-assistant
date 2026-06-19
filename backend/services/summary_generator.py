import requests

OLLAMA_URL = "http://ollama:11434/api/generate"

def generate_summary(
    resume_text,
    job_description
):

    prompt = f"""
Generate ONLY a professional summary.

Resume:
{resume_text}

Job:
{job_description}

Rules:
- Maximum 5 lines
- ATS friendly
- No headings
- No explanation
- No bullet points
"""

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]
