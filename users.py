import streamlit as st
import requests
from config import BACKEND_URL

BASE_URL = BACKEND_URL # adjust if needed

# ✅ Helper function for headers
def get_auth_headers():
    if "token" not in st.session_state:
        st.error("‼️ Please login first.")
        return None
    return {"Authorization": f"Bearer {st.session_state['token']}"}

# ✅ Get All Users (Admin only)
def get_all_users():
    st.subheader("👥 All Users (Admin Only)")
    headers = get_auth_headers()
    if not headers: return
    if st.button("Fetch Users"):
        try:
            response = requests.get(f"{BASE_URL}/users", headers=headers)
            if response.status_code == 200:
                users = response.json()
                for u in users:
                    st.markdown(f"**ID:** {u['id']} | **Email:** {u['email']} | **Role:** {u['role']} | **Created At:** {u['created_at']}")
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Connection Error: {e}")


# ✅ Get user by ID
def get_user_by_id():
    st.subheader("🔍 Get User by ID")
    headers = get_auth_headers()
    if not headers: return
    user_id = st.number_input("Enter User ID", min_value=1, step=1)
    if st.button("Fetch User"):
        try:
            response = requests.get(f"{BASE_URL}/users/{user_id}", headers=headers)
            if response.status_code == 200:
                user = response.json()
                st.json(user)
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Connection Error: {e}")


# ✅ Update user
def update_user():
    st.subheader("✏️ Update User")
    headers = get_auth_headers()
    if not headers: return
    user_id = st.number_input("User ID to Update", min_value=1, step=1)
    email = st.text_input("New Email")
    password = st.text_input("New Password (optional)", type="password")
    if st.button("Update User"):
        payload = {}
        if email: payload["email"] = email
        if password: payload["password"] = password
        try:
            response = requests.put(f"{BASE_URL}/users/{user_id}", json=payload, headers=headers)
            if response.status_code == 200:
                st.success(f"✅ User {user_id} updated successfully!")
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Connection Error: {e}")


# ✅ Delete user
def delete_user():
    st.subheader("🗑️ Delete User")
    headers = get_auth_headers()
    if not headers: return
    user_id = st.number_input("User ID to Delete", min_value=1, step=1)
    if st.button("Delete User"):
        try:
            response = requests.delete(f"{BASE_URL}/users/{user_id}", headers=headers)
            if response.status_code == 204:
                st.success(f"✅ User {user_id} deleted successfully!")
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Connection Error: {e}")



# ✅ Main User Page
def users_page():
    st.title("👤 User Management")

    action = st.selectbox(
        "Choose Action",
        ["Get All Users", "Get User By ID", "Update User", "Delete User"]
    )

    if action == "Get All Users":
        get_all_users()
    elif action == "Get User By ID":
        get_user_by_id()
    elif action == "Update User":
        update_user()
    elif action == "Delete User":
        delete_user()

