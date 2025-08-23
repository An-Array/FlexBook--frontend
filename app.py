import streamlit as st
from pages.users import users_page
from pages.venues import venues_page
from pages.bookings import bookings_page
from pages.auth import auth_page


st.info(
    "⚠️ If APIs are not working, it might be a Render cold start. "
    "To confirm, check the [FlexBook Docs](https://flexbook-backend.onrender.com/docs)."
)

if "user_id" in st.session_state:
    st.markdown(f"User ID: {st.session_state['user_id']}")
    st.markdown(f"Role: {st.session_state['role']}")



PAGES = {
    "Auth": auth_page,
    "Users": users_page,
    "Venues": venues_page,
    "Bookings": bookings_page
}

st.sidebar.title("📌 Navigation")
choice = st.sidebar.radio("Go to", list(PAGES.keys()))
PAGES[choice]()

st.info("""
    ##### **Demo Accounts**
    - **Admin** → `admin@admin.com` / `admin`  
    - **Owner** → `owner@owner.com` / `owner`  
    - **User** → `user@user.com` / `user`
    """)

st.link_button("🌐 View on GitHub", "https://github.com/An-Array/FlexBook")


