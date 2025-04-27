import streamlit as st
import requests
from modules.nav import SideBarLinks

SideBarLinks()
st.header("Product Reviews")
BASE_URL = "http://web-api:4000"

# View reviews for a sensory product
st.subheader("📝 View Reviews for Sensory Product")
review_pid = st.text_input("Product ID to View Reviews")
if st.button("View Reviews"):
    if review_pid:
        r = requests.get(f"{BASE_URL}/products/{review_pid}/reviews")
        if r.ok:
            reviews = r.json()
            if reviews:
                st.table(reviews)
            else:
                st.info("ℹ️ No reviews yet for this product.")
        else:
            st.error("❌ Failed to fetch reviews.")
    else:
        st.warning("⚠️ Enter a product ID.")

# Add review to sensory product
st.subheader("➕ Add Review for Sensory Product")
with st.form("add_review"):
    review_pid = st.text_input("Product ID to Review", key="review_pid")
    userId = st.number_input("Your User ID", min_value=1)
    rating = st.slider("Overall Rating", 1, 5)
    easeOfUse = st.slider("Ease of Use", 1, 5)
    sensoryComfort = st.slider("Sensory Comfort", 1, 5)
    comment = st.text_area("Comment")
    submit_review = st.form_submit_button("Submit Review")
    if submit_review:
        if review_pid:
            review_data = {
                "userId": userId,
                "rating": rating,
                "easeOfUse": easeOfUse,
                "sensoryComfort": sensoryComfort,
                "comment": comment
            }
            r = requests.post(f"{BASE_URL}/products/{review_pid}/reviews", json=review_data)
            if r.ok:
                st.success("✅ Review added!")
            else:
                st.error("❌ Failed to add review.")
        else:
            st.warning("⚠️ Enter a product ID to review.")
