import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks

st.set_page_config(layout = 'wide')

# Show appropriate sidebar links for the role of the currently logged in user
SideBarLinks()

st.title(f"Welcome Store Manager, {st.session_state['first_name']}.")
st.write('')
st.write('')
st.write('### What would you like to do today?')

if st.button('View Product Management Dashboard', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/01_Product_Management_Dash.py')

if st.button('View Order Management Dashboard', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/02_Order_Management_Dash.py')

if st.button('Manage Categories', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/05_Category_Management.py')
