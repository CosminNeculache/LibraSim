class Person:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def __repr__(self):
        return f"Person({self.first_name}, {self.last_name}, {self.age})"
