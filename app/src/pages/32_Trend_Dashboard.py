import streamlit as st
import requests
from collections import Counter
from modules.nav import SideBarLinks

SideBarLinks()
st.header("Trend Dashboard")

#Get Order and Products
orders = requests.get("http://localhost:5000/orders").json()
products = requests.get("http://localhost:5000/products").json()
product_lookup = {p["sku"]: p for p in products}

#Count product appearances
all_items = []
for order in orders:
    all_items.extend(order["products"])  # assuming each order has "products": [SKUs]

top_skus = Counter(all_items).most_common(5)

#Display trending products
for sku, count in top_skus:
    p = product_lookup.get(sku)
    if p:
        st.subheader(p["name"])
        st.write(f"📦 Ordered {count} times")
        st.write(f"💲 ${p['price']}")
        st.markdown("---")
