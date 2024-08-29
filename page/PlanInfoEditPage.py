import streamlit as st

from listener.PlanInfoEditListener import PlanInfoEditListener
from page.BasePage import BasePage


class PlanInfoEditPage(BasePage):
    listener: PlanInfoEditListener

    def __init__(self):
        super().__init__(PlanInfoEditListener())

        self.new_name = ""
        self.new_goal = ""
        self.new_description = ""

    def main(self):
        plan = self.get_parameters()[0]

        st.title("Plan")

        st.subheader("Name")
        self.new_name = st.text_input(value=f"{plan[2]}", key=f"{plan[0]}_name",
                                      label="name", label_visibility="collapsed")

        st.subheader("Goal")
        self.new_goal = st.text_input(value=f"{plan[3]}", key=f"{plan[0]}_goal",
                                      label="goal", label_visibility="collapsed")

        st.subheader("Description")
        self.new_description = st.text_area(value=f"{plan[4]}", key=f"{plan[0]}_description", height=10,
                                            label="description", label_visibility="collapsed")

    def side(self):
        st.title("Selection")

        if st.button("Save", use_container_width=True):
            plan = self.get_parameters()[0]
            self.listener.change_plan_info(plan[0], self.new_name, self.new_goal, self.new_description)
            plan = self.listener.get_plan(plan[0])
            self.listener.switch_page("PlanInfoPage", plan)

        if st.button("Cancel", use_container_width=True):
            plan = self.get_parameters()[0]
            self.listener.switch_page("PlanInfoPage", plan)
