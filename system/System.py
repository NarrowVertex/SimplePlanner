from system.DBManager import DBManager
from system.PageManager import PageManager
from util.meta import SingletonMeta


class System(metaclass=SingletonMeta):
    def __init__(self):
        if System.is_initialized():
            return

        System.instances[System] = self

        self.page_manager = None
        self.db_manager = None

    def initialize(self):
        self.page_manager = PageManager()
        self.db_manager = DBManager()
