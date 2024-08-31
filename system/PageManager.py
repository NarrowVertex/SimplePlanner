import streamlit as st

from page.PlanListPage import PlanListPage
from page.PlanListEditPage import PlanListEditPage
from page.PlanInfoPage import PlanInfoPage
from page.PlanInfoEditPage import PlanInfoEditPage
from page.PlanSchedulePage import PlanSchedulePage
from page.PlanTaskInfoEditPage import PlanTaskInfoEditPage
from page.PlanTaskInfoPage import PlanTaskInfoPage


class PageManager:
    def __init__(self):
        self.page_map = {}

        self._register_page(PlanListPage())
        self._register_page(PlanListEditPage())
        self._register_page(PlanInfoPage())
        self._register_page(PlanInfoEditPage())
        self._register_page(PlanSchedulePage())
        self._register_page(PlanTaskInfoPage())
        self._register_page(PlanTaskInfoEditPage())

    def _register_page(self, page):
        self.page_map[type(page).__name__] = page

    def switch_page(self, page_name):
        st.session_state["page"] = self._get_page(page_name)
        st.rerun()

    def _get_page(self, page_name):
        if page_name not in self.page_map:
            print(f"No page named '{page_name}' is found!")
            return None

        return self.page_map[page_name]
