import smtplib

from email.mime.text import MIMEText


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587

EMAIL = "siddhardhamaddula37791@gmail.com"
PASSWORD = "ciqv jqdq gtbe vnaj"


def send_email(
    recipient,
    subject,
    body
):

    msg = MIMEText(body)

    msg["Subject"] = subject
    msg["From"] = EMAIL
    msg["To"] = recipient

    server = smtplib.SMTP(
        SMTP_SERVER,
        SMTP_PORT
    )

    server.starttls()

    server.login(
        EMAIL,
        PASSWORD
    )

    server.sendmail(
        EMAIL,
        recipient,
        msg.as_string()
    )

    server.quit()
