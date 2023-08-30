from datetime import datetime
from LibraSim.classes.member import Member


class Library:
    def __init__(self, librarian, email_sender):
        self.books = []
        self.members = []
        self.librarian = librarian
        self.email_sender = email_sender

    def register_member(self, first_name, last_name, age, email, member_id):
        new_member = Member(first_name, last_name, age, email, member_id, [])
        self.members.append(new_member)
        return new_member

    def add_book(self, book):
        self.books.append(book)

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
        overdue_books = set()
        for member in self.members:
            for book in member.borrowed_books:
                if book.return_date < datetime.now():
                    overdue_books.add((member, book))
        return overdue_books

    def __repr__(self):
        return f"Library({len(self.books)} books, {len(self.members)} members)"

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
                    f"and cooperation.\n\nSincerely,\n{self.librarian.first_name} {self.librarian.last_name}\nLibraSim")
            self.email_sender.send_email(member.email, subject, body)
