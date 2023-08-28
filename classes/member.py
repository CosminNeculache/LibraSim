from .person import Person
from datetime import timedelta, datetime


class Member(Person):

    def __init__(self, first_name, last_name, age, email, member_id, borrowed_books):
        super().__init__(first_name, last_name, age, email)
        self.member_id = member_id
        self.borrowed_books = borrowed_books


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
        return f"{self.first_name} {self.last_name}"

