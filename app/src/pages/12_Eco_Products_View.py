import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)

SideBarLinks()

st.header('Sustainable Fashion Products')

# Get all products
response = requests.get("http://localhost:8501/products")
if response.ok:
    products = response.json()
    eco_keywords = ["sustainable", "organic", "eco", "recycled", "vegan"]
    eco_products = [
        p for p in products if any(word in p['name'].lower() for word in eco_keywords)
    ]

    if eco_products:
        for p in eco_products:
            with st.expander(p["name"]):
                st.write(f"💰 Price: ${p['price']}")
                st.write(f"🔢 SKU: {p['sku']}")
    else:
        st.info("No sustainable products found.")
else:
    st.error("Could not load products.")
