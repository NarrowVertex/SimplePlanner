from abc import ABC, abstractmethod
import streamlit as st


class BasePage(ABC):
    def __init__(self, listener):
        self.listener = listener

    def run(self):
        with st.sidebar:
            self.side()

        self.main()

    @abstractmethod
    def main(self):
        pass

    @abstractmethod
    def side(self):
        pass

    def switch_page(self, page_name):
        self.listener.switch_page(page_name)

    def get_parameters(self):
        if "parameters" not in st.session_state:
            return ()

        return st.session_state["parameters"]
