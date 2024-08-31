import streamlit as st

from listener.PlanTaskInfoListener import PlanTaskInfoListener
from page.BasePage import BasePage


class PlanTaskInfoPage(BasePage):
    listener: PlanTaskInfoListener

    def __init__(self):
        super().__init__(PlanTaskInfoListener())

    def main(self):
        plan = self.get_parameters()[0]
        task = self.get_parameters()[1]
        task_type = task[2]

        st.title("Task")

        st.subheader("Task Type")
        st.text(f"{task_type}")

        st.subheader("Name")
        st.text(f"{task[3]}")

        st.subheader("Description")
        st.text(f"{task[4]}")

        if task_type == "trigger":
            st.subheader("Trigger Time")
            st.text(f"{task[5]}")
        elif task_type == "temporal":
            st.subheader("Start Time")
            st.text(f"{task[6]}")

            st.subheader("End Time")
            st.text(f"{task[7]}")
        elif task_type == "periodic":
            st.subheader("Start Time")
            st.text(f"{task[6]}")

            st.subheader("End Time")
            st.text(f"{task[7]}")

            st.subheader("Time List")
            st.text(f"{task[8]}")

    def side(self):
        if st.button("Return", use_container_width=True):
            plan = self.get_parameters()[0]
            self.listener.switch_page("PlanSchedulePage", plan)

        if st.button("Edit", use_container_width=True):
            plan = self.get_parameters()[0]
            task = self.get_parameters()[1]
            self.listener.switch_page("PlanTaskInfoEditPage", plan, task)
