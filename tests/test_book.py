import unittest
from LibraSim.classes.book import Book


class TestBookClass(unittest.TestCase):

    def test_book_init(self):
        book = Book("Fahrenheit 451", "Ray Bradbury")
        self.assertEqual(book.title, "Fahrenheit 451")
        self.assertEqual(book.writer, "Ray Bradbury")

    def test_book_repr(self):
        book = Book("Fahrenheit 451", "Ray Bradbury")
        expected_repr = "Book(title='Fahrenheit 451', writer='Ray Bradbury')"
        self.assertEqual(repr(book), expected_repr)


if __name__ == '__main__':
    unittest.main()
