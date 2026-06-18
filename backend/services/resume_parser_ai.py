import re

def extract_resume_details(text):

    email = ""

    phone = ""

    email_match = re.search(
        r'[\w\.-]+@[\w\.-]+',
        text
    )

    if email_match:
        email = email_match.group()

    phone_match = re.search(
        r'\d{10}',
        text
    )

    if phone_match:
        phone = phone_match.group()

    return {
        "email": email,
        "phone": phone
    }
