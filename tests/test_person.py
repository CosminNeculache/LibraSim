import unittest
from LibraSim.classes.person import Person


class TestPersonClass(unittest.TestCase):

    def test_person_init(self):
        person = Person("John", "Doe", 30, "john@example.com")
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")
        self.assertEqual(person.age, 30)
        self.assertEqual(person.email, "john@example.com")

    def test_person_repr(self):
        person = Person("John", "Doe", 30, "john@example.com")
        expected_repr = "Person(John, Doe, 30)"
        self.assertEqual(repr(person), expected_repr)


if __name__ == '__main__':
    unittest.main()
