import os
import streamlit as st
import toml

# Function to load local secrets.toml
def load_local_secrets():
    if os.path.exists("secrets.toml"):
        return toml.load("secrets.toml")
    return {}

local_secrets = load_local_secrets()

# Use Streamlit secrets if available, else fallback to local TOML
BACKEND_URL = st.secrets["BASE_URL"] if "BASE_URL" in st.secrets else local_secrets.get("BASE_URL")

def get_auth_headers():
    if not all(k in st.session_state for k in ["token", "user_id", "role"]):
        st.error("‼️ Please login first.")
        return None
    return {"Authorization": f"Bearer {st.session_state['token']}"}
