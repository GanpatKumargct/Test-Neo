import streamlit as st
import os

st.set_page_config(
    page_title="TestNeo Growth Console",
    page_icon="🚀",
    layout="wide"
)

# Custom Styling for modern look
st.markdown("""
<style>
    .reportview-container {
        background: #f0f2f6;
    }
    .sidebar .sidebar-content {
        background: #ffffff;
    }
    .css-1d391kg {
        padding-top: 2rem;
    }
</style>
""", unsafe_allow_html=True)

from pages.dashboard.dashboard import render_dashboard
from pages.leads.list import render_leads
from pages.upload.csv_upload import render_csv_upload

# Initialize session state for navigation
if 'page' not in st.session_state:
    st.session_state.page = "Dashboard"

# Sidebar Navigation
with st.sidebar:
    st.image("src/TestNeoLogo.png", width=150)
    st.title("Growth Console")
    
    if st.button("📊 Dashboard", use_container_width=True):
        st.session_state.page = "Dashboard"
    if st.button("👥 Leads Pipeline", use_container_width=True):
        st.session_state.page = "Leads"
    if st.button("📂 CSV Upload", use_container_width=True):
        st.session_state.page = "Upload"

# Main Content Area
if st.session_state.page == "Dashboard":
    render_dashboard()
elif st.session_state.page == "Leads":
    render_leads()
elif st.session_state.page == "Upload":
    render_csv_upload()
