import streamlit as st
import pandas as pd
from services.lead_api import get_leads

def render_dashboard():
    st.title("📊 Growth Dashboard")
    st.markdown("Overview of your outreach performance.")
    
    leads = get_leads()
    
    if not leads:
        st.info("No leads available yet. Head over to the Leads Pipeline to add some.")
        return
        
    df = pd.DataFrame(leads)
    
    total_leads = len(df)
    contacted = len(df[df['status'] == 'Contacted'])
    replied = len(df[df['status'] == 'Replied'])
    converted = len(df[df['status'] == 'Converted'])
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total Leads", total_leads)
    with col2:
        st.metric("Contacted", contacted)
    with col3:
        st.metric("Replied", replied)
    with col4:
        st.metric("Converted", converted)
        
    st.subheader("Lead Status Distribution")
    status_counts = df['status'].value_counts()
    st.bar_chart(status_counts)
