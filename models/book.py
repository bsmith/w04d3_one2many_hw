class Book:
    def __init__(self, title, page_count, has_read, author, id = None):
        self.title = title
        self.page_count = page_count
        self.has_read = has_read
        self.author = author
        self.id = id

    def __repr__(self):
        return f"Book({self.title!r}, {self.page_count!r}, {self.has_read!r}, {self.author!r}, id={self.id!r})"

