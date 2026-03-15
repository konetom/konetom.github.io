import streamlit as st
import requests

# --- Page config ---
st.set_page_config(layout="centered")
st.title("My Profile Webpage")
st.markdown("<h4 style='font-size: 24px;'>Publications</h4>", unsafe_allow_html=True)

# --- Add hover effect CSS ---
st.markdown(
    """
    <style>
    .paper-card {
        border: 1px solid #ddd;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
        background-color: #f9f9f9;
        transition: transform 0.2s, box-shadow 0.2s, background-color 0.2s;
    }
    .paper-card:hover {
        transform: translateY(-4px);
        box-shadow: 0 4px 12px rgba(0,0,0,0.15);
        background-color: #f1f5f9;
    }
    .paper-card h4 {
        margin: 0;
    }
    .paper-card p {
        margin: 4px 0 0 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- ORCID ID ---
orcid_id = "0000-0003-2311-6092"
orcid_api_url = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
headers = {"Accept": "application/json"}

try:
    response = requests.get(orcid_api_url, headers=headers)
    response.raise_for_status()
    data = response.json()
    
    works = data.get("group", [])
    
    if works:
        col1, col2 = st.columns(2)
        for i, work_group in enumerate(works):
            work_summary = work_group.get("work-summary", [])[0]
            title = work_summary.get("title", {}).get("title", {}).get("value", "No title")
            journal = work_summary.get("journal-title", {}).get("value", "")
            year = work_summary.get("publication-date", {}).get("year", {}).get("value", "")
            url = work_summary.get("url", {}).get("value", f"https://orcid.org/{orcid_id}")
            
            col = col1 if i % 2 == 0 else col2
            
            col.markdown(
                f"""
                <div class="paper-card">
                    <h4><a href="{url}" target="_blank">{title}</a></h4>
                    <p style='font-style:italic;'>{journal}</p>
                    <p style='color:#555;'>Year: {year}</p>
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.write("No works found on ORCID.")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data from ORCID: {e}")
