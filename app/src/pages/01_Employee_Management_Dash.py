import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
from modules.db import execute_query

logger = logging.getLogger(__name__)

# Call the SideBarLinks from the nav module in the modules directory
SideBarLinks()

# set the header of the page
st.header('Employee Management Dashboard')


# You can access the session state to make a more customized/personalized app experience
st.write(f"### Hi, {st.session_state['first_name']}.")

# Tabs for different operations
tab1, tab2, tab3, tab4 = st.tabs(["View Employees", "Add Employee", "Update Employee", "Delete Employee"])

with tab1:
    # GET /users (READ operation)
    st.subheader("All Employees")
    employees = execute_query("""
        SELECT employeeID, first_name, middle_name, last_name, email, storeID 
        FROM employees
        ORDER BY last_name, first_name
    """)
    
    if employees:
        st.dataframe(pd.DataFrame(employees))
    else:
        st.warning("No employee records found")

with tab2:
    # POST /users (CREATE operation)
    st.subheader("Add New Employee")
    with st.form("add_employee"):
        col1, col2 = st.columns(2)
        
        with col1:
            first_name = st.text_input("First Name*", required=True)
            middle_name = st.text_input("Middle Name")
            last_name = st.text_input("Last Name*", required=True)
        
        with col2:
            email = st.text_input("Email*", required=True)
            storeID = st.number_input("Store ID*", min_value=1, step=1)
            employeeID = st.text_input("Employee ID*", required=True)
        
        if st.form_submit_button("Add Employee"):
            try:
                execute_query(
                    """INSERT INTO employees 
                    (employeeID, first_name, middle_name, last_name, email, storeID)
                    VALUES (?, ?, ?, ?, ?, ?)""",
                    (employeeID, first_name, middle_name, last_name, email, storeID),
                    is_update=True
                )
                st.success("Employee added successfully!")
            except Exception as e:
                st.error(f"Error adding employee: {str(e)}")

with tab3:
    # PUT /users/{id} (UPDATE operation)
    st.subheader("Update Employee Information")
    if employees:
        employee_options = {
            f"{emp['last_name']}, {emp['first_name']} (ID: {emp['employeeID']})": emp['employeeID']
            for emp in employees
        }
        selected = st.selectbox("Select employee to update", options=employee_options.keys())
        
        if selected:
            emp_id = employee_options[selected]
            emp_data = execute_query(
                "SELECT * FROM employees WHERE employeeID = ?", 
                (emp_id,)
            )[0]
            
            with st.form("update_employee"):
                col1, col2 = st.columns(2)
                
                with col1:
                    new_first = st.text_input("First Name", value=emp_data['first_name'])
                    new_middle = st.text_input("Middle Name", value=emp_data['middle_name'])
                    new_last = st.text_input("Last Name", value=emp_data['last_name'])
                
                with col2:
                    new_email = st.text_input("Email", value=emp_data['email'])
                    new_store = st.number_input(
                        "Store ID", 
                        min_value=1, 
                        value=emp_data['storeID']
                    )
                
                if st.form_submit_button("Update Employee"):
                    execute_query(
                        """UPDATE employees SET 
                        first_name = ?, middle_name = ?, last_name = ?,
                        email = ?, storeID = ?
                        WHERE employeeID = ?""",
                        (new_first, new_middle, new_last, new_email, new_store, emp_id),
                        is_update=True
                    )
                    st.success("Employee updated successfully!")

with tab4:
    # DELETE /users/{id} (DELETE operation)
    st.subheader("Remove Employee")
    if employees:
        employee_options = {
            f"{emp['last_name']}, {emp['first_name']} (ID: {emp['employeeID']})": emp['employeeID']
            for emp in employees
        }
        selected = st.selectbox("Select employee to remove", options=employee_options.keys())
        
        if selected:
            emp_id = employee_options[selected]
            if st.button("Delete Employee", type="primary"):
                execute_query(
                    "DELETE FROM employees WHERE employeeID = ?",
                    (emp_id,),
                    is_update=True
                )
                st.success("Employee deleted successfully!")
                st.experimental_rerun()  # Refresh the page
    else:
        st.warning("No employees to delete")
