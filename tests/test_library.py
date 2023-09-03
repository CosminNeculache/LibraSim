import unittest
from LibraSim.classes.library import Library
from LibraSim.classes.member import Member
from LibraSim.classes.physical_book import PhysicalBook
from unittest.mock import patch
from io import StringIO
from datetime import datetime, timedelta


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library(None, None)
        self.member1 = Member('John', 'Snow', 47, 'john@example.com', '002', [])
        self.member2 = Member('Sam', 'Smith', 33, 'sam@example.com', '003', [])
        self.book1 = PhysicalBook("Book 1", "Author 1", "Shelf 1", "available", "Publisher 1", self.library)
        self.book2 = PhysicalBook("Book 2", "Author 2", "Shelf 2", "available", "Publisher 2", self.library)
        self.library.members.append(self.member1)
        self.library.members.append(self.member2)
        self.books = []
        self.members = []
        self.today = datetime.now()

    def test_init(self):
        self.assertEqual(self.books, [])
        self.assertEqual(self.members, [])

    def test_register_members(self):
        self.assertIn(self.member1, self.library.members)
        self.assertIn(self.member2, self.library.members)

    def test_add_books(self):
        self.assertIn(self.book1, self.library.books)
        self.assertIn(self.book2, self.library.books)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_books(self, mock_stdout):
        self.library.books = []
        self.library.books.append(self.book1)
        self.library.books.append(self.book2)

        expected_output = "List of books:\nBook 1\nBook 2\n"

        self.library.print_books()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_members(self, mock_stdout):
        expected_output = "List of members:\nJohn Snow\nSam Smith\n"

        self.library.print_members()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_get_borrowed_books_empty(self):
        borrowed_books = self.library.get_borrowed_books()
        self.assertEqual(borrowed_books, [])

    def test_get_borrowed_books(self):
        self.member1.borrowed_books.append(self.book1)
        self.member2.borrowed_books.append(self.book2)

        borrowed_books = self.library.get_borrowed_books()
        self.assertEqual(borrowed_books, [self.book1, self.book2])

    def test_get_overdue_books_no_overdue(self):
        self.member1.borrow_book(self.book1)
        self.member2.borrow_book(self.book2)

        overdue_books = self.library.get_overdue_books()
        self.assertEqual(len(overdue_books), 0)

    def test_get_overdue_books_with_overdue(self):
        self.member1.borrow_book(self.book1)
        self.member2.borrow_book(self.book2)

        self.book1.return_date = self.today - timedelta(days=20)
        self.book2.return_date = self.today - timedelta(days=20)

        overdue_books = self.library.get_overdue_books()
        self.assertEqual(len(overdue_books), 2)


if __name__ == '__main__':
    unittest.main()
