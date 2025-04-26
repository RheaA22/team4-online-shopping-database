import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()
st.header("Find Adaptive Clothing")

customer_id = st.text_input("🔐 Customer ID", key="cust_id")

if st.button("View My Orders"):
    orders = requests.get("http://localhost:4000/orders").json()
    user_orders = [o for o in orders if o["customer_id"] == customer_id]

    if user_orders:
        for o in user_orders:
            st.markdown("---")
            st.write(f"🛒 Order ID: {o['order_id']}")
            st.write(f"📅 Date: {o['date']}")
            st.write(f"🚚 Status: {o['status']}")
            st.write(f"💳 Total: ${o['total']}")
    else:
        st.info("No orders found.")
