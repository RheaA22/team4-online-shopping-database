import streamlit as st
import requests
from collections import Counter
from modules.nav import SideBarLinks

BASE_URL = "http://web-api:4000"
SideBarLinks()
st.header("Trend Dashboard")


# Get Order and Products
products = requests.get(f"{BASE_URL}/products").json()
product_lookup = {i + 1: p for i, p in enumerate(products)}

# Fetch orders
orders = requests.get(f"{BASE_URL}/orders").json()

# Count product appearances
all_items = []
for order in orders:
    all_items.extend(order["items"])

top_skus = Counter(all_items).most_common(5)

# Display trending products
for sku, count in top_skus:
    p = product_lookup.get(sku)
    if p:
        st.subheader(p["name"])
        st.write(f"📦 Ordered {count} time(s)")
        st.write(f"💲 ${p['price']}")
        st.markdown("---")
    else:
        st.write("❌ Product not found for SKU:", sku)
