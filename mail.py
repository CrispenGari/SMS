import smtplib, ssl
from keys import Keys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class SmtpConfig(object):
    FROM = Keys.EMAIL
    PORT = 465  # For SSL
    SMTP_SERVER = "smtp.gmail.com"
    PASSWORD = Keys.PASSWORD


def sendPlainEmail(to: str, body: str, subject: str):
    message = f"""\
    Subject: {subject}
    {body}
    """
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(
        SmtpConfig.SMTP_SERVER, SmtpConfig.PORT, context=context
    ) as server:
        server.login(SmtpConfig.FROM, SmtpConfig.PASSWORD)
        server.sendmail(SmtpConfig.FROM, to, message)


def sendFancyEmail(to: str, body: str, subject: str):
    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = SmtpConfig.FROM
    message["To"] = to

    html = f"""
    <html>
    <body>
        <p>Hi,<br>
        {body}<br>

    </body>
    </html>
    """
    part2 = MIMEText(html, "html")
    message.attach(part2)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", SmtpConfig.PORT, context=context) as server:
        server.login(SmtpConfig.FROM, SmtpConfig.PASSWORD)
        server.sendmail(SmtpConfig.FROM, to, message.as_string())


# sendPlainEmail("crispengari@gmail.com", "Hi", "Testing")
sendFancyEmail("crispengari@gmail.com", "Hi", "Testing")
