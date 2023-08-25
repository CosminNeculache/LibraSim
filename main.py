from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
from datetime import timedelta
from datetime import datetime
import smtplib
import os

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
        library.register_member(self)

    def borrow_book(self, physical_book):
        self.borrowed_books.append(physical_book)
        physical_book.return_date -= timedelta(weeks=4)
        physical_book.status = "unavailable"
        physical_book.borrowed_to = self.member_id

    def return_book(self, physical_book):
        self.borrowed_books.remove(physical_book)
        physical_book.return_date = datetime.now()
        physical_book.status = "available"
        physical_book.borrowed_to = None

    def __repr__(self):
        return self.first_name + self.last_name


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


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self, book):
        self.books.append(book)

    def register_member(self, member):
        self.members.append(member)

    def print_books(self):
        print("List of books:")
        for book in self.books:
            print(book.title)

    def print_members(self):
        print("List of members:")
        for member in self.members:
            print(member.first_name, member.last_name)

    def get_borrowed_books(self):
        borrowed_books = []
        for member in self.members:
            borrowed_books.extend(member.borrowed_books)
        return borrowed_books

    def get_overdue_books(self):
        overdue_books = []
        for member in self.members:
            for book in member.borrowed_books:
                if book.return_date < datetime.now():
                    overdue_books.append((member, book))
        return overdue_books

    def send_overdue_emails(self):
        for member, book in self.get_overdue_books():
            subject = "Overdue Book Notice"
            body = (f"Dear {member.first_name},\n\nWe hope this email finds you well. We wanted to remind you that the"
                    f" following book is currently overdue:\n\nBook Title: {book.title}\nAuthor: {book.writer}.\n"
                    f"Due Date:{book.return_date}\n\nWe kindly request that you return the book to the library at your "
                    f"earliest convenience. If you've already returned the book, please accept our apologies for any "
                    f" inconvenience this reminder may have caused. Overdue items prevent other library patrons from "
                    f"enjoying the same materials, and we strive to ensure equitable access to all our resources. "
                    f"Please help us by returning the book promptly. If you have any questions or concerns, please feel"
                    f" free to reply to this email or contact our library staff.\n\nThank you for your understanding "
                    f"and cooperation.\n\nSincerely,\n{librarian.first_name} {librarian.last_name}\nLibraSim")
            email_sender.send_email(member.email, subject, body)


class Book:

    def __init__(self, title, writer):
        self.title = title
        self.writer = writer

    def __repr__(self):
        return self.title


class PhysicalBook(Book):

    def __init__(self, title, writer, shelf, status, publishing_house, return_allert=False):
        super().__init__(title, writer)
        self.shelf = shelf
        self.status = status
        self.publishing_house = publishing_house
        self.return_date = datetime.now()
        self.borrowed_to = None
        self.return_allert = return_allert
        library.add_book(self)

    def check_return_date(self):
        if self.return_date < datetime.now():
            self.return_allert = True
        else:
            self.return_allert = False


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
    library = Library()
    book1 = PhysicalBook("Fahrenheit 451", "Ray Bradbury", "Shelf 2", "available", "Art")
    book2 = PhysicalBook("1984", "George Orwell", "Shelf 1", "available", "Secker & Warburg")
    book3 = PhysicalBook("To Kill a Mockingbird", "Harper Lee", "Shelf 3", "available", "J. B. Lippincott & Co.")
    book4 = PhysicalBook("The Great Gatsby", "F. Scott Fitzgerald", "Shelf 4", "available", "Charles Scribner's Sons")
    book5 = PhysicalBook("Pride and Prejudice", "Jane Austen", "Shelf 5", "available", "T. Egerton, Whitehall")
    book6 = PhysicalBook("Brave New World", "Aldous Huxley", "Shelf 6", "available", "Chatto & Windus")

    librarian = Librarian('Constantin', 'Ion', '50', datetime(2018, 12, 2))
    email_sender = Email("smtp.gmail.com", 587, "cosmin.neculache@gmail.com", password)

    new_member1 = librarian.register_member('Cosmin', 'Neculache', 26, '001', 'lordrush12@gmail.com')
    new_member2 = librarian.register_member('John', 'Snow', 47, '002', 'john@example.com')
    new_member3 = librarian.register_member('Sam', 'Smith', 33, '003', 'sam@example.com')

    if librarian.check_disponibility(book1):
        new_member1.borrow_book(book1)

    # if librarian.check_disponibility(book2):
    #     new_member1.borrow_book(book2)

    # if librarian.check_disponibility(book3):
    #     new_member2.borrow_book(book3)
    #
    # if librarian.check_disponibility(book5):
    #     new_member3.borrow_book(book5)
    #
    # if librarian.check_disponibility(book3):
    #     new_member3.borrow_book(book3)

    all_borrowed_books = library.get_borrowed_books()
    print("borrowed books", all_borrowed_books)
    overdue_books = library.get_overdue_books()

    print(overdue_books)
    library.send_overdue_emails()


    # print(new_member.borrowed_books)
    # print(book1.borrowed_to)
    # print(book2.borrowed_to)
    # if book1.return_date < datetime.now():
    #     email_sender.send_email("lordrush12@gmail.com", "Overdue Notice", "This is a test Email.")
