import streamlit as st

from listener.PlanInfoListener import PlanInfoListener
from page.BasePage import BasePage


class PlanInfoPage(BasePage):
    listener: PlanInfoListener

    def __init__(self):
        super().__init__(PlanInfoListener())

    def main(self):
        plan = self.get_parameters()[0]

        st.title("Plan")

        st.subheader("Name")
        st.text(f"{plan[2]}")

        st.subheader("Goal")
        st.text(f"{plan[3]}")

        st.subheader("Description")
        st.text(f"{plan[4]}")

    def side(self):
        if st.button("Return", use_container_width=True):
            self.listener.switch_page("PlanListPage")

        if st.button("Edit", use_container_width=True):
            plan = self.get_parameters()[0]
            self.listener.switch_page("PlanInfoEditPage", plan)

        if st.button("Schedule", use_container_width=True):
            plan = self.get_parameters()[0]
            self.listener.switch_page("PlanSchedulePage", plan)
