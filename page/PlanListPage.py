import streamlit as st

from listener.PlanListListener import PlanListListener
from page.BasePage import BasePage


class PlanListPage(BasePage):
    listener: PlanListListener

    def __init__(self):
        super().__init__(PlanListListener())

        self.plan_list = []

    def main(self):
        st.title("Plan List")

        plan_list = self.listener.get_plans()
        for plan in plan_list:
            if st.button(label=plan[2], key=plan[0], use_container_width=True):
                self.listener.switch_page("PlanInfoPage", plan)

    def side(self):
        st.title("Side")

        if st.button("create plan", use_container_width=True):
            self.listener: PlanListListener
            self.listener.add_plan("name", "goal", "description")

        if st.button("get plans", use_container_width=True):
            self.listener.get_plans()

        if st.button("remove all plans", use_container_width=True):
            self.listener.remove_all_plans()
