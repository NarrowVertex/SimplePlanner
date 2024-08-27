from abc import ABC, abstractmethod


class BasePage(ABC):
    def __init__(self, listener):
        self.listener = listener

    @abstractmethod
    def run(self):
        pass

    def switch_page(self, page_name):
        self.listener.switch_page(page_name)
