import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from typing import Optional

class EmailService:
    def __init__(self):
        self.smtp_server = os.getenv("SMTP_SERVER", "smtp-relay.brevo.com")
        self.port = int(os.getenv("SMTP_PORT", 587))  
        self.username = os.getenv("EMAIL_NAME", "BREVO")
        self.password = os.getenv("EMAIL_PASSWORD", "")
        self.sender = os.getenv("EMAIL_SENDER")
        
        if not self.sender:
            raise ValueError("EMAIL_SENDER no está configurado en las variables de entorno")

    async def send_email(self, receiver_email: str, subject: str, html_content: str) -> bool:
      
        message = MIMEMultipart()
        message["From"] = self.sender
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(html_content, "html"))

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.starttls()
                if self.username and self.password:
                    server.login(self.username, self.password)
                server.sendmail(self.sender, receiver_email, message.as_string())
            return True
        except Exception as e:
            
            print(f"Error al enviar correo a {receiver_email}: {str(e)}")
            input()
            return False