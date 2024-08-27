import streamlit as st


if __name__ == "__page__":
    page = st.session_state["page"]
    page.run()
