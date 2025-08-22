import streamlit as st
from users import users_page
from venues import venues_page
from bookings import bookings_page
from auth import auth_page



PAGES = {
    "Auth": auth_page,
    "Users": users_page,
    "Venues": venues_page,
    "Bookings": bookings_page
}

st.sidebar.title("📌 Navigation")
choice = st.sidebar.radio("Go to", list(PAGES.keys()))
PAGES[choice]()


