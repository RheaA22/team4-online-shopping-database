import streamlit as st
import requests

# Base URL where Flask is running
BASE_URL = "http://localhost:5000"

st.title("Customer Behavior Prediction")

# Collect user inputs
var01 = st.number_input("Enter Variable 1 (e.g., Customer Age)", min_value=0.0, format="%.2f")
var02 = st.number_input("Enter Variable 2 (e.g., Number of Past Purchases)", min_value=0.0, format="%.2f")

# Prediction button
if st.button("Predict Customer Behavior"):
    if var01 is not None and var02 is not None:
        try:
            # Send GET request to Flask
            response = requests.get(f"{BASE_URL}/prediction/{var01}/{var02}")
            if response.status_code == 200:
                result = response.json().get('result')
                st.success(f"Predicted Value: {result:.2f}")
            else:
                st.error("Failed to fetch prediction from server!")
        except Exception as e:
            st.error(f"Error contacting server: {e}")
