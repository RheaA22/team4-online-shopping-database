import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()
BASE_URL = "http://web-api:4000"

# Streamlit header for the feature page
st.header('Update Your User Information')

# Get the user ID from the user input
user_id = st.number_input("Enter your User ID:", min_value=1, step=1)

# Fetch the current user data from the Flask back-end
if user_id:
    response = requests.get(f"{BASE_URL}/users/{user_id}")

    if response.ok:
        user_data = response.json()

        if user_data:
            st.write("Current Information:")
            st.write(user_data)

            # Create input fields for updating the user's name and preferences
            name = st.text_input("Name", user_data.get('name'))
            preferences = st.text_input("Preferences (comma separated)", ', '.join(user_data.get('preferences', [])))

            # Handle the "Update Information" button click
            if st.button("Update Information"):
                # Prepare the updated data for the PUT request
                updated_data = {
                    "name": name,
                    "preferences": [pref.strip() for pref in preferences.split(',')]
                }

                update_response = requests.put(f"{BASE_URL}/users/{user_id}", json=updated_data)

                if update_response.ok:
                    st.success("User information updated successfully!")
                else:
                    st.error("Failed to update user information.")
        else:
            st.error("User not found.")
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
