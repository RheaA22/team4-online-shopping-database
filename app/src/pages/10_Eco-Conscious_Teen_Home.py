import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Eco-Conscious Teen Customer, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('Browse Sustainable Products', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/11_Sustainable_Products.py')

if st.button('View Eco Events', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/12_Eco_Events_View.py')

if st.button("Review Management Info",
             type='primary',
             use_container_width=True):
  st.switch_page('pages/13_Product_Reviews_Viewer.py')
