import streamlit as st

from listener.PlanInfoListener import PlanInfoListener
from page.BasePage import BasePage


class PlanInfoPage(BasePage):
    listener: PlanInfoListener

    def __init__(self):
        super().__init__(PlanInfoListener())

    def main(self):
        plan = self.get_parameters()[0]

        st.title(f"{plan[2]}")

        st.text(f"Goal: {plan[3]}")
        st.text(f"Description: {plan[4]}")

    def side(self):
        if st.button("Return", use_container_width=True):
            self.listener.switch_page("PlanListPage")

        if st.button("Edit", use_container_width=True):
            self.listener.switch_page("PlanListEditPage")
