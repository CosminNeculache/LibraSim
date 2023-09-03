import os
from datetime import datetime, timedelta
from dotenv import load_dotenv
from classes.library import Library
from classes.send_email import SendEmail
from classes.librarian import Librarian
from classes.physical_book import PhysicalBook

load_dotenv()
password = os.getenv("GMAIL_PASSWORD")

if __name__ == '__main__':

    # Creating an instance of the Library class:
    library = Library(None, None)

    # Creating an instance of the Librarian class:
    librarian = Librarian('Constantin', 'Ion', 50, "cosmin.neculache@gmail.com", datetime(2018, 12, 2), library)

    # Creating an instance of the SendEmail class:
    email_sender = SendEmail("smtp.gmail.com", 587, librarian.email, password)

    # Initialise the library instance with the librarian and email_sender attributes:
    library = Library(librarian, email_sender)

    # Creating instances of the PhysicalBooks class and adding them to the library list of books:
    book1 = PhysicalBook("Fahrenheit 451", "Ray Bradbury", "Shelf 2", "available", "Art", library)
    book2 = PhysicalBook("1984", "George Orwell", "Shelf 1", "available", "Secker & Warburg", library)
    book3 = PhysicalBook("To Kill a Mockingbird", "Harper Lee", "Shelf 3", "available", "J. B. Lippincott & Co."
                         , library)
    book4 = PhysicalBook("The Great Gatsby", "F. Scott Fitzgerald", "Shelf 4", "available", "Charles Scribner's Sons"
                         , library)
    book5 = PhysicalBook("Pride and Prejudice", "Jane Austen", "Shelf 5", "available", "T. Egerton, Whitehall", library)
    book6 = PhysicalBook("Brave New World", "Aldous Huxley", "Shelf 6", "available", "Chatto & Windus", library)

    # Creating instances of the Member class and adding them to the library list of members:
    new_member1 = library.register_member('Holmes', 'Sherlock', 45, 'sherlock@example.com', '001')
    new_member2 = library.register_member('John', 'Snow', 47, 'john@example.com', '002')
    new_member3 = library.register_member('Sam', 'Smith', 33, 'sam@example.com', '003')

    # Checking if the books are available for borrowing:
    if librarian.check_disponibility(book1):
        # Borrowing book for member1:
        new_member1.borrow_book(book1)

    if librarian.check_disponibility(book3):
        # Borrowing book for member2:
        new_member2.borrow_book(book3)

    if librarian.check_disponibility(book6):
        # Borrowing book for member1:
        new_member1.borrow_book(book6)

    # Returning books to library:
    new_member1.return_book(book1)
    new_member2.return_book(book3)

    # Manually changing book6 return_date to check overdue books email send:
    book6.return_date = datetime.now() - timedelta(weeks=4)

    # Printing library members:
    library.print_members()

    # Printing library books:
    library.print_books()

    # Printing library borrowed books:
    print("Borrowed books: ", library.get_borrowed_books())

    # Printing library overdue books:
    print("Overdue books: ", library.get_overdue_books())

    # Send overdue books email:
    library.send_overdue_emails()
