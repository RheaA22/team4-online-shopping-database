import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()
st.header("Saved Looks")

user_id = st.text_input("Enter your Customer ID")

if st.button("Show My Vibe"):
    user = requests.get(f"http://localhost:5000/users/{user_id}").json()
    pref_keywords = user.get("preferences", "").lower().split()

    products = requests.get("http://localhost:5000/products").json()
    aesthetic_matches = [
        p for p in products if any(k in p["name"].lower() for k in pref_keywords)
    ]

    if aesthetic_matches:
        for p in aesthetic_matches:
            st.subheader(p["name"])
            st.write(f"💲 ${p['price']}")
            st.write(f"📦 SKU: {p['sku']}")
            st.markdown("---")
    else:
        st.warning("No matching products found.")
