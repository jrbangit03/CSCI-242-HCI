
import streamlit as st

from util import TEST_DATA, TEST_TRANSACTIONS, MARKET_RECOMMENDATIONS


# pending - chat
# pending - accept listing

def nav_bar():
    c1, c2, c3, c4, c5 = st.columns(5)
    if c1.button("Home", use_container_width=True):
        go("home")
    if c2.button("Post a task", use_container_width=True):
        go("post")
    if c3.button("Find a work", use_container_width=True):
        go("find")
    if c4.button("Transactions", use_container_width=True):
        go("transactions")
    if c5.button("Logout", use_container_width=True):
        go("welcome")



def go(screen: str):
    st.session_state.screen = screen
    st.rerun()

def register_screen():
    st.title("User Registration")
    with st.form("Registration"):
        st.text_input("First Name", placeholder="Ramoncito Jr")
        st.text_input("Last Name", placeholder="Bangit")
        st.text_input("Address", placeholder="Shibuya, Tokyo")
        st.text_input("Username", placeholder="jrbangit")
        st.text_input("Bearable Markup Percentage in Open Market", placeholder="50%")
        st.text_input("Credit Card Number", placeholder="******1234")
        st.text_input("Credit Card Expiration", placeholder="07/27")
        st.text_input("Credit Card Security Code", placeholder="123")
        st.file_uploader("Government ID: driver's license, etc")
        st.checkbox("Link to Facebook")
        submit = st.form_submit_button("Register", type="primary", use_container_width=True)

    if submit:
        st.success("Registration has been completed!")
        st.button("Proceed to Login", on_click=lambda: go("login"))

def login_screen():
    st.title("Login")
    with st.form("Login"):
        st.text_input("Username", placeholder="abc123")
        st.text_input("Password", type="password", placeholder="****")
        submit = st.form_submit_button("Login", type="primary", use_container_width=True)
    if submit:
        go("home")
    # st.caption("JR Hire/Get Hired Prototype")
    # st.write("List a task you need done, or earn by doing tasks for others.")

# def logout_screen():
#     st.title("Logout")
#     if st.button("Logout", use_container_width=True):
#         go("welcome")

def post_task_screen():
    nav_bar()
    st.title("List a queuing task")
    st.caption("Describe the queuing task")
    with st.form("List a Queue Task"):
        st.text_input("Title", placeholder="Queue for One Piece drop")
        st.text_input("Description", placeholder="What exactly needs to be done?")
        st.text_input("Location", placeholder="Ueno Biccamera")
        col1, col2 = st.columns(2)
        col1.text_input("Date and Time", placeholder="Oct 22, 2026, Fri, 3:00PM")
        col2.text_input("Offered Pay", placeholder="5,000 Yen")
        submitted = st.form_submit_button("Publish Listing", type="primary", use_container_width=True)
    if submitted:
        st.success("Congratulations! Your listing has been published!")
        st.button("Browse/View open listings", on_click=lambda : go("find"))

def find_work_screen():
    nav_bar()
    st.title("Find a queuing task")
    st.caption("Open Listing Tasks")

    for listing in TEST_DATA:
        with st.container(border=True):
            st.subheader(listing["title"])
            st.write(listing["description"])
            c1, c2, c3, c4 = st.columns(4)
            c1.markdown("Location: {}".format(listing["location"]))
            c2.markdown("Pay : {}".format(listing["offered pay"]))
            c2.markdown("When: {}".format(listing["date and time"]))
            c2.markdown("Lister: {}".format(listing["poster"]))
            # st.sub
    # st.write("List a task you need done, or earn by doing tasks for others.")

def view_transactions():
    nav_bar()
    st.title("Transactions")
    st.caption("View your Active and Historical Transactions")
    for transactions in TEST_TRANSACTIONS:
        with st.container(border=True):
            st.subheader(transactions["title"])
            # st.write(transactions["transacting with"])
            c1, c2, c3, c4 = st.columns(4)
            c1.markdown("Transacting with {}".format(transactions["transacting with"]))
            c2.markdown("Pay {}".format(transactions["offered pay"]))
            c3.markdown("Date: {}".format(transactions["date and time"]))
            c4.markdown("Status: {}".format(transactions["status"]))
            got_the_item = transactions["got the item"]
            st.write("Able to get the item? : {}".format(got_the_item))
            if got_the_item == "False":
                st.button("See Recommendations for One Piece in Open Market".format(),
                          use_container_width=True, key="recommendations", on_click=lambda: go("recommendations"))


def recommendations():
    nav_bar()
    st.title("Market Recommendations within the set Bearable Markup")
    for recommendation in MARKET_RECOMMENDATIONS:
        with st.container(border=True):
            st.subheader(recommendation["title"])
            col1, col2, col3, col4 = st.columns(4)
            col1.markdown("Origin: {}".format(recommendation["listed in"]))
            col2.markdown("Price: {}".format(recommendation["listing price"]))
            col3.markdown("Markup: {}".format(recommendation["markup"]))
            col4.markdown("Lister: {}".format(recommendation["lister"]))



def home_screen():
    nav_bar()
    st.title("Home")
    st.caption("What would you like to do? Hire someone or Looking for a quick job?")

def welcome_screen():
    st.title("Welcome")
    st.caption("JR's Hire to Queue or Get hired for quick bucks - TCG Queue Prototype")
    st.write("List a queuing task you need done, or earn by doing queuing tasks for others.")

    if st.button("Create Account", use_container_width=True):
        go("register")
    if st.button("Already have an account", use_container_width=True):
        go("login")

SCREENS = {
    "register": register_screen,
    "welcome": welcome_screen,
    "home": home_screen,
    "login": login_screen,
    "post": post_task_screen,
    "find": find_work_screen,
    "transactions": view_transactions,
    "recommendations": recommendations
    # "logout": logout_screen
}

def main():
    st.set_page_config(page_title="JR's Hire to Queue or Get hired for quick bucks - TCG Queue Prototype")

    if "screen" not in st.session_state:
        st.session_state.screen = "welcome"

    SCREENS[st.session_state.screen]()

if __name__ == "__main__":
    main()
