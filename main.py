
import streamlit as st


def welcome_screen():
    st.title("Home")
    st.caption("JR Hire/Get Hired Prototype")
    st.write("List a task you need done, or earn by doing tasks for others.")

def main():
    st.set_page_config(page_title="JR Hire/Get Hired Prototype")

    if "screen" not in st.session_state:
        st.session_state.screen = welcome_screen()

if __name__ == "__main__":
    main()
