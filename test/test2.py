class Book(object):

    def __init__(self, title):
        self.title = title

    @classmethod
    def create(cls, title):
        book = cls(title=title)
        return book

    @staticmethod
    def create():


book1 = Book("python")
book2 = Book.create("python and django")
print(book1.title)
print(book2.title)