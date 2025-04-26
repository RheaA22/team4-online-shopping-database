import logging

logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks
import requests

SideBarLinks()

st.sidebar.header('Track My Order')

user_id = st.text_input("Enter your Customer ID", key="customer_id")
if user_id and st.button("View My Orders"):
    orders = requests.get("http://localhost:4000/orders").json()
    my_orders = [o for o in orders if o["customer_id"] == user_id]

    if my_orders:
        for order in my_orders:
            with st.expander(f"🧾 Order #{order['order_id']} — {order['date']}"):
                st.write(f"🛍️ Status: {order['status']}")
                st.write(f"🧑 Customer ID: {order['customer_id']}")
                st.write(f"💳 Total: ${order['total']}")
    else:
        st.info("No orders found.")
