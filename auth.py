import streamlit as st
import requests
from config import BACKEND_URL

BASE_URL = BACKEND_URL  # adjust if needed

# ✅ Helper function for headers
def get_auth_headers():
    if "token" not in st.session_state:
        st.error("‼️ Please login first.")
        return None
    return {"Authorization": f"Bearer {st.session_state['token']}"}


# ✅ Signup
def signup():
    st.subheader("📝 Signup")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    if st.button("Create Account"):
        payload = {"email": email, "password": password}
        try:
            response = requests.post(f"{BASE_URL}/signup", json=payload)
            if response.status_code == 201:
                st.success("✅ User created successfully. Please login.")
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Connection Error: {e}")


# ✅ Login
def login():
    st.subheader("🔑 Login")
    email = st.text_input("Email (username)")
    password = st.text_input("Password", type="password")
    if st.button("Login"):
        if "token" in st.session_state:
            del st.session_state["token"]
        data = {"username": email, "password": password}
        try:
            response = requests.post(f"{BASE_URL}/login", data=data)
            if response.status_code == 200:
                token = response.json()["access_token"]
                st.session_state["token"] = token
                st.success("✅ Login successful!")
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Connection Error: {e}")



# ✅ Admin role panel
def admin_panel():
    st.subheader("🛠️ Admin Panel - Assign Role")
    user_id = st.number_input("User ID", min_value=1, step=1)
    role = st.selectbox("Select Role", ["user", "owner", "admin"])
    panel_key = st.text_input("Admin Panel Key", type="password")
    if st.button("Update Role"):
        payload = {"user_id": user_id, "role": role, "panel_key": panel_key}
        try:
            response = requests.put(f"{BASE_URL}/panel", json=payload)
            if response.status_code == 200:
                st.success(response.json()["message"])
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Connection Error: {e}")


# ✅ Main User Page
def auth_page():
    st.title("👤 Auth Management")

    action = st.selectbox(
        "Choose Action",
        ["Signup", "Login", "Admin Panel"]
    )

    if action == "Signup":
        signup()
    elif action == "Login":
        login()
    elif action == "Admin Panel":
        admin_panel()