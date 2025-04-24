import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
from modules.db import execute_query

logger = logging.getLogger(__name__)

# Display the appropriate sidebar links for the role of the logged in user
SideBarLinks()

st.header('Sustainable Fashion Finder')

# Tabs for different operations
tab1, tab2, tab3 = st.tabs(["Browse Products", "View Reviews", "Write Review"])

with tab1:
    # GET /products with eco filters (READ)
    st.subheader("Eco-Friendly Products")
    
    col1, col2 = st.columns(2)
    with col1:
        min_sustain_score = st.slider(
            "Minimum Sustainability Score", 
            min_value=0, max_value=10, value=7
        )
    with col2:
        cert_options = ['GOTS', 'OEKO-TEX', 'Fair Trade', 'Organic']
        certifications = st.multiselect(
            "Certifications", 
            options=cert_options
        )
    
    query = """
        SELECT p.SKU, p.name, p.price, p.material, p.eco_certification, 
               p.sustainability_score, b.name as brand_name
        FROM Product p
        JOIN Brand b ON p.brandID = b.brandID
        WHERE p.sustainability_score >= ?
    """
    params = [min_sustain_score]
    
    if certifications:
        query += " AND p.eco_certification IN (" + ",".join(["?"]*len(certifications)) + ")"
        params.extend(certifications)
    
    eco_products = execute_query(query, params)
    
    if eco_products:
        df = pd.DataFrame(eco_products)
        st.dataframe(df)
    else:
        st.warning("No products match your filters")

with tab2:
    # GET /reviews (READ)
    st.subheader("Product Reviews")
    if eco_products:
        product_options = {f"{p['name']} (SKU: {p['SKU']})": p['SKU'] for p in eco_products}
        selected = st.selectbox("Select product to see reviews", options=product_options.keys())
        
        if selected:
            sku = product_options[selected]
            reviews = execute_query("""
                SELECT r.rating, r.comfort_score, r.comment, c.firstName, c.lastName
                FROM Review r
                JOIN Customer c ON r.CustomerID = c.customerID
                WHERE r.SKU = ?
                ORDER BY r.rating DESC
            """, [sku])
            
            if reviews:
                for review in reviews:
                    with st.expander(f"{review['firstName']} {review['lastName']} - {review['rating']}★"):
                        st.write(f"**Comfort:** {review['comfort_score']}/5")
                        st.write(review['comment'])
            else:
                st.info("No reviews yet for this product")

with tab3:
    # POST /reviews (CREATE)
    st.subheader("Share Your Experience")
    if 'user_id' in st.session_state:
        if eco_products:
            product_options = {f"{p['name']} (SKU: {p['SKU']})": p['SKU'] for p in eco_products}
            selected = st.selectbox("Select product to review", options=product_options.keys())
            
            if selected:
                sku = product_options[selected]
                with st.form("add_review"):
                    rating = st.slider("Rating (1-5 stars)", 1, 5, 5)
                    comfort = st.slider("Comfort Score (1-5)", 1, 5, 5)
                    comment = st.text_area("Your review", 
                        placeholder="How was the quality? Was it truly sustainable?")
                    
                    if st.form_submit_button("Submit Review"):
                        review_id = f"REV-{pd.Timestamp.now().strftime('%Y%m%d%H%M%S')}"
                        execute_query(
                            """INSERT INTO Review 
                            (reviewID, comment, rating, comfort_score, CustomerID, SKU)
                            VALUES (?, ?, ?, ?, ?, ?)""",
                            (review_id, comment, rating, comfort, st.session_state['user_id'], sku),
                            is_update=True
                        )
                        st.success("Thanks for your review!")
        else:
            st.warning("No products available to review")
    else:
        st.warning("Please sign in to leave a review")
