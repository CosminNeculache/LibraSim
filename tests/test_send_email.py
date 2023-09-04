import unittest
from LibraSim.classes.send_email import SendEmail
from dotenv import load_dotenv
import logging
import os


class TestSendEmail(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        password = os.getenv("GMAIL_PASSWORD")
        self.sender_email = SendEmail("smtp.gmail.com", 587, "cosmin.neculache@gmail.com", password)

        self.logger = logging.getLogger("SendEmail")
        self.handler = logging.FileHandler("Log.log")
        self.formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        self.handler.setFormatter(self.formatter)
        self.logger.addHandler(self.handler)
        self.logger.setLevel(logging.ERROR)

    def test_send_email_init(self):
        self.assertEqual(self.sender_email.smtp_server, "smtp.gmail.com")
        self.assertEqual(self.sender_email.smtp_port, 587)
        self.assertEqual(self.sender_email.sender_email, "cosmin.neculache@gmail.com")
        self.assertIsNotNone(self.sender_email.password)

    def test_send_email_succes(self):
        receiver_email = "lordrush12@gmail.com"
        subject = "Test Email"
        body = "This is a test email."

        with self.assertLogs(logger=self.logger, level=logging.INFO):
            self.sender_email.send_email(receiver_email, subject, body)

    def test_send_email_failure(self):
        self.sender_email.smtp_server = "smtp.invalidserver.com"
        receiver_email = "receiver@example.com"
        subject = "Test Email"
        body = "This is a test email."
        self.logger.info("Test the custom logger")
        with self.assertLogs(logger=self.logger, level=logging.ERROR):
            with self.assertRaises(Exception):
                self.sender_email.send_email(receiver_email, subject, body)

    def test_send_email_repr(self):
        expected_repr = "Email('smtp.gmail.com', 587, 'cosmin.neculache@gmail.com')"
        self.assertEqual(repr(self.sender_email), expected_repr)


if __name__ == '__main__':
    unittest.main()
