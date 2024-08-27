import streamlit as st

from page.PlanListEditPage import PlanListEditPage
from page.PlanListPage import PlanListPage


class PageManager:
    def __init__(self):
        self.page_map = {}

        self._register_page(PlanListPage())
        self._register_page(PlanListEditPage())

    def _register_page(self, page):
        self.page_map[type(page).__name__] = page

    def switch_page(self, page_name):
        if page_name not in self.page_map:
            print(f"No page named '{page_name}' is found!")
            return

        st.session_state["page"] = self.page_map[page_name]
        st.rerun()
