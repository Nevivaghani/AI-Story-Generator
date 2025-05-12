import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_HOST = "smtp.gmail.com"  # Replace with your SMTP server
EMAIL_PORT = 587
EMAIL_ADDRESS = "nevivaghani793@gmail.com"
EMAIL_PASSWORD = "kvec hvon dtff zonw"

def send_email_otp(email: str, otp: str):
    subject = "Your OTP for Login"
    body = f"Your OTP for login is: {otp}\n\nDo not share this with anyone."
    
    msg = MIMEMultipart()
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.sendmail(EMAIL_ADDRESS, email, msg.as_string())
        server.quit()
        print(f"OTP sent successfully to {email}")
    except Exception as e:
        print(f"Error sending OTP: {e}")
