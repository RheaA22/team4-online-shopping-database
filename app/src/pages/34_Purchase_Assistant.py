import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()
st.header("Purchase Assistant")

# Tracked items using fake API link
tracked = requests.get("https://fashion-api.example.com/tracked").json()

for item in tracked["items"]:
    with st.expander(f"{item['name']} (${item['price']})"):
        st.write(f"**Retailers:**")
        for retailer in item["retailers"]:
            st.write(f"- [{retailer['name']}]({retailer['url']}) (${retailer['price']})")
        
        # Price drop alert
        if item["price_drop"]:
            st.success(f"Price dropped {item['price_drop']}%!")
        
        if st.button("Stop Tracking", key=f"remove_{item['id']}"):
            requests.delete(f"https://fashion-api.example.com/tracked/{item['id']}")
            st.experimental_rerun()
