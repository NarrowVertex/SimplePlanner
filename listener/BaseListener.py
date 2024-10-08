import streamlit as st


class BaseListener:
    def __init__(self):
        from system.System import System
        self.system = System()

    def switch_page(self, page_name, *parameters):
        st.session_state["parameters"] = parameters
        self.system.page_manager.switch_page(page_name)
