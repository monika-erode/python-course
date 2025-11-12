import smtplib
from email.mime.text import MIMEText

sender = "imeshmuthuraj2003@gmail.com"
receiver = "settlohari@example.com"
password = "HARI97880"  # Use App Password for Gmail

msg = MIMEText("Hello! This is a test email from Python.")
msg["Subject"] = "Python Email Test"
msg["From"] = sender
msg["To"] = receiver

with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender, password)
    server.send_message(msg)

print("Email sent successfully!")
