import streamlit as st
import requests
import pandas as pd

st.set_page_config(layout="centered")
st.title("My Profile Webpage")
st.markdown("<h4 style='font-size: 24px;'>Publications</h4>", unsafe_allow_html=True)

orcid_id = "0000-0003-2311-6092"
orcid_api_url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"

headers = {
    "Accept": "application/json"
}

try:
    response = requests.get(orcid_api_url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    works = data.get("group", [])
    
    if works:
        # Prepare data for table
        papers = []
        for work_group in works:
            work_summary = work_group.get("work-summary", [])[0]
            title = work_summary.get("title", {}).get("title", {}).get("value", "No title")
            journal = work_summary.get("journal-title", {}).get("value", "")
            year = work_summary.get("publication-date", {}).get("year", {}).get("value", "")
            url = work_summary.get("url", {}).get("value", f"https://orcid.org/{orcid_id}")
            
            papers.append({
                "Title": f"[{title}]({url})",
                "Journal/Conference": journal,
                "Year": year
            })
        
        # Convert to DataFrame
        df = pd.DataFrame(papers)
        
        # Display with Streamlit (allow HTML links)
        st.markdown(df.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    else:
        st.write("No works found on ORCID.")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data from ORCID: {e}")
