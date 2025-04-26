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
if st.button("🔍 View Current Inventory"):
    response = requests.get(f"{BASE_URL}/products")
    if response.ok:
        st.table(response.json())

# Add new product
st.subheader("Add New Product")
with st.form("add_product"):
    name = st.text_input("Product Name")
    price = st.number_input("Price ($)", min_value=0.0)
    category_id = st.text_input("Category ID")
    submit = st.form_submit_button("Add Product")
    if submit:
        data = {"name": name, "price": price, "category_id": category_id}
        r = requests.post(f"{BASE_URL}/products", json=data)
        st.success("✅ Product added!" if r.ok else "❌ Error adding product")

# Update product
st.subheader("Update Product Info")
with st.form("update_product"):
    pid = st.text_input("Product ID to update")
    new_price = st.number_input("New Price", min_value=0.0)
    tags = st.text_input("Tags (comma-separated)")
    submit_update = st.form_submit_button("Update Product")
    if submit_update:
        data = {"price": new_price, "tags": tags.split(",")}
        r = requests.put(f"http://localhost:4000/products/{pid}", json=data)
        st.success("✅ Product updated!" if r.ok else "❌ Update failed")

# Mark product as out of stock
st.subheader("Mark Product as Out of Stock")
product_id = st.text_input("Product ID to mark as out of stock")
if st.button("Mark Out of Stock"):
    r = requests.delete(f"http://localhost:4000/products/{product_id}")
    st.success("✅ Product marked out of stock" if r.ok else "❌ Failed")
