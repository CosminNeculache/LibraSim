import unittest
from datetime import datetime, timedelta
from LibraSim.classes.physical_book import PhysicalBook


class TestPhysicalBookClass(unittest.TestCase):

    def setUp(self):
        self.library_mock = LibraryMock()
        self.book = PhysicalBook("Fahrenheit 451", "Ray Bradbury", "Shelf 2", "available", "Art", self.library_mock)

    def test_physical_book_init(self):
        self.assertEqual(self.book.title, "Fahrenheit 451")
        self.assertEqual(self.book.writer, "Ray Bradbury")
        self.assertEqual(self.book.shelf, "Shelf 2")
        self.assertEqual(self.book.status, "available")
        self.assertEqual(self.book.publishing_house, "Art")
        self.assertIsNotNone(self.book.return_date)
        self.assertIsNone(self.book.borrowed_to)
        self.assertEqual(self.book.library, self.library_mock)
        self.assertTrue(self.library_mock.book_added)

    def test_physical_book_repr(self):
        expected_repr = "PhysicalBook('Fahrenheit 451', 'Ray Bradbury', 'Shelf 2', 'available')"
        self.assertEqual(repr(self.book), expected_repr)


class LibraryMock:
    def __init__(self):
        self.book_added = False

    def add_book(self, book):
        self.book_added = True


if __name__ == '__main__':
    unittest.main()
