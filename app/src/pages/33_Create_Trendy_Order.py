import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()
st.header("Create My Trendy Order")

name = st.text_input("Name")
email = st.text_input("Email")
products = requests.get("http://localhost:5000/products").json()

selected_skus = st.multiselect(
    "Choose products to match your vibe:",
    options=[p["sku"] for p in products],
    format_func=lambda sku: next((p["name"] for p in products if p["sku"] == sku), sku)
)

if st.button("Place Order"):
    payload = {
        "customer": {"name": name, "email": email},
        "products": selected_skus
    }
    res = requests.post("http://localhost:5000/orders", json=payload)
    if res.ok:
        st.success("Order placed!")
    else:
        st.error("Could not create order.")
