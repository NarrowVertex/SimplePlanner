import streamlit as st

from listener.PageListListener import PageListListener
from page.BasePage import BasePage


class PlanListPage(BasePage):
    def __init__(self):
        super().__init__(PageListListener())

    def run(self):
        st.title("TEST")

        if st.button("SWITCH"):
            self.switch_page("PlanListEditPage")
