import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Sensory Sensitive Shopper Home Page')

if st.button('View Sensory Friendly Products', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/21_Sensory_Friendly_Products.py')

if st.button('Build Product Preferences', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Personalize_Preferences.py')

if st.button('Find My Orders', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Order_Finder.py')
