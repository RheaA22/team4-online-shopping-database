import streamlit as st
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.write("# About this App")

st.markdown (
    """
    This is a is an online clothing store management system, that is designed to make the shopping process easier for customers as well as store managers. 
    It is a full-fledged online clothing store management system with features that enable easy navigation, seamless transaction processing, and efficient stock management. 
    By providing a range of clothing options, the system seeks to satisfy the many demands of its clientele, including those who are ecologically concerned, disabled, have little knowledge of technology, or have sensory requirements. 
    Advanced filtering features on the website will enable users to locate clothing that meets their needs, including sustainable, adaptable, and mobility-supportive clothes. 
    In addition, store managers will be able to process orders, maintain inventory, make data-driven decisions to improve profit, and provide quick customer care. 
    With the integration of simple-to-use interfaces and adaptive functionality, the project aims to make the overall online shopping experience easy, accessible, inclusive, and efficient for all.


    Stay tuned for more information and features to come!
    """
        )
