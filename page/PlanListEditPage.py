import streamlit as st

from listener.PageListEditListener import PageListEditListener
from page.BasePage import BasePage


class PlanListEditPage(BasePage):
    listener: PageListEditListener

    def __init__(self):
        super().__init__(PageListEditListener())

    def main(self):
        pass

    def side(self):
        pass
