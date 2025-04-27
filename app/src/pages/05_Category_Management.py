import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
import requests

logger = logging.getLogger(__name__)
BASE_URL = "http://web-api:4000"

SideBarLinks()

# set up the page
st.markdown("# View Categories")
st.sidebar.header("View Categories")

# View all categories
if st.button("📋 View Categories"):
    r = requests.get(f"{BASE_URL}/categories")
    if r.ok:
        st.table(r.json())
    else:
        st.error("❌ Failed to fetch categories")

# Add new category
st.subheader("Add New Category")
with st.form("add_category"):
    name = st.text_input("Category Name")
    submit = st.form_submit_button("Add")
    if submit:
        r = requests.post(f"{BASE_URL}/categories", json={"name": name})
        st.success("✅ Category added" if r.ok else "❌ Failed to add")

# Update category
st.subheader("Edit Category")
with st.form("edit_category"):
    cid = st.text_input("Category ID")
    new_name = st.text_input("New Category Name")
    submit = st.form_submit_button("Update Category")
    if submit:
        r = requests.put(f"{BASE_URL}/categories/{cid}", json={"name": new_name})
        st.success("✅ Category updated" if r.ok else "❌ Failed")
    else:
        st.warning("⚠️ Please enter at least one field to update.")

# Delete category
st.subheader("Delete Category")
cid_delete = st.text_input("Category ID to delete")
if st.button("Delete Category"):
    r = requests.delete(f"{BASE_URL}/categories/{cid_delete}")
    st.success("✅ Deleted category" if r.ok else "❌ Error")
