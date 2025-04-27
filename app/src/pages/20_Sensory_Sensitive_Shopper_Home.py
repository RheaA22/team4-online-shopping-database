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

if st.button('Edit Sensory-Specific Reviews',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/22_Sensory_Reviews.py')

if st.button('Find Adaptive Clothing',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/23_Clothing_Finder.py')
