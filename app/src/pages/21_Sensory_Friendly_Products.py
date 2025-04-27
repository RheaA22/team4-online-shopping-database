import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()
st.header("View Sensory Friendly Products")
BASE_URL = "http://web-api:4000"

#GET all sensory products (via category)
resp = requests.get(f"{BASE_URL}/products/category/sensory")
if resp.ok:
    sensory_products = resp.json()

    if sensory_products:
        for p in sensory_products:
            with st.expander(p["name"]):
                st.write(f"💲 ${p['price']}")
                st.write(f"🧾 Brand: {p.get('brand', 'Unknown')}")
                if p.get("features"):
                    st.write(f"✨ Features: {', '.join(p['features'])}")
                st.write(f"📦 Category: {p['category']}")
    else:
        st.warning("No sensory-friendly items available right now.")
else:
    st.error("❌ Could not fetch sensory products.")



