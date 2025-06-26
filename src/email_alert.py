import smtplib
from email.mime.text import MIMEText
from config import SMTP_SERVER, SMTP_PORT, EMAIL_USERNAME, EMAIL_PASSWORD, ADMIN_EMAIL

def send_alert(incident):
    subject = f"🚨 {incident['type']} Incident Detected"
    body = f"""
Incident ID: {incident['id']}
Type: {incident['type']}
User Affected: {incident['user']}
Detected On: {incident['detected_on']}

Action Required: Please investigate. The user will be locked after 5 days if unresolved.
"""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = EMAIL_USERNAME
    msg['To'] = ADMIN_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USERNAME, ADMIN_EMAIL, msg.as_string())
