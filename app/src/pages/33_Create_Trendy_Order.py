import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)
BASE_URL = "http://web-api:4000"

SideBarLinks()

st.header('Create My Trendy Order')
# Step 1: Load products
response = requests.get(f"{BASE_URL}/products")
if response.ok:
    products = response.json()

    if products:
        # Ask user for their user ID
        user_id = st.number_input("Enter your User ID:", min_value=1, step=1)

        product_names = [p['name'] for p in products if p.get('stock', True)]
        selected_products = st.multiselect("Select products you want to order:", product_names)

        if st.button("Create Order"):
            if selected_products and user_id:
                # Find IDs for the selected products
                selected_ids = [
                    idx + 1 for idx, p in enumerate(products)
                    if p['name'] in selected_products
                ]

                order_data = {
                    "user_id": user_id,
                    "items": selected_ids,
                    "status": "pending"
                }

                # POST to create order
                order_response = requests.post(f"{BASE_URL}/orders", json=order_data)

                if order_response.ok:
                    st.success("🎉 Order created successfully!")
                else:
                    st.error("❌ Failed to create order.")
            else:
                st.warning("⚠️ Please enter a valid User ID and select at least one product.")
    else:
        st.info("No products available.")
else:
    st.error("Could not load products.")
