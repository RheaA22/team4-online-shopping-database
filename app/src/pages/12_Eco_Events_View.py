import logging
import streamlit as st
import pandas as pd
from modules.nav import SideBarLinks
from modules.db import execute_query

logger = logging.getLogger(__name__)

SideBarLinks()

st.header('Sustainable Fashion Events')

# Tabs for different operations
tab1, tab2 = st.tabs(["Upcoming Events", "My Events"])

with tab1:
    # GET /events with sustainability filter (READ)
    st.subheader("Community Events")
    events = execute_query("""
        SELECT e.eventID, e.name, e.description, e.location, 
               strftime('%Y-%m-%d %H:%M', e.datetime) as event_time,
               m.firstName as organizer
        FROM VirtualEvent e
        JOIN Manager m ON e.managerID = m.managerID
        WHERE e.name LIKE '%Sustainable%' OR e.description LIKE '%Eco%'
        ORDER BY e.datetime
    """)
    
    if events:
        for event in events:
            with st.expander(f"{event['name']} - {event['event_time']}"):
                st.write(f"**Organizer:** {event['organizer']}")
                st.write(f"**Location:** {event['location']}")
                st.write(event['description'])
                
                # Simple attendance tracker
                if 'user_id' in st.session_state:
                    attending = execute_query(
                        "SELECT 1 FROM EventAttendees WHERE eventID = ? AND customerID = ?",
                        (event['eventID'], st.session_state['user_id'])
                    )
                    
                    if not attending:
                        if st.button("RSVP", key=f"rsvp_{event['eventID']}"):
                            execute_query(
                                "INSERT INTO EventAttendees (eventID, customerID) VALUES (?, ?)",
                                (event['eventID'], st.session_state['user_id']),
                                is_update=True
                            )
                            st.success("You're registered for this event!")
                    else:
                        st.info("You're attending this event")
                        if st.button("Cancel RSVP", key=f"cancel_{event['eventID']}"):
                            execute_query(
                                "DELETE FROM EventAttendees WHERE eventID = ? AND customerID = ?",
                                (event['eventID'], st.session_state['user_id']),
                                is_update=True
                            )
                            st.success("Registration cancelled")
                            st.experimental_rerun()
    else:
        st.info("No upcoming sustainable fashion events")

with tab2:
    # GET/PUT/DELETE for user's events
    if 'user_id' in st.session_state:
        st.subheader("Events You're Attending")
        my_events = execute_query("""
            SELECT e.eventID, e.name, e.description, 
                   strftime('%Y-%m-%d %H:%M', e.datetime) as event_time
            FROM VirtualEvent e
            JOIN EventAttendees a ON e.eventID = a.eventID
            WHERE a.customerID = ?
            ORDER BY e.datetime
        """, [st.session_state['user_id']])
        
        if my_events:
            for event in my_events:
                with st.expander(event['name']):
                    st.write(f"**When:** {event['event_time']}")
                    st.write(event['description'])
                    
                    if st.button("Cancel Attendance", key=f"cancel_{event['eventID']}"):
                        execute_query(
                            "DELETE FROM EventAttendees WHERE eventID = ? AND customerID = ?",
                            (event['eventID'], st.session_state['user_id']),
                            is_update=True
                        )
                        st.success("You're no longer attending this event")
                        st.experimental_rerun()
        else:
            st.info("You're not registered for any events yet")
    else:
        st.warning("Please sign in to view your events")
