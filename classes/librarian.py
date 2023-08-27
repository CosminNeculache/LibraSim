from .person import Person
from .member import Member


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

    def __repr__(self):
        return f"Librarian('{self.first_name}', '{self.last_name}', {self.age}, {self.employment_date})"
