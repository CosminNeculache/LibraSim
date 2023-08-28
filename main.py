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

    email_sender = SendEmail("smtp.gmail.com", 587, "cosmin.neculache@gmail.com", password)
    library = Library(None, email_sender)
    librarian = Librarian('Constantin', 'Ion', '50', "constantin.ion@test.com", datetime(2018, 12, 2), library)

    book1 = PhysicalBook("Fahrenheit 451", "Ray Bradbury", "Shelf 2", "available", "Art", library)
    book2 = PhysicalBook("1984", "George Orwell", "Shelf 1", "available", "Secker & Warburg", library)
    book3 = PhysicalBook("To Kill a Mockingbird", "Harper Lee", "Shelf 3", "available", "J. B. Lippincott & Co."
                         , library)
    book4 = PhysicalBook("The Great Gatsby", "F. Scott Fitzgerald", "Shelf 4", "available", "Charles Scribner's Sons"
                         , library)
    book5 = PhysicalBook("Pride and Prejudice", "Jane Austen", "Shelf 5", "available", "T. Egerton, Whitehall", library)
    book6 = PhysicalBook("Brave New World", "Aldous Huxley", "Shelf 6", "available", "Chatto & Windus", library)

    new_member1 = library.register_member('Cosmin', 'Neculache', 26, 'lordrush12@gmail.com', '001')
    new_member2 = library.register_member('John', 'Snow', 47, 'john@example.com', '002')
    new_member3 = library.register_member('Sam', 'Smith', 33, 'sam@example.com', '003')

    if librarian.check_disponibility(book1):
        new_member1.borrow_book(book1)

    library.print_members()
    library.print_books()

    print(library.get_borrowed_books())

    if librarian.check_disponibility(book2):
        new_member1.borrow_book(book2)

    if librarian.check_disponibility(book3):
        new_member2.borrow_book(book3)
    #
    if librarian.check_disponibility(book5):
        new_member3.borrow_book(book5)
    #
    if librarian.check_disponibility(book3):
        new_member3.borrow_book(book3)

    print("Borrowed books:", library.get_borrowed_books())
    print("Overdue books:", library.get_overdue_books())

    # library.send_overdue_emails()

