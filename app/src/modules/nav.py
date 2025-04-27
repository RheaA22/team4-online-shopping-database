# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has function to add certain functionality to the left side bar of the app

import streamlit as st


#### ------------------------ General ------------------------
def HomeNav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def AboutPageNav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


#### ------------------------ Role of Store_Manager ------------------------
def StoreManagerHomeNav():
    st.sidebar.page_link(
        "pages/00_Store_Manager_Home.py", label="Store Manager Home", icon="👤"
    )


def ProductManagementDashNav():
    st.sidebar.page_link(
        "pages/01_Product_Management_Dash.py", label="Product Management Dashboard", icon="🏦"
    )


def OrderManagementDashNav():
    st.sidebar.page_link("pages/02_Order_Management_Dash.py", label="Order Management Dashboard", icon="🗺️")


def CategoryManagementNav():
    st.sidebar.page_link("pages/05_Category_Management.py.py", label="Category Management Dashboard", icon="🗺️")


## ------------------------ Role of Eco-Conscious Teen ------------------------
def EcoConsciousTeenHomeNav():
    st.sidebar.page_link(
        "pages/10_Eco-Conscious_Teen_Home.py", label="Eco-Conscious Teen Home", icon="👤"
    )

def SustainableCategoriesViewNav():
    st.sidebar.page_link("pages/11_Manage_User_Profile.py", label="Manage User Profile", icon="🛜")


def EcoProductsViewNav():
    st.sidebar.page_link(
        "pages/12_Eco_Products_View.py", label="Eco-Friendly Products Viewer", icon="📈"
    )


def OrdersTrackerNav():
    st.sidebar.page_link(
        "pages/13_Orders_Tracker.py", label="Orders Tracker", icon="🌺"
    )


#### ------------------------ Sensory Sensitive Shopper Role ------------------------
def SensorySensitiveShopperNav():
    st.sidebar.page_link("pages/20_Sensory_Sensitive_Shopper_Home.py", label="Sensory Shopper Home", icon="🖥️")

    st.sidebar.page_link(
        "pages/21_Sensory_Friendly_Products.py", label="Sensory Friendly Products Viewer", icon="🏢"
    )
    st.sidebar.page_link(
        "pages/22_Sensory_Reviews.py", label="Sensory Reviews", icon="🏢"
    )
    st.sidebar.page_link(
        "pages/23_Clothing_Finder.py", label="Adaptable Clothing Finder", icon="🏢"
    )

#### ------------------------ Trend-Focused Influencer Role ------------------------
def TrendFocusedInfluencerNav():
    st.sidebar.page_link("pages/31_Trend-Focused_Influencer_Home.py.py", label="Trend Focused Influencer Home", icon="🖥️")
    st.sidebar.page_link(
        "pages/32_Trend_Dashboard.py", label="Trend Dashboard", icon="🏢"
    )
    st.sidebar.page_link(
        "pages/33_Create_Trendy_Order.py", label="Create Trendy Order", icon="🏢"
    )
    st.sidebar.page_link(
        "pages/34_Outfit_Recs.py", label="Outfit Recommendations", icon="🏢"
    )


# --------------------------------Links Function -----------------------------------------------
def SideBarLinks(show_home=False):
    """
    This function handles adding links to the sidebar of the app based upon the logged-in user's role, which was put in the streamlit session_state object when logging in.
    """

    # add a logo to the sidebar always
    st.sidebar.image("assets/clothingStoreLogo.png", width=150)

    # If there is no logged in user, redirect to the Home (Landing) page
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        # Show the Home page link (the landing page)
        HomeNav()

    # Show the other page navigators depending on the users' role.
    if st.session_state["authenticated"]:

        # Show Product Management Link, Order Management Link, and Category Management Link if the user is a Store Manager.
        if st.session_state["role"] == "Store_Manager":
            StoreManagerHomeNav()
            ProductManagementDashNav()
            OrderManagementDashNav()
            CategoryManagementNav()

        # If the user role is Eco-Conscious Teen, show the following pages
        if st.session_state["role"] == "Eco-Conscious_Teen":
            EcoConsciousTeenHomeNav()
            SustainableCategoriesViewNav()
            EcoProductsViewNav()
            OrdersTrackerNav()


        # If the user is an Sensory Sensitive Shopper, give them access to the sensory sensitive shopper pages
        if st.session_state["role"] == "Sensory_Sensitive_Shopper":
            SensorySensitiveShopperNav()
        
         # If the user is an Trend-Focused Influencer, give them access to the trend focused influencer pages
        if st.session_state["role"] == "Trend_Focused_Influencer":
            TrendFocusedInfluencerNav()

    # Always show the About page at the bottom of the list of links
    AboutPageNav()

    if st.session_state["authenticated"]:
        # Always show a logout button if there is a logged in user
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")
