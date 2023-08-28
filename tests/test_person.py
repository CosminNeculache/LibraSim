import unittest
from LibraSim.classes.person import Person


class TestPersonClass(unittest.TestCase):

    def test_person_init(self):
        person = Person("John", "Doe", 30)
        self.assertEqual(person.first_name, "John")
        self.assertEqual(person.last_name, "Doe")
        self.assertEqual(person.age, 30)

    def test_person_repr(self):
        person = Person("John", "Doe", 30)
        expected_repr = "Person(John, Doe, 30)"
        self.assertEqual(repr(person), expected_repr)


if __name__ == '__main__':
    unittest.main()
