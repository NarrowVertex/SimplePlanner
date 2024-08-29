import streamlit as st

from listener.PageListListener import PageListListener
from page.BasePage import BasePage


class PlanListPage(BasePage):
    def __init__(self):
        super().__init__(PageListListener())

        self.plan_list = []

    def run(self):
        with st.sidebar:
            self.side()

        self.main()

    def main(self):
        st.title("Plan List")

        plan_list = self.listener.get_plans()
        for plan in plan_list:
            if st.button(label=plan[2], key=plan[0], use_container_width=True):
                print(f'Plan[{plan[2]}] is clicked!')

    def side(self):
        st.title("Side")

        if st.button("create plan", use_container_width=True):
            self.listener: PageListListener
            self.listener.add_plan("name", "goal", "description")

        if st.button("get plans", use_container_width=True):
            self.listener.get_plans()

        if st.button("remove all plans", use_container_width=True):
            self.listener.remove_all_plans()
