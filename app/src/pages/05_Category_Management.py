import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
from modules.db import execute_query

logger = logging.getLogger(__name__)

SideBarLinks()

# set up the page
st.markdown("# View Categories")
st.sidebar.header("View Categories")



# View all categories
if st.button("📋 View Categories"):
    r = requests.get("http://localhost:5000/categories")
    if r.ok:
        st.table(r.json())

# Add new category
st.subheader("Add New Category")
with st.form("add_category"):
    name = st.text_input("Category Name")
    submit = st.form_submit_button("Add")
    if submit:
        r = requests.post("http://localhost:5000/categories", json={"name": name})
        st.success("✅ Category added" if r.ok else "❌ Failed to add")

# Update category
st.subheader("Edit Category")
with st.form("edit_category"):
    cid = st.text_input("Category ID")
    new_name = st.text_input("New Category Name")
    submit = st.form_submit_button("Update Category")
    if submit:
        r = requests.put(f"http://localhost:5000/categories/{cid}", json={"name": new_name})
        st.success("✅ Category updated" if r.ok else "❌ Failed")

# Delete category
st.subheader("Delete Category")
cid_delete = st.text_input("Category ID to delete")
if st.button("Delete Category"):
    r = requests.delete(f"http://localhost:5000/categories/{cid_delete}")
    st.success("✅ Deleted category" if r.ok else "❌ Error")
