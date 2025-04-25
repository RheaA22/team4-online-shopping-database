import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()
st.header("Sensory Friendly Products")

# GET all products
resp = requests.get("http://localhost:5000/products")
if resp.ok:
    all_products = resp.json()
    keywords = ["soft", "tagless", "breathable", "seamless", "cotton", "gentle", "muted"]

    sensory_products = [
        p for p in all_products if any(k in p["name"].lower() for k in keywords)
    ]

    if sensory_products:
        for p in sensory_products:
            with st.expander(p["name"]):
                st.write(f"💲 ${p['price']}")
                st.write(f"🧾 SKU: {p['sku']}")
    else:
        st.warning("No sensory-friendly items available right now.")
else:
    st.error("Could not fetch products.")
