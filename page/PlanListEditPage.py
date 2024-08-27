import streamlit as st

from listener.PageListEditListener import PageListEditListener
from page.BasePage import BasePage


class PlanListEditPage(BasePage):
    def __init__(self):
        super().__init__(PageListEditListener())

    def run(self):
        st.title("TEST2")

        if st.button("SWITCH"):
            self.switch_page("PlanListPage")
