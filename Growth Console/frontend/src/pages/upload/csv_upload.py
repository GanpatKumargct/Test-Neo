import streamlit as st
import pandas as pd
from services.lead_api import create_lead

def render_csv_upload():
    st.title("📂 Upload Leads via CSV")
    st.markdown("Upload a CSV file to bulk import leads into the TestNeo Growth Console.")
    
    st.info("Expected Columns: `name`, `role`, `company`, `linkedin_url`, `website`, `notes`")
    
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    
    if uploaded_file is not None:
        try:
            df = pd.read_csv(uploaded_file)
            
            # Handle cases where CSV export adds fake headers (e.g., Column1, Column2)
            if 'name' not in [str(c).lower() for c in df.columns]:
                for idx, row in df.iterrows():
                    if 'name' in [str(val).lower().strip() for val in row.values if pd.notna(val)]:
                        df.columns = [str(val).lower().strip() if pd.notna(val) else f"col_{i}" for i, val in enumerate(row.values)]
                        df = df.iloc[idx+1:].reset_index(drop=True)
                        break
            else:
                df.columns = [str(c).lower().strip() for c in df.columns]
                
            st.subheader("Data Preview")
            st.dataframe(df.head())
            
            if st.button("Import Leads"):
                progress_bar = st.progress(0)
                status_text = st.empty()
                
                success_count = 0
                error_count = 0
                
                for index, row in df.iterrows():
                    lead_data = {
                        "name": str(row.get('name', '')),
                        "role": str(row.get('role', '')) if pd.notna(row.get('role')) else "",
                        "company": str(row.get('company', '')),
                        "linkedin_url": str(row.get('linkedin_url', '')) if pd.notna(row.get('linkedin_url')) else "",
                        "website": str(row.get('website', '')) if pd.notna(row.get('website')) else "",
                        "notes": str(row.get('notes', '')) if pd.notna(row.get('notes')) else ""
                    }
                    
                    if not lead_data["name"] or not lead_data["company"]:
                        error_count += 1
                        continue
                        
                    res = create_lead(lead_data)
                    if res:
                        success_count += 1
                    else:
                        error_count += 1
                        
                    progress_bar.progress((index + 1) / len(df))
                    status_text.text(f"Processed {index + 1} / {len(df)} leads")
                    
                st.success(f"Import complete! {success_count} added, {error_count} failed/skipped.")
                
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
