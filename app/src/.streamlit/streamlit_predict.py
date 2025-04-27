import streamlit as st
import requests

# Base URL of your Flask app
BASE_URL = "http://localhost:5000"

st.title("Product Popularity Prediction")

# Collect user input
price = st.number_input("Enter Product Price ($)", min_value=0.0, format="%.2f")
feature_count = st.number_input("Enter Number of Special Features", min_value=0)

# Button to trigger prediction
if st.button("Predict Popularity"):
    if price and feature_count is not None:
        try:
            # Make request to Flask API
            response = requests.get(f"{BASE_URL}/products/predict/{price}/{feature_count}")
            if response.status_code == 200:
                prediction = response.json().get('prediction_result')
                st.success(f"Predicted Popularity Score: {prediction:.2f}")
            else:
                st.error("Failed to fetch prediction from server!")
        except Exception as e:
            st.error(f"Error contacting server: {e}")
