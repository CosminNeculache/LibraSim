from datetime import datetime
from datetime import timedelta


class Person:

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


class Member(Person):

    def __init__(self, first_name, last_name, age, member_id, borrowed_books):
        super().__init__(first_name, last_name, age)
        self.member_id = member_id
        self.borrowed_books = borrowed_books

    def borrow_book(self, physical_book):
        self.borrowed_books.append(physical_book)
        physical_book.return_date += timedelta(weeks=4)

    def return_book(self, physical_book):
        self.borrowed_books.remove(physical_book)
        physical_book.return_date = datetime.now()


class Librarian(Person):

    def __init__(self, first_name, last_name, age, employment_date):
        super().__init__(first_name, last_name, age)
        self.employment_date = employment_date

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


class PhysicalBook(Book):

    def __init__(self, title, writer, shelf, status, publishing_house):
        super().__init__(title, writer)
        self.shelf = shelf
        self.status = status
        self.publishing_house = publishing_house
        self.return_date = datetime.now()
