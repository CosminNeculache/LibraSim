class Book:

    def __init__(self, title, writer):
        self.title = title
        self.writer = writer

    def __repr__(self):
        return f"Book(title='{self.title}', writer='{self.writer}')"
