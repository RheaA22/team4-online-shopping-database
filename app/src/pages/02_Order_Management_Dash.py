import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
from datetime import datetime
import requests

logger = logging.getLogger(__name__)
BASE_URL = "http://web-api:4000"

SideBarLinks()

st.header('Order Management Dashboard')

# View all orders
if st.button("View All Orders"):
    response = requests.get(f"{BASE_URL}/orders")
    if response.ok:
        st.table(response.json())
    else:
        st.error("❌ Failed to fetch products")

# View single order
order_id = st.text_input("Order ID to view")
if st.button("🔍 View Order Details"):
    r = requests.get(f"{BASE_URL}/orders/{order_id}")
    if r.ok:
        st.json(r.json())
    else:
        st.error("❌ Failed to fetch products")

# Update order status
st.subheader("Update Order Status")
with st.form("update_order"):
    oid = st.text_input("Order ID")
    status = st.selectbox("New Status", ["Pending", "Shipped", "Delivered", "Cancelled"])
    submit = st.form_submit_button("Update Order")
    if submit:
        r = requests.put(f"{BASE_URL}/orders/{oid}", json={"status": status})
        st.success("✅ Order updated" if r.ok else "❌ Update failed")
    else:
        st.warning("⚠️ Please enter at least one field to update.")
