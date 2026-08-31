from abc import ABC, abstractmethod


class LibraryItem(ABC):
    def __init__(self, item_id, title):
        self.id = item_id
        self.title = title

    @abstractmethod
    def get_info(self):
        pass
