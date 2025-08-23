import streamlit as st
import requests
from config import BACKEND_URL, get_auth_headers

BASE_URL = BACKEND_URL   # change if deployed

# ✅ Helper function to get auth headers
def auth_check():
    get_auth_headers()


# ✅ Show all venues
def show_all_venues():
    st.subheader("🏢 All Venues")
    headers = get_auth_headers()
    if not headers: return
    try:
        response = requests.get(f"{BASE_URL}/venues", headers=headers)
        if response.status_code == 200:
            venues = response.json()
            for v in venues:
                st.markdown(f"- **ID:** {v['id']} | **Name:** {v['name']} | **Owner ID:** {v['owner_id']}")
        else:
            st.error(f"⚠️ {response.json().get('detail')}")
    except Exception as e:
        st.error(f"🚨 Connection Error: {e}")


# ✅ Show single venue by ID
def show_venue_by_id():
    st.subheader("🔍 Get Venue by ID")
    headers = get_auth_headers()
    if not headers: return
    venue_id = st.number_input("Enter Venue ID", min_value=1, step=1)
    if st.button("Fetch Venue"):
        try:
            response = requests.get(f"{BASE_URL}/venues/{venue_id}", headers=headers)
            if response.status_code == 200:
                venue = response.json()
                st.markdown(
                    f"""
                    **Venue ID:** {venue['id']}  
                    **Name:** {venue['name']}  
                    **Owner ID:** {venue['owner_id']}  
                    **Owner Email:** {venue['owner_email']}  
                    """
                )
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Connection Error: {e}")


# ✅ Add new venue
def add_venue():
    st.subheader("🏨 Add Venue")
    headers = get_auth_headers()
    if not headers: return
    name = st.text_input("Venue Name")
    if st.button("Add Venue"):
        payload = {"name": name}
        try:
            response = requests.post(f"{BASE_URL}/venues", json=payload, headers=headers)
            if response.status_code == 201:
                st.success(f"✅ Venue '{name}' created successfully!")
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Connection Error: {e}")


# ✅ Update venue
def update_venue():
    st.subheader("✏️ Update Venue")
    headers = get_auth_headers()
    if not headers: return
    venue_id = st.number_input("Venue ID to Update", min_value=1, step=1)
    new_name = st.text_input("New Venue Name")
    if st.button("Update Venue"):
        payload = {"name": new_name}
        try:
            response = requests.put(f"{BASE_URL}/venues/{venue_id}", json=payload, headers=headers)
            if response.status_code == 202:
                st.success(f"✅ Venue {venue_id} updated successfully!")
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Connection Error: {e}")


# ✅ Delete venue
def delete_venue():
    st.subheader("❌ Delete Venue")
    headers = get_auth_headers()
    if not headers: return
    venue_id = st.number_input("Venue ID to Delete", min_value=1, step=1)
    if st.button("Delete Venue"):
        try:
            response = requests.delete(f"{BASE_URL}/venues/{venue_id}", headers=headers)
            if response.status_code == 204:
                st.success(f"🗑️ Venue {venue_id} deleted successfully!")
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Connection Error: {e}")


# ✅ Main venue page
def venues_page():
    st.title("🏢 Venue Management")

    action = st.selectbox(
        "Choose Action",
        ["Show All Venues", "Show Venue By ID", "Add Venue", "Update Venue", "Delete Venue"]
    )

    if action == "Show All Venues":
        show_all_venues()
    elif action == "Show Venue By ID":
        show_venue_by_id()
    elif action == "Add Venue":
        add_venue()
    elif action == "Update Venue":
        update_venue()
    elif action == "Delete Venue":
        delete_venue()
