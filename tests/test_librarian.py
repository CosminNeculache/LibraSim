import unittest
from LibraSim.classes.librarian import Librarian
from LibraSim.classes.library import Library
from datetime import datetime
from LibraSim.classes.physical_book import PhysicalBook


class TestLibrarianClass(unittest.TestCase):
    def setUp(self):
        self.library = Library(None, None)
        self.librarian = Librarian('Constantin', 'Ion', 50, "cosmin.neculache@gmail.com",
                                   datetime(2018, 12, 2), self.library)
        self.book = PhysicalBook("Fahrenheit 451", "Ray Bradbury", "Shelf 2", "available", "Art", self.library)

    def test_librarian_init(self):
        self.assertEqual(self.librarian.first_name, "Constantin")
        self.assertEqual(self.librarian.last_name, "Ion")
        self.assertEqual(self.librarian.age, 50)
        self.assertEqual(self.librarian.email, "cosmin.neculache@gmail.com")
        self.assertEqual(self.librarian.employment_date, datetime(2018, 12, 2))
        self.assertEqual(self.librarian.library, self.library)

    def test_check_disponibility(self):
        result = self.librarian.check_disponibility(self.book)
        self.assertTrue(result)

        self.book.status = "unavailable"
        result = self.librarian.check_disponibility(self.book)
        self.assertFalse(result)

    def test_physical_book_repr(self):
        expected_repr = "Librarian('Constantin', 'Ion', 50, 2018-12-02 00:00:00)"
        self.assertEqual(repr(self.librarian), expected_repr)


if __name__ == '__main__':
    unittest.main()
