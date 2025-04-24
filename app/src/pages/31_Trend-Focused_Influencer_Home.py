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

if st.button('View Viral Alerts', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/33_Viral_Alerts_Systemd.py')

if st.button('View Purchase Assistant', 
             type='primary',
             use_container_width=True):
  st.switch_page('pages/34_Purchase_Assistant.py')
