from models.user import User


class Admin(User):
    def get_permissions(self):
        return [
            "borrow",
            "return",
            "add_book",
            "delete_book",
            "update_book",
            "view_statistics"
        ]

    def get_info(self):
        return f"Admin #{self.id}: {self.name} | {self.email}"
