import streamlit as st

from system.System import System


def run_page():
    page_path = "page/PageLauncher.py"
    page_list = [st.Page(page_path), ]
    page = st.navigation(pages=page_list, position="hidden")
    page.run()


def main():
    if "initialized" not in st.session_state:
        st.session_state["initialized"] = "initialized"

        system = System()
        system.initialize()

        system.page_manager.switch_page("PlanListPage")

    run_page()


if __name__ == "__main__":
    main()
