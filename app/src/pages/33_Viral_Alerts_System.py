import streamlit as st
from modules.nav import SideBarLinks

SideBarLinks()
st.header("Viral Alert System")

# Get viral items from fake API link
alerts = requests.get("https://fashion-api.example.com/alerts").json()

# Notification system
for alert in alerts["items"]:
    with st.container(border=True):
        col1, col2 = st.columns([1, 3])
        with col1:
            st.image(alert["image"], width=100)
        with col2:
            st.write(f"**🚨 {alert['name']}**")
            st.write(f"*Going viral on {alert['platform']}*")
            st.write(f"Price: ${alert['price']} | Stock: {alert['stock']}")
            if st.button("Buy Now", key=f"buy_{alert['id']}"):
                st.switch_page("pages/34_Purchase_Assistant.py")
