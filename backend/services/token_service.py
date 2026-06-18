from jose import jwt

SECRET_KEY = "siddu-devops-ai-job-assistant"
ALGORITHM = "HS256"

def decode_token(token):

    payload = jwt.decode(
        token,
        SECRET_KEY,
        algorithms=[ALGORITHM]
    )

    return payload
