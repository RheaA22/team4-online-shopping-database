import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
from modules.db import execute_query
from datetime import datetime
import requests

logger = logging.getLogger(__name__)

SideBarLinks()

st.header('Order Management Dashboard')

# View all orders
if st.button("View All Orders"):
    r = requests.get("http://localhost:5000/orders")
    if r.ok:
        st.table(r.json())

# View single order
order_id = st.text_input("Order ID to view")
if st.button("🔍 View Order Details"):
    r = requests.get(f"http://localhost:5000/orders/{order_id}")
    if r.ok:
        st.json(r.json())

# Update order status
st.subheader("Update Order Status")
with st.form("update_order"):
    oid = st.text_input("Order ID")
    status = st.selectbox("New Status", ["Pending", "Shipped", "Delivered", "Cancelled"])
    submit = st.form_submit_button("Update Order")
    if submit:
        r = requests.put(f"http://localhost:5000/orders/{oid}", json={"status": status})
        st.success("✅ Order updated" if r.ok else "❌ Update failed")
