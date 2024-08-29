import streamlit as st
from streamlit_calendar import calendar

from listener.PlanScheduleListener import PlanScheduleListener
from page.BasePage import BasePage


class PlanSchedulePage(BasePage):
    listener: PlanScheduleListener

    def __init__(self):
        super().__init__(PlanScheduleListener())

    def main(self):
        plan = self.get_parameters()[0]

        tasks = self.listener.get_tasks(plan[0])
        print(tasks)

    def side(self):
        if st.button("Return", use_container_width=True):
            plan = self.get_parameters()[0]
            self.listener.switch_page("PlanInfoPage", plan)

        if st.button("Edit", use_container_width=True):
            plan = self.get_parameters()[0]
            # self.listener.switch_page("PlanInfoEditPage", plan)
