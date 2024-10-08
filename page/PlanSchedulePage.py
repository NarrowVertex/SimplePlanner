from datetime import datetime

import streamlit as st
from streamlit_calendar import calendar

from listener.PlanScheduleListener import PlanScheduleListener
from page.BasePage import BasePage
from system.task.Task import TriggerTask, create_task_by_list


class PlanSchedulePage(BasePage):
    listener: PlanScheduleListener

    def __init__(self):
        super().__init__(PlanScheduleListener())

    def main(self):
        plan = self.get_parameters()[0]

        tasks = self.listener.get_tasks(plan[0])
        for task in tasks:
            if st.button(label=task.name, key=task.task_id, use_container_width=True):
                self.listener.switch_page("PlanTaskInfoPage", plan, task)

    def side(self):
        if st.button("Return", use_container_width=True):
            plan = self.get_parameters()[0]
            self.listener.switch_page("PlanInfoPage", plan)

        if st.button("Edit", use_container_width=True):
            plan = self.get_parameters()[0]
            self.listener.switch_page("PlanScheduleEditPage", plan)

        if st.button("Add task", use_container_width=True):
            plan = self.get_parameters()[0]
            task = TriggerTask(plan[0], "test_task", "test_task_description",
                               datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            self.listener.add_task(task)
            self.listener.switch_page("PlanTaskInfoEditPage", plan, task)
