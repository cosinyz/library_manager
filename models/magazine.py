from models.library_item import LibraryItem


class Magazine(LibraryItem):
    def __init__(self, item_id, title, year, issue_number):
        super().__init__(item_id, title)

        self.year = year
        self.issue_number = issue_number

    def get_info(self):
        return (
            f"Magazine #{self.id}: "
            f"{self.title} | "
            f"{self.year} | "
            f"Issue #{self.issue_number}"
        )

    def __str__(self):
        return self.get_info()
