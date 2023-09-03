import unittest
from LibraSim.classes.book import Book


class TestBookClass(unittest.TestCase):

    def setUp(self) -> None:
        self.book = Book("Fahrenheit 451", "Ray Bradbury")

    def test_book_init(self):
        self.assertEqual(self.book.title, "Fahrenheit 451")
        self.assertEqual(self.book.writer, "Ray Bradbury")

    def test_book_repr(self):
        expected_repr = "Book(title='Fahrenheit 451', writer='Ray Bradbury')"
        self.assertEqual(repr(self.book), expected_repr)


if __name__ == '__main__':
    unittest.main()
