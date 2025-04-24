import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
from modules.db import execute_query
from datetime import datetime

logger = logging.getLogger(__name__)

SideBarLinks()

st.header('Virtual Event Tracker')

# Tabs for event management
tab1, tab2, tab3 = st.tabs(["View Events", "Create Event", "Manage Events"])

with tab1:
    # GET /events (READ operation)
    st.subheader("Upcoming Virtual Events")
    events = execute_query("""
        SELECT eventID, name, managerID, 
               strftime('%Y-%m-%d %H:%M', event_datetime) as event_time
        FROM virtual_events
        WHERE event_datetime >= datetime('now')
        ORDER BY event_datetime
    """)
    
    if events:
        st.dataframe(pd.DataFrame(events))
    else:
        st.info("No upcoming virtual events")

with tab2:
    # POST /events (CREATE operation)
    st.subheader("Schedule New Event")
    with st.form("create_event"):
        event_name = st.text_input("Event Name*", required=True)
        manager_id = st.text_input("Your Manager ID*", required=True)
        event_date = st.date_input("Event Date*", min_value=datetime.today())
        event_time = st.time_input("Event Time*")
        
        if st.form_submit_button("Schedule Event"):
            event_datetime = f"{event_date} {event_time}"
            event_id = f"EVT-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
            try:
                execute_query(
                    """INSERT INTO virtual_events 
                    (eventID, name, managerID, event_datetime)
                    VALUES (?, ?, ?, ?)""",
                    (event_id, event_name, manager_id, event_datetime),
                    is_update=True
                )
                st.success(f"Event '{event_name}' scheduled successfully!")
            except Exception as e:
                st.error(f"Error creating event: {str(e)}")

with tab3:
    # PUT /events/{id} and DELETE /events/{id} (UPDATE/DELETE operations)
    st.subheader("Manage Existing Events")
    all_events = execute_query("SELECT eventID, name FROM virtual_events")
    
    if all_events:
        event_options = {
            f"{event['name']} (ID: {event['eventID']})": event['eventID']
            for event in all_events
        }
        selected = st.selectbox("Select event to manage", options=event_options.keys())
        
        if selected:
            event_id = event_options[selected]
            event_data = execute_query(
                "SELECT * FROM virtual_events WHERE eventID = ?", 
                (event_id,)
            )[0]
            
            col1, col2 = st.columns(2)
            
            with col1:
                # UPDATE form
                with st.form("update_event"):
                    new_name = st.text_input("Event Name", value=event_data['name'])
                    new_datetime = st.text_input("Event Time", value=event_data['event_datetime'])
                    
                    if st.form_submit_button("Update Event"):
                        execute_query(
                            """UPDATE virtual_events SET 
                            name = ?, event_datetime = ?
                            WHERE eventID = ?""",
                            (new_name, new_datetime, event_id),
                            is_update=True
                        )
                        st.success("Event updated successfully!")
            
            with col2:
                # DELETE button
                if st.button("Delete Event", type="primary"):
                    execute_query(
                        "DELETE FROM virtual_events WHERE eventID = ?",
                        (event_id,),
                        is_update=True
                    )
                    st.success("Event deleted successfully!")
                    st.experimental_rerun()
    else:
        st.warning("No events to manage")
