import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)
BASE_URL = "http://web-api:4000"

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Product Management Dashboard')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

# View all products
if st.button("🔍 View All Products"):
    response = requests.get(f"{BASE_URL}/products")
    if response.ok:
        st.table(response.json())
    else:
        st.error("❌ Failed to fetch products")

# Update product
st.subheader("✏️ Update Product")
with st.form("update_product"):
    pid = st.text_input("Product ID to Update")
    new_name = st.text_input("New Name (optional)")
    new_price = st.number_input("New Price ($)", min_value=0.0, format="%.2f")
    new_brand = st.text_input("New Brand (optional)")
    new_features = st.text_area("New Features (comma-separated, optional)")
    new_category = st.text_input("New Category (optional)")

    submit_update = st.form_submit_button("Update Product")

    if submit_update:
        update_data = {}
        if new_name:
            update_data["name"] = new_name
        if new_price > 0:
            update_data["price"] = new_price
        if new_brand:
            update_data["brand"] = new_brand
        if new_features:
            features_list = [feature.strip() for feature in new_features.split(",") if feature.strip()]
            update_data["features"] = features_list
        if new_category:
            update_data["category"] = new_category

        if update_data:
            r = requests.put(f"{BASE_URL}/products/{pid}", json=update_data)
            if r.ok:
                st.success("✅ Product updated!")
            else:
                st.error("❌ Failed to update product")
        else:
            st.warning("⚠️ Please enter at least one field to update.")


# Mark product as out of stock
st.subheader("🚫 Mark Product Out of Stock")
product_id = st.text_input("Product ID to Mark Out of Stock")
if st.button("Mark as Out of Stock"):
    if product_id:
        r = requests.delete(f"{BASE_URL}/products/{product_id}")
        if r.ok:
            st.success("✅ Product marked out of stock!")
        else:
            st.error("❌ Failed to mark out of stock")
    else:
        st.warning("⚠️ Enter a product ID")



