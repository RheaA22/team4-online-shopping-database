import pandas as pd
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)
BASE_URL = "http://web-api:4000"

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Product Management Dashboard')

# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

# View all products
if st.button("🔍 View Current Inventory"):
    response = requests.get(f"{BASE_URL}/products")
    if response.ok:
        st.table(response.json())
    else:
        st.error("❌ Failed to fetch products")

# Add new product
st.subheader("Add New Product")
with st.form("add_product"):
    name = st.text_input("Product Name")
    price = st.number_input("Price ($)", min_value=0.0)
    stock = st.checkbox("In Stock", value=True)
    submit = st.form_submit_button("Add Product")
    if submit:
        data = {"name": name, "price": price, "stock": stock}
        r = requests.post(f"{BASE_URL}/products", json=data)
        st.success("✅ Product added!" if r.ok else "❌ Error adding product")

# Update product
st.subheader("Update Product Info")
with st.form("update_product"):
    pid = st.text_input("Product ID to update")
    new_name = st.text_input("New Name (leave blank to skip)")
    new_price = st.number_input("New Price", min_value=0.0, format="%.2f")
    submit_update = st.form_submit_button("Update Product")
    if submit_update:
        update_data = {}
        if new_name:
            update_data["name"] = new_name
        if new_price > 0:
            update_data["price"] = new_price
        if update_data:
            r = requests.put(f"{BASE_URL}/products", json=data)
            st.success("✅ Product updated!" if r.ok else "❌ Update failed")
        else:
            st.warning("⚠️ Please enter at least one field to update.")

# Mark product as out of stock
st.subheader("Mark Product as Out of Stock")
product_id = st.text_input("Product ID to mark as out of stock")
if st.button("Mark Out of Stock"):
    r = requests.delete(f"{BASE_URL}/products", json=data)
    st.success("✅ Product marked out of stock" if r.ok else "❌ Failed")
