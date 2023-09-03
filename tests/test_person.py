import unittest
from LibraSim.classes.person import Person


class TestPersonClass(unittest.TestCase):

    def setUp(self):
        self.person = Person("John", "Doe", 30, "john@example.com")

    def test_person_init(self):
        self.assertEqual(self.person.first_name, "John")
        self.assertEqual(self.person.last_name, "Doe")
        self.assertEqual(self.person.age, 30)
        self.assertEqual(self.person.email, "john@example.com")

    def test_person_repr(self):
        expected_repr = "Person(John, Doe, 30)"
        self.assertEqual(repr(self.person), expected_repr)


if __name__ == '__main__':
    unittest.main()
