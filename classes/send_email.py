from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import logging


class SendEmail:
    def __init__(self, smtp_server, smtp_port, sender_email, password):
        self.smtp_server = smtp_server
        self.smtp_port = smtp_port
        self.sender_email = sender_email
        self.password = password

        self.logger = logging.getLogger("SendEmail")
        self.logger.setLevel(logging.ERROR)

    def send_email(self, receiver_email, subject, body):
        try:
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = receiver_email
            message["Subject"] = subject
            message.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, message.as_string())
                self.logger.info(f"Email sent successfully to {receiver_email}")
        except Exception as e:
            self.logger.error(f"Error sending email to {receiver_email}: {str(e)}")
            raise

    def __repr__(self):
        return f"Email('{self.smtp_server}', {self.smtp_port}, '{self.sender_email}')"
