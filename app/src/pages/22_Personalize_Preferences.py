import streamlit as st
import requests
from modules.nav import SideBarLinks


SideBarLinks()
st.header("Product Preferences")

user_id = st.text_input("Enter your Customer ID")
preferences = st.text_area("What do you look for in clothing? (e.g. tagless, soft fabrics, neutral colors)")

if st.button("Update Preferences"):
    payload = {
        "preferences": preferences
    }
    res = requests.put(f"http://localhost:5000/users/{user_id}", json=payload)
    if res.ok:
        st.success("Preferences updated!")
    else:
        st.error("Could not update preferences.")
