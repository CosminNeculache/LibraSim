import unittest
from datetime import datetime
from LibraSim.classes.physical_book import PhysicalBook
from LibraSim.classes.library import Library


class TestPhysicalBookClass(unittest.TestCase):

    def setUp(self):
        self.library = Library(None, None)
        self.book = PhysicalBook("Fahrenheit 451", "Ray Bradbury", "Shelf 2", "available", "Art", self.library)

    def test_physical_book_init(self):
        self.assertEqual(self.book.title, "Fahrenheit 451")
        self.assertEqual(self.book.writer, "Ray Bradbury")
        self.assertEqual(self.book.shelf, "Shelf 2")
        self.assertEqual(self.book.status, "available")
        self.assertEqual(self.book.publishing_house, "Art")
        self.assertEqual(self.book.return_date, datetime.now())
        self.assertIsNone(self.book.borrowed_to)
        self.assertEqual(self.book.library, self.library)
        self.assertTrue(self.book in self.library.books)

    def test_physical_book_repr(self):
        expected_repr = "PhysicalBook('Fahrenheit 451', 'Ray Bradbury', 'Shelf 2', 'available')"
        self.assertEqual(repr(self.book), expected_repr)


if __name__ == '__main__':
    unittest.main()
