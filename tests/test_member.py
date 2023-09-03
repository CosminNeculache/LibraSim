import unittest
from datetime import datetime, timedelta
from LibraSim.classes.library import Library
from LibraSim.classes.member import Member
from LibraSim.classes.physical_book import PhysicalBook


class TestMemberClass(unittest.TestCase):
    def setUp(self):
        self.library = Library(None, None)
        self.member = Member("John", "Doe", 30, "john@example.com", "001", [])
        self.book = PhysicalBook("Fahrenheit 451", "Ray Bradbury", "Shelf 2", "available", "Art", self.library)

    def test_member_init(self):
        self.assertEqual(self.member.first_name, "John")
        self.assertEqual(self.member.last_name, "Doe")
        self.assertEqual(self.member.age, 30)
        self.assertEqual(self.member.member_id, "001")
        self.assertEqual(self.member.borrowed_books, [])
        self.assertEqual(self.member.email, "john@example.com")

    def test_borrow_book(self):
        self.member.borrow_book(self.book)

        self.assertTrue(self.book in self.member.borrowed_books)
        self.assertEqual(self.book.return_date, datetime.now() + timedelta(weeks=4))
        self.assertEqual(self.book.status, "unavailable")
        self.assertEqual(self.book.borrowed_to, "001")

    def test_return_book(self):
        self.member.borrow_book(self.book)
        self.member.return_book(self.book)

        self.assertTrue(self.book not in self.member.borrowed_books)
        self.assertEqual(self.book.return_date.date(), datetime.now().date())
        self.assertEqual(self.book.status, "available")
        self.assertIsNone(self.book.borrowed_to)

    def test_member_repr(self):
        expected_repr = "John Doe"
        self.assertEqual(repr(self.member), expected_repr)


if __name__ == '__main__':
    unittest.main()
