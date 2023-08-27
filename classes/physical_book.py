from datetime import datetime
from book import Book


class PhysicalBook(Book):

    def __init__(self, title, writer, shelf, status, publishing_house, library):
        super().__init__(title, writer)
        self.shelf = shelf
        self.status = status
        self.publishing_house = publishing_house
        self.return_date = datetime.now()
        self.borrowed_to = None
        self.library = library
        if library is not None:
            library.add_book(self)

    def __repr__(self):
        return f"PhysicalBook('{self.title}', '{self.writer}', '{self.shelf}', '{self.status}')"
