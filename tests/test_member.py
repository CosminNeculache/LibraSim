import unittest
from datetime import datetime
from LibraSim.classes.library import Library
from LibraSim.classes.member import Member
from LibraSim.classes.physical_book import PhysicalBook


class TestMemberClass(unittest.TestCase):
    def setUp(self):
        self.library = Library()
        self.member = Member("John", "Doe", 30, "001", [], "john@example.com", self.library)
        self.physical_book = PhysicalBook("Book Title", "Author", "Shelf", "available", "Publisher", self.library)

    def test_member_init(self):
        self.assertEqual(self.member.first_name, "John")
        self.assertEqual(self.member.last_name, "Doe")
        self.assertEqual(self.member.age, 30)
        self.assertEqual(self.member.member_id, "001")
        self.assertEqual(self.member.borrowed_books, [])
        self.assertEqual(self.member.email, "john@example.com")
        self.assertEqual(self.member.library, self.library)
        # self.assertTrue(self.library.member_registered)

    def test_borrow_book(self):
        print("Before borrowing:")
        print("Member borrowed_books:", self.member.borrowed_books)
        print("PhysicalBook status:", self.physical_book.status)
        print("PhysicalBook borrowed_to:", self.physical_book.borrowed_to)

        self.member.borrow_book(self.physical_book)
        self.assertTrue(self.physical_book in self.member.borrowed_books)
        self.assertEqual(self.physical_book.borrowed_to, "001")

        print("After borrowing:")
        print("Member borrowed_books:", self.member.borrowed_books)
        print("PhysicalBook status:", self.physical_book.status)
        print("PhysicalBook borrowed_to:", self.physical_book.borrowed_to)

    def test_return_book(self):
        self.member.borrow_book(self.physical_book)
        print("Before returning:")
        print("Member borrowed_books:", self.member.borrowed_books)

        self.member.return_book(self.physical_book)

        print("After returning:")
        print("Member borrowed_books:", self.member.borrowed_books)
        self.assertNotIn(self.physical_book, self.member.borrowed_books)
        self.assertEqual(self.physical_book.return_date.date(), datetime.now().date())
        self.assertEqual(self.physical_book.status, "available")
        self.assertIsNone(self.physical_book.borrowed_to)

    def test_member_repr(self):
        expected_repr = "John Doe"
        self.assertEqual(repr(self.member), expected_repr)


class LibraryMock:
    def __init__(self):
        self.member_registered = False

    def register_member(self, member):
        self.member_registered = True


if __name__ == '__main__':
    unittest.main()
