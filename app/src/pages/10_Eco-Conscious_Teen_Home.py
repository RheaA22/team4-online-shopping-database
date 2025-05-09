import logging
logger = logging.getLogger(__name__)
import requests

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Eco-Conscious Teen Customer, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Manage My Profile',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Manage_User_Profile.py')

if st.button('View Eco-Friendly Products',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Eco_Products_View.py')

if st.button("Track My Order",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Orders_Tracker.py')
