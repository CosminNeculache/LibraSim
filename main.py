from datetime import datetime
from datetime import timedelta
from dotenv import load_dotenv
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()
password = os.getenv("GMAIL_PASSWORD")


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Member(Person):

    def __init__(self, first_name, last_name, age, member_id, borrowed_books, email):
        super().__init__(first_name, last_name, age)
        self.member_id = member_id
        self.borrowed_books = borrowed_books
        self.email = email

    def borrow_book(self, physical_book):
        self.borrowed_books.append(physical_book)
        physical_book.return_date += timedelta(weeks=4)
        physical_book.status = "unavailable"
        physical_book.borrowed_to = self.member_id

    def return_book(self, physical_book):
        self.borrowed_books.remove(physical_book)
        physical_book.return_date = datetime.now()
        physical_book.status = "available"


class Librarian(Person):

    def __init__(self, first_name, last_name, age, employment_date):
        super().__init__(first_name, last_name, age)
        self.employment_date = employment_date

    def register_member(self, first_name, last_name, age, member_id, email):
        new_member = Member(first_name, last_name, age, member_id, [], email)
        return new_member

    def check_disponibility(self, physical_book):
        if physical_book.status == "available":
            print("The book " + physical_book.title + " written by "
                  + physical_book.writer + " it's available.")
            return True
        else:
            print("The book " + physical_book.title + " written by "
                  + physical_book.writer + " it's not available. ")
            return False


class Book:

    def __init__(self, title, writer):
        self.title = title
        self.writer = writer

    def __repr__(self):
        return self.title


class PhysicalBook(Book):

    def __init__(self, title, writer, shelf, status, publishing_house):
        super().__init__(title, writer)
        self.shelf = shelf
        self.status = status
        self.publishing_house = publishing_house
        self.return_date = datetime.now()
        self.borrowed_to = None


class Email:
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


if __name__ == '__main__':

    book1 = PhysicalBook("Fahrenheit 451", "Ray Bradbury", "Shelf 2", "available", "Art")
    book2 = PhysicalBook("1984", "George Orwell", "Shelf 1", "available", "Secker & Warburg")
    librarian = Librarian('Constantin', 'Ion', '50', datetime(2018, 12, 2))
    email_sender = Email("smtp.gmail.com", 587, "cosmin.neculache@gmail.com", password)

    new_member = librarian.register_member('Alice', 'Johnson', 30, '002', 'alice@example.com')
    print("New member registered:", new_member.first_name, new_member.last_name)

    if librarian.check_disponibility(book1):
        new_member.borrow_book(book1)

    print(new_member.borrowed_books)
    print(book1.borrowed_to)
    print(book2.borrowed_to)

    if book1.return_date > datetime.now():
        email_sender.send_email("lordrush12@gmail.com", "Overdue Notice", "This is a test Email.")
