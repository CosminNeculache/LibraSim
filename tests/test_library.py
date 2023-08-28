import unittest
from LibraSim.classes.library import Library
from LibraSim.classes.book import Book
from LibraSim.classes.member import Member
from unittest.mock import patch
from io import StringIO


class TestLibrary(unittest.TestCase):
    def setUp(self):
        self.library = Library("John", "email@example.com")
        self.books = []
        self.members = []

    def test_init(self):
        self.assertEqual(self.books, [])
        self.assertEqual(self.members, [])

    def test_register_members(self):
        self.library.members.append("Member 1")
        self.library.members.append("Member 2")

        self.assertIn("Member 1", self.library.members)
        self.assertIn("Member 2", self.library.members)

    def test_add_books(self):
        self.library.books.append("Book 1")
        self.library.books.append("Book 2")

        self.assertIn("Book 1", self.library.books)
        self.assertIn("Book 2", self.library.books)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_books(self, mock_stdout):
        book1 = Book("Book 1", "Author 1")
        book2 = Book("Book 2", "Author 2")

        self.library.books.append(book1)
        self.library.books.append(book2)

        expected_output = "List of books:\nBook 1\nBook 2\n"

        self.library.print_books()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    @patch('sys.stdout', new_callable=StringIO)
    def test_print_members(self, mock_stdout):
        member1 = Member('John', 'Snow', 47, 'john@example.com', '002', [])
        member2 = Member('Sam', 'Smith', 33, 'sam@example.com', '003', [])

        self.library.members.append(member1)
        self.library.members.append(member2)

        expected_output = "List of members:\nJohn Snow\nSam Smith\n"

        self.library.print_members()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_get_borrowed_books_empty(self):
        borrowed_books = self.library.get_borrowed_books()
        self.assertEqual(borrowed_books, [])

    def test_get_borrowed_books(self):
        member1 = Member('John', 'Snow', 47, '002', 'john@example.com', [])
        member2 = Member('Sam', 'Smith', 33, '003', 'sam@example.com', [])
        book1 = Book('Book 1', 'Author 1')
        book2 = Book('Book 2', 'Author 2')

        member1.borrowed_books.append(book1)
        member2.borrowed_books.append(book2)

        self.library.members.append(member1)
        self.library.members.append(member2)

        borrowed_books = self.library.get_borrowed_books()
        self.assertEqual(borrowed_books, [book1, book2])


if __name__ == '__main__':
    unittest.main()
