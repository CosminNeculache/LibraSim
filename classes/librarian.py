from .person import Person


class Librarian(Person):
    def __init__(self, first_name, last_name, age, email, employment_date, library):
        super().__init__(first_name, last_name, age, email)
        self.employment_date = employment_date
        self.library = library

    def check_disponibility(self, physical_book):
        if physical_book.status == "available":
            print(f"The book {physical_book.title} written by {physical_book.writer} it's available.")
            return True
        else:
            print(f"The book {physical_book.title} written by {physical_book.writer} it's not available.")
            return False

    def __repr__(self):
        return f"Librarian('{self.first_name}', '{self.last_name}', {self.age}, {self.employment_date})"
