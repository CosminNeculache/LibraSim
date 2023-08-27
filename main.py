import os
from datetime import datetime
from dotenv import load_dotenv

from classes.library import Library
from classes.send_email import SendEmail
from classes.librarian import Librarian
from classes.physical_book import PhysicalBook

load_dotenv()
password = os.getenv("GMAIL_PASSWORD")

if __name__ == '__main__':
    library = Library()
    book1 = PhysicalBook("Fahrenheit 451", "Ray Bradbury", "Shelf 2", "available", "Art")
    book2 = PhysicalBook("1984", "George Orwell", "Shelf 1", "available", "Secker & Warburg")
    book3 = PhysicalBook("To Kill a Mockingbird", "Harper Lee", "Shelf 3", "available", "J. B. Lippincott & Co.")
    book4 = PhysicalBook("The Great Gatsby", "F. Scott Fitzgerald", "Shelf 4", "available", "Charles Scribner's Sons")
    book5 = PhysicalBook("Pride and Prejudice", "Jane Austen", "Shelf 5", "available", "T. Egerton, Whitehall")
    book6 = PhysicalBook("Brave New World", "Aldous Huxley", "Shelf 6", "available", "Chatto & Windus")
    #
    librarian = Librarian('Constantin', 'Ion', '50', datetime(2018, 12, 2))
    email_sender = SendEmail("smtp.gmail.com", 587, "cosmin.neculache@gmail.com", password)

    new_member1 = librarian.register_member('Cosmin', 'Neculache', 26, '001', 'lordrush12@gmail.com')
    new_member2 = librarian.register_member('John', 'Snow', 47, '002', 'john@example.com')
    new_member3 = librarian.register_member('Sam', 'Smith', 33, '003', 'sam@example.com')
    #
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
    #
    print(overdue_books)
    library.send_overdue_emails()




    # print(new_member.borrowed_books)
    # print(book1.borrowed_to)
    # print(book2.borrowed_to)
    # if book1.return_date < datetime.now():
    #     email_sender.send_email("lordrush12@gmail.com", "Overdue Notice", "This is a test Email.")