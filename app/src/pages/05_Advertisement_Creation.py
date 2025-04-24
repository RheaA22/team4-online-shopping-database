import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
from modules.db import execute_query

logger = logging.getLogger(__name__)

SideBarLinks()

# add the logo
add_logo("assets/logo.png", height=400)

# set up the page
st.markdown("# Advertisement Creation")
st.sidebar.header("Advertisement Creation")



# Tabs for ad management
tab1, tab2, tab3, tab4 = st.tabs(["View Ads", "Create Ad", "Update Ad", "Delete Ad"])

with tab1:
    # GET /ads (READ operation)
    st.subheader("Current Advertisements")
    ads = execute_query("""
        SELECT adID, content, target_segment, managerID,
               strftime('%Y-%m-%d', created_at) as created_date
        FROM advertisements
        ORDER BY created_at DESC
    """)
    
    if ads:
        st.dataframe(pd.DataFrame(ads))
    else:
        st.info("No advertisements created yet")

with tab2:
    # POST /ads (CREATE operation)
    st.subheader("Create New Advertisement")
    with st.form("create_ad"):
        manager_id = st.text_input("Your Manager ID*", required=True)
        ad_content = st.text_area("Ad Content*", height=200, required=True)
        
        target_options = [
            "Teens", "Young Adults", "Adults", "Seniors",
            "Eco-Conscious", "Budget Shoppers", "Luxury Buyers",
            "Adaptive Clothing", "Trend Followers"
        ]
        target_segment = st.multiselect(
            "Target Segment(s)*", 
            options=target_options,
            default=["Young Adults"],
            required=True
        )
        
        if st.form_submit_button("Create Advertisement"):
            ad_id = f"AD-{pd.Timestamp.now().strftime('%Y%m%d%H%M%S')}"
            
            try:
                execute_query(
                    """INSERT INTO advertisements 
                    (adID, content, managerID, target_segment)
                    VALUES (?, ?, ?, ?)""",
                    (ad_id, ad_content, manager_id, ",".join(target_segment)),
                    is_update=True
                )
                st.success("Advertisement created successfully!")
            except Exception as e:
                st.error(f"Error creating ad: {str(e)}")

with tab3:
    # PUT /ads/{id} (UPDATE operation)
    st.subheader("Update Existing Advertisement")
    if ads:
        ad_options = {
            f"Ad {ad['adID']}": ad['adID']
            for ad in ads
        }
        selected = st.selectbox("Select ad to update", options=ad_options.keys())
        
        if selected:
            ad_id = ad_options[selected]
            ad_data = execute_query(
                "SELECT * FROM advertisements WHERE adID = ?", 
                (ad_id,)
            )[0]
            
            with st.form("update_ad"):
                new_content = st.text_area(
                    "Ad Content*", 
                    value=ad_data['content'],
                    height=200,
                    required=True
                )
                
                current_segments = ad_data['target_segment'].split(",")
                new_segments = st.multiselect(
                    "Update Target Segments*",
                    options=target_options,
                    default=current_segments,
                    required=True
                )
                
                if st.form_submit_button("Update Advertisement"):
                    execute_query(
                        """UPDATE advertisements SET 
                        content = ?, target_segment = ?
                        WHERE adID = ?""",
                        (new_content, ",".join(new_segments), ad_id),
                        is_update=True
                    )
                    st.success("Advertisement updated successfully!")

with tab4:
    # DELETE /ads/{id} (DELETE operation)
    st.subheader("Remove Advertisement")
    if ads:
        ad_options = {
            f"Ad {ad['adID']}": ad['adID']
            for ad in ads
        }
        selected = st.selectbox("Select ad to delete", options=ad_options.keys())
        
        if selected:
            ad_id = ad_options[selected]
            if st.button("Delete Advertisement", type="primary"):
                execute_query(
                    "DELETE FROM advertisements WHERE adID = ?",
                    (ad_id,),
                    is_update=True
                )
                st.success("Advertisement deleted successfully!")
                st.experimental_rerun()
    else:
        st.warning("No advertisements to delete")
