from typing import Union

import streamlit as st

from listener.PlanTaskInfoListener import PlanTaskInfoListener
from page.BasePage import BasePage
from system.task.Task import BaseTask, TriggerTask, TemporalTask, PeriodicTask


class PlanTaskInfoPage(BasePage):
    listener: PlanTaskInfoListener

    def __init__(self):
        super().__init__(PlanTaskInfoListener())

    def main(self):
        plan = self.get_parameters()[0]
        task = self.get_parameters()[1]
        task: Union[BaseTask, TriggerTask, TemporalTask, PeriodicTask]

        st.title("Task")

        st.subheader("Task Type")
        st.text(f"{task.task_type}")

        st.subheader("Name")
        st.text(f"{task.name}")

        st.subheader("Description")
        st.text(f"{task.description}")

        if task.task_type == "trigger":
            st.subheader("Trigger Time")
            st.text(f"{task.trigger_time}")
        elif task.task_type == "temporal":
            st.subheader("Start Time")
            st.text(f"{task.start_time}")

            st.subheader("End Time")
            st.text(f"{task.end_time}")
        elif task.task_type == "periodic":
            st.subheader("Start Time")
            st.text(f"{task.start_time}")

            st.subheader("End Time")
            st.text(f"{task.end_time}")

            st.subheader("Time List")
            st.text(f"{task.time_list}")

    def side(self):
        if st.button("Return", use_container_width=True):
            plan = self.get_parameters()[0]
            self.listener.switch_page("PlanSchedulePage", plan)

        if st.button("Edit", use_container_width=True):
            plan = self.get_parameters()[0]
            task = self.get_parameters()[1]
            self.listener.switch_page("PlanTaskInfoEditPage", plan, task)
