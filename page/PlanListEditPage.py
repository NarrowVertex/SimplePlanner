import streamlit as st

from listener.PlanListEditListener import PlanListEditListener
from page.BasePage import BasePage


class PlanListEditPage(BasePage):
    listener: PlanListEditListener

    def __init__(self):
        super().__init__(PlanListEditListener())

    def main(self):
        pass

    def side(self):
        pass
