class Borrowable:
    def borrow(self):
        print(f"Item '{self.title}' has been borrowed.")

    def return_item(self):
        print(f"Item '{self.title}' has been returned.")
