import logging
logger = logging.getLogger(__name__)
import streamlit as st
import pandas as pd
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from streamlit_extras.app_logo import add_logo
from modules.nav import SideBarLinks

SideBarLinks()

st.sidebar.header('My Product Reviews')


if 'user_id' not in st.session_state:
    st.warning("Please sign in to view your reviews")
else:
    # Tabs for different operations
    tab1, tab2 = st.tabs(["My Reviews", "Update Review"])

    with tab1:
        # GET /reviews for user (READ)
        st.subheader("Reviews You've Written")
        reviews = execute_query("""
            SELECT r.reviewID, r.comment, r.rating, r.comfort_score, 
                   r.created_at, p.name as product_name, p.SKU
            FROM Review r
            JOIN Product p ON r.SKU = p.SKU
            WHERE r.CustomerID = ?
            ORDER BY r.created_at DESC
        """, [st.session_state['user_id']])
        
        if reviews:
            for review in reviews:
                with st.expander(f"{review['product_name']} - {review['rating']}★"):
                    st.write(f"**Comfort Score:** {review['comfort_score']}/5")
                    st.write(f"**Reviewed on:** {review['created_at']}")
                    st.write(review['comment'])
                    
                    if st.button("Delete Review", key=f"del_{review['reviewID']}"):
                        execute_query(
                            "DELETE FROM Review WHERE reviewID = ?",
                            [review['reviewID']],
                            is_update=True
                        )
                        st.success("Review deleted")
                        st.experimental_rerun()
        else:
            st.info("You haven't written any reviews yet")

    with tab2:
        # PUT /reviews/{id} (UPDATE)
        st.subheader("Update a Review")
        if reviews:
            review_options = {
                f"{r['product_name']} ({r['created_at']})": r['reviewID']
                for r in reviews
            }
            selected = st.selectbox("Select review to update", options=review_options.keys())
            
            if selected:
                review_id = review_options[selected]
                review_data = execute_query(
                    "SELECT * FROM Review WHERE reviewID = ?",
                    [review_id]
                )[0]
                
                with st.form("update_review"):
                    new_rating = st.slider("Rating", 1, 5, review_data['rating'])
                    new_comfort = st.slider("Comfort Score", 1, 5, review_data['comfort_score'])
                    new_comment = st.text_area("Your updated review", value=review_data['comment'])
                    
                    if st.form_submit_button("Update Review"):
                        execute_query(
                            """UPDATE Review SET 
                            comment = ?, rating = ?, comfort_score = ?
                            WHERE reviewID = ?""",
                            (new_comment, new_rating, new_comfort, review_id),
                            is_update=True
                        )
                        st.success("Review updated successfully!")
                        st.experimental_rerun()
        else:
            st.warning("No reviews to update")
