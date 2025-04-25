import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.header('Sustainable Fashion Finder')

# Get categories (e.g., Sustainable options)
r = requests.get("http://localhost:8501/categories")
categories = r.json() if r.ok else []
eco_categories = [cat for cat in categories if "eco" in cat["name"].lower() or "sustainable" in cat["name"].lower()]
selected_category = st.selectbox("♻️ Filter by Sustainable Category", [c["name"] for c in eco_categories])

# Get products by category
if selected_category:
    category_id = next((c["id"] for c in eco_categories if c["name"] == selected_category), None)
    if category_id:
        products = requests.get(f"http://localhost:8501/categories/{category_id}").json()
        st.subheader(f"🛒 Products in '{selected_category}'")
        for product in products:
            with st.expander(product["name"]):
                st.write(f"💰 Price: ${product['price']}")
                st.write(f"🧵 Tags: {', '.join(product.get('tags', []))}")
                if st.button("View Details", key=product["id"]):
                    detail = requests.get(f"http://localhost:8501/products/{product['id']}").json()
                    st.json(detail)
