import requests

OLLAMA_URL = "http://ollama:11434/api/generate"


def generate_reason(
    resume_skills,
    job_title,
    job_skills
):

    prompt = f"""
Resume Skills:
{', '.join(resume_skills)}

Job Title:
{job_title}

Required Skills:
{job_skills}

Explain in 2 short sentences why this job matches the candidate.
Keep it under 40 words.
"""

    try:

        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3",
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        if response.status_code == 200:

            return response.json().get(
                "response",
                "Good skill match."
            )

        return "Good skill match."

    except Exception:

        return "Your skills align well with this role."
