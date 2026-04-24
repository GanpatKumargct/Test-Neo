import streamlit as st
import pandas as pd
from services.lead_api import get_leads, create_lead, update_lead, score_lead, generate_message

def render_leads():
    st.title("👥 Leads Pipeline")
    
    tab1, tab2 = st.tabs(["View Pipeline", "Add Lead"])
    
    with tab1:
        leads = get_leads()
        if not leads:
            st.info("No leads found.")
        else:
            df = pd.DataFrame(leads)
            
            # 1. Sticky ordering: sort by ID so rows don't jump around
            if 'id' in df.columns:
                df = df.sort_values(by="id", ascending=True).reset_index(drop=True)
            
            # 2. Filter by Status
            st.markdown("### Filters")
            all_statuses = ["All", "New", "Contacted", "Replied", "Demo Scheduled", "Converted", "Dropped"]
            # Add any other statuses that might exist in data but not in predefined list
            unique_statuses = df['status'].unique().tolist() if 'status' in df.columns else []
            for s in unique_statuses:
                if s not in all_statuses and pd.notna(s):
                    all_statuses.append(s)
                    
            selected_filter = st.selectbox("Filter by Status", options=all_statuses)
            
            if selected_filter != "All":
                df = df[df['status'] == selected_filter].reset_index(drop=True)
            
            # Display important columns
            display_cols = ['id', 'name', 'company', 'role', 'status', 'score', 'linkedin_url', 'website']
            
            # 3. Pagination (10 per page)
            if "current_page" not in st.session_state:
                st.session_state.current_page = 1
                
            ITEMS_PER_PAGE = 10
            total_items = len(df)
            total_pages = max(1, (total_items - 1) // ITEMS_PER_PAGE + 1)
            
            if st.session_state.current_page > total_pages:
                st.session_state.current_page = total_pages
                
            start_idx = (st.session_state.current_page - 1) * ITEMS_PER_PAGE
            end_idx = start_idx + ITEMS_PER_PAGE
            
            df_page = df.iloc[start_idx:end_idx]
            
            st.dataframe(
                df_page[[c for c in display_cols if c in df.columns]], 
                use_container_width=True,
                column_config={
                    "linkedin_url": st.column_config.LinkColumn("LinkedIn", display_text="link"),
                    "website": st.column_config.LinkColumn("Website", display_text="link")
                }
            )
            
            # Pagination Controls
            if total_pages > 1:
                col_p1, col_p2, col_p3 = st.columns([1, 2, 1])
                with col_p1:
                    if st.button("< Previous", disabled=(st.session_state.current_page == 1)):
                        st.session_state.current_page -= 1
                        st.rerun()
                with col_p2:
                    st.markdown(f"<div style='text-align: center'>Page {st.session_state.current_page} of {total_pages}</div>", unsafe_allow_html=True)
                with col_p3:
                    if st.button("Next >", disabled=(st.session_state.current_page == total_pages)):
                        st.session_state.current_page += 1
                        st.rerun()
            
            st.markdown("---")
            
            st.markdown("### Action Center")
            col1, col2 = st.columns([1, 2])
            
            with col1:
                selected_lead_id = st.selectbox("Select Lead ID to perform actions", options=df['id'].tolist())
            
            if selected_lead_id:
                lead_details = next((l for l in leads if l['id'] == selected_lead_id), None)
                with col2:
                    st.write(f"**Selected:** {lead_details['name']} @ {lead_details['company']}")
                    
                    statuses = ["New", "Contacted", "Replied", "Demo Scheduled", "Converted", "Dropped"]
                    current_idx = statuses.index(lead_details['status']) if lead_details['status'] in statuses else 0
                    new_status = st.selectbox("Update Status", options=statuses, index=current_idx)
                    if st.button("Save Status"):
                        update_lead(selected_lead_id, {"status": new_status})
                        st.success("Status Updated! Refreshing...")
                        st.rerun()
                        
                    st.markdown("---")
                    
                    if st.button("🤖 AI Score Lead"):
                        with st.spinner("Scoring..."):
                            res = score_lead(selected_lead_id)
                            if res:
                                st.success(f"Score: {res['score']}/10 | Relevant: {res['relevant']}\nReason: {res['reason']}")
                                
                    if st.button("✉️ AI Generate Outreach Messages"):
                        with st.spinner("Drafting..."):
                            res = generate_message(selected_lead_id)
                            if res:
                                st.subheader("Email Draft")
                                st.text_area("Email", value=res.get('email', ''), height=200, key="email_box")
                                st.subheader("LinkedIn Draft")
                                st.text_area("LinkedIn", value=res.get('linkedin', ''), height=100, key="linkedin_box")

    with tab2:
        st.subheader("Manually Add Lead")
        with st.form("add_lead_form"):
            name = st.text_input("Name")
            role = st.text_input("Role")
            company = st.text_input("Company")
            linkedin_url = st.text_input("LinkedIn URL")
            website = st.text_input("Website URL")
            notes = st.text_area("Notes")
            
            submit = st.form_submit_button("Add Lead")
            if submit:
                if name and company:
                    res = create_lead({
                        "name": name,
                        "role": role,
                        "company": company,
                        "linkedin_url": linkedin_url,
                        "website": website,
                        "notes": notes
                    })
                    if res:
                        st.success("Lead added successfully!")
                else:
                    st.error("Name and Company are required.")
