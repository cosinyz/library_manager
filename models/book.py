from models.library_item import LibraryItem
from models.printable import Printable
from models.borrowable import Borrowable


class Book(LibraryItem, Printable, Borrowable):
    def __init__(self, item_id, title, author, year, genre, is_available=True):
        super().__init__(item_id, title)

        self.author = author
        self.year = year
        self.genre = genre
        self.is_available = is_available

    def get_info(self):
        status = "Available" if self.is_available else "Borrowed"

        return (
            f"Book #{self.id}: "
            f"{self.title} | "
            f"{self.author} | "
            f"{self.year} | "
            f"{self.genre} | "
            f"{status}"
        )

    def check_availability(self):
        return self.is_available

    @staticmethod
    def is_valid_year(year):
        return 0 < year <= 2026

    @classmethod
    def from_string(cls, data):
        title, author, year, genre = data.split(";")

        return cls(
            item_id=0,
            title=title,
            author=author,
            year=int(year),
            genre=genre
        )

    def __str__(self):
        return self.get_info()

    def __repr__(self):
        return (
            f"Book("
            f"id={self.id}, "
            f"title='{self.title}', "
            f"author='{self.author}', "
            f"year={self.year}, "
            f"genre='{self.genre}'"
            f")"
        )

    def __eq__(self, other):
        if not isinstance(other, Book):
            return NotImplemented

        return self.id == other.id

    def __len__(self):
        return len(self.title)
