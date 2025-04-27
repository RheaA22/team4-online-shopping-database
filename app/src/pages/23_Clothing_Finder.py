import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()
st.header("Find Adaptive Clothing")
BASE_URL = "http://web-api:4000"

st.header('Personalized Sensory Preferences')

# Input for sensory preferences
selected_features = st.multiselect(
    "Select Sensory Features You Prefer",
    ["Tagless", "Magnetic Closures", "Seamless", "Stretch Fabric", "Minimal Seams"],
    help="Select the features that best match your sensory comfort needs."
)

if selected_features:
    # Get all products
    response = requests.get(f"{BASE_URL}/products")
    if response.ok:
        products = response.json()
        # Filter products based on selected sensory features
        filtered_products = [
            p for p in products if 'features' in p and any(feature in p['features'] for feature in selected_features)
        ]

        if filtered_products:
            for p in filtered_products:
                with st.expander(p["name"]):
                    st.write(f"💰 Price: ${p['price']}")
                    st.write(f"🔢 Category: {p['category']}")
                    st.write(f"👚 Features: {', '.join(p.get('features', []))}")
                    st.write(f"📦 In Stock: {'Yes' if p['stock'] else 'No'}")
        else:
            st.info("No products found matching your preferences.")
    else:
        st.error("Could not load products.")
else:
    st.info("Select sensory features to filter products.")
