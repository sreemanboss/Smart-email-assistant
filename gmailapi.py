import smtplib

# Mailtrap SMTP credentials (from your Integrations page)
SMTP_SERVER = "sandbox.smtp.mailtrap.io"
SMTP_PORT = 2525
USERNAME = "121a246be3cf83"         # Replace with your real Mailtrap username
PASSWORD = "8f05674da089be"     # Replace with your real Mailtrap password

# Email details
sender_email = "from@example.com"
receiver_email = "to@example.com"

# Email content
message = f"""\
Subject: Hello from Smart Email Assistant

To: {receiver_email}
From: {sender_email}

This is a test email sent from our college project using Mailtrap SMTP.
"""

# Send the email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(USERNAME, PASSWORD)
        server.sendmail(sender_email, receiver_email, message)
        print("✅ Email sent and captured in Mailtrap inbox!")
except Exception as e:
    print("❌ Failed to send email:", e)
