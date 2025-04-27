import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()
BASE_URL = "http://web-api:4000"
st.header('👗 Trendy Outfit Recommendations')

# Fetch all products
response = requests.get(f"{BASE_URL}/products")
if response.ok:
    products = response.json()

    # Define logic: products in "general" category are considered trendy
    trendy_products = [p for p in products if p.get('category') == 'trendy' and p.get('stock', True)]

    if trendy_products:
        st.subheader("✨ Here’s what’s trending right now:")

        for product in trendy_products:
            with st.container():
                st.markdown(f"### {product['name']}")
                st.write(f"💵 Price: ${product['price']}")
                st.write(f"🛒 Available Now!")
                st.divider()
    else:
        st.info("No trendy items available at the moment. Check back soon!")
else:
    st.error("Failed to load products. Please try again later.")
