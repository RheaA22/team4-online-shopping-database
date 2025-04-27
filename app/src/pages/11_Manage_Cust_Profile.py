import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.header("🌱 Manage Your Profile")
BASE_URL = "http://web-api:4000"

# Step 1: User enters their userID
user_id = st.number_input("Enter your User ID to view your profile:", min_value=1, step=1)

# Fetch customer details if user_id is provided
if user_id:
    response = requests.get(f"{BASE_URL}/customers/{user_id}")

    if response.ok:
        customer_data = response.json()

        if customer_data:
            customer = customer_data[0]  # Assuming the response is a list of one item

            # Display the current customer profile information
            st.subheader("Your Profile")
            st.write(f"**First Name**: {customer['first_name']}")
            st.write(f"**Last Name**: {customer['last_name']}")
            st.write(f"**Company**: {customer['company']}")

            # Allow the user to edit their profile
            st.subheader("Edit Your Profile")

            new_first_name = st.text_input("First Name", value=customer['first_name'])
            new_last_name = st.text_input("Last Name", value=customer['last_name'])
            new_company = st.text_input("Company", value=customer['company'])

            if st.button("Update Profile"):
                # Send updated data to the backend
                update_data = {
                    "id": user_id,
                    "first_name": new_first_name,
                    "last_name": new_last_name,
                    "company": new_company
                }

                update_response = requests.put(f"{BASE_URL}/customers", json=update_data)

                if update_response.ok:
                    st.success("Your profile has been updated successfully!")
                else:
                    st.error("Failed to update your profile. Please try again.")
        else:
            st.warning("No profile found for this user ID.")
    else:
        st.error("Error fetching your profile. Please try again.")








