import streamlit as st
import requests
from datetime import datetime
from config import BACKEND_URL

BASE_URL = f"{BACKEND_URL}/bookings"  # adjust if needed


# ✅ Helper function for headers
def get_auth_headers():
    if "token" not in st.session_state:
        st.error("‼️ Please login first.")
        return None
    return {"Authorization": f"Bearer {st.session_state['token']}"}


# ✅ Create booking
def create_booking():
    st.subheader("📝 Create Booking")
    headers = get_auth_headers()
    if not headers: return
    
    venue_id = st.number_input("Venue ID", min_value=1, step=1)
    # Start Date & Time on the same line
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date")
    with col2:
        start_time = st.time_input("Start Time")

    # End Date & Time on the same line
    col3, col4 = st.columns(2)
    with col3:
        end_date = st.date_input("End Date")
    with col4:
        end_time = st.time_input("End Time")
    start_datetime = datetime.combine(start_date, start_time)
    end_datetime = datetime.combine(end_date, end_time)

    if st.button("Book Venue"):
        try:
            payload = {
                "venue_id": venue_id,
                "start_time": start_datetime.isoformat(),
                "end_time": end_datetime.isoformat()
            }
            response = requests.post(BASE_URL, json=payload, headers=headers)
            if response.status_code == 201:
                st.success("✅ Booking created successfully!")
                st.json(response.json())
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Error: {e}")


# ✅ Get all bookings (Admin only)
def get_all_bookings():
    st.subheader("📋 All Bookings (Admin Only)")
    headers = get_auth_headers()
    if not headers: return
    if st.button("Fetch All Bookings"):
        try:
            response = requests.get(BASE_URL, headers=headers)
            if response.status_code == 200:
                st.json(response.json())
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Error: {e}")


# ✅ Get booking by ID
def get_booking_by_id():
    st.subheader("🔍 Get Booking by ID")
    headers = get_auth_headers()
    if not headers: return
    booking_id = st.number_input("Booking ID", min_value=1, step=1)
    if st.button("Fetch Booking"):
        try:
            response = requests.get(f"{BASE_URL}/{booking_id}", headers=headers)
            if response.status_code == 200:
                st.json(response.json())
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Error: {e}")


# ✅ Update booking
def update_booking():
    st.subheader("✏️ Update Booking")
    headers = get_auth_headers()
    if not headers: return
    booking_id = st.number_input("Booking ID to Update", min_value=1, step=1)
    # Start Date & Time on the same line
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start Date")
    with col2:
        start_time = st.time_input("Start Time")

    # End Date & Time on the same line
    col3, col4 = st.columns(2)
    with col3:
        end_date = st.date_input("End Date")
    with col4:
        end_time = st.time_input("End Time")
    start_datetime = datetime.combine(start_date, start_time)
    end_datetime = datetime.combine(end_date, end_time)

    if st.button("Update Booking"):
        try:
            payload = {
                "start_time": start_datetime.isoformat(),
                "end_time": end_datetime.isoformat()
            }
            response = requests.put(f"{BASE_URL}/{booking_id}", json=payload, headers=headers)
            if response.status_code == 202:
                st.success("✅ Booking updated successfully!")
                st.json(response.json())
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Error: {e}")


# ✅ Delete booking
def delete_booking():
    st.subheader("🗑️ Delete Booking")
    headers = get_auth_headers()
    if not headers: return
    booking_id = st.number_input("Booking ID to Delete", min_value=1, step=1)
    if st.button("Delete Booking"):
        try:
            response = requests.delete(f"{BASE_URL}/{booking_id}", headers=headers)
            if response.status_code == 204:
                st.success(f"✅ Booking {booking_id} deleted successfully!")
            else:
                st.error(f"⚠️ {response.json().get('detail')}")
        except Exception as e:
            st.error(f"🚨 Error: {e}")


# ✅ Main Booking Page
def bookings_page():
    st.title("📅 Booking Management")
    action = st.selectbox(
        "Choose Action",
        ["Create Booking", "Get All Bookings", "Get Booking By ID", "Update Booking", "Delete Booking"]
    )

    if action == "Create Booking":
        create_booking()
    elif action == "Get All Bookings":
        get_all_bookings()
    elif action == "Get Booking By ID":
        get_booking_by_id()
    elif action == "Update Booking":
        update_booking()
    elif action == "Delete Booking":
        delete_booking()
