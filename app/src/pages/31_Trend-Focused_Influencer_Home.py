import logging
logger = logging.getLogger(__name__)

import streamlit as st
from modules.nav import SideBarLinks
import requests

st.set_page_config(layout = 'wide')

SideBarLinks()

st.title('Trend Focused Influencer Home Page')

if st.button('View Trend Dashboard', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/32_Trend_Dashboard.py')

if st.button('Create a Trend-Focused Order', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/33_Create_Trendy_Order.py')

if st.button('View Trendy Outfit Reccommendations',
             type='primary',
             use_container_width=True):
  st.switch_page('pages/34_Outfit_Recs.py')
