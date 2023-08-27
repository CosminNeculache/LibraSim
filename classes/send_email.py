from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class SendEmail:
    def __init__(self, smtp_server, smtp_port, sender_email, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.password = password

    def send_email(self, receiver_email, subject, body):
        message = MIMEMultipart()
        message["From"] = self.sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(self.smtp_server, self.smtp_port)
        server.starttls()
        server.login(self.sender_email, self.password)
        server.sendmail(self.sender_email, receiver_email, message.as_string())
        server.quit()

    def __repr__(self):
        return f"Email('{self.smtp_server}', {self.smtp_port}, '{self.sender_email}')"
