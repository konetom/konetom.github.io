import streamlit as st
import requests
import re

# --- Function to clean HTML tags from ORCID text ---
def clean_html(text):
    if not text:
        return ""
    # Remove any HTML/XML tags
    text = re.sub(r"<[^>]+>", "", text)
    # Remove weird artifacts or excessive whitespace
    return text.strip()

# --- Page config ---
st.set_page_config(layout="centered")
st.title("My Profile Webpage")
st.markdown("<h4 style='font-size: 22px;'>Publications</h4>", unsafe_allow_html=True)

# --- CSS for compact single-column cards ---
st.markdown(
    """
    <style>
    .paper-card {
        border: 1px solid #ccc;
        border-radius: 6px;
        padding: 12px;
        margin-bottom: 12px;
        background-color: #fafafa;
        transition: transform 0.2s, box-shadow 0.2s;
        font-size: 13px;
        line-height: 1.25;
    }
    .paper-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 3px 10px rgba(0,0,0,0.12);
        background-color: #f1f5f9;
    }
    .paper-title {
        font-size: 14px;
        font-weight: 600;
        margin-bottom: 4px;
    }
    .paper-meta {
        font-size: 12px;
        color: #555;
        margin-bottom: 4px;
    }
    .paper-summary {
        font-size: 12px;
        color: #444;
        margin-top: 6px;
        white-space: pre-wrap;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- ORCID settings ---
orcid_id = "0000-0003-2311-6092"
api_works = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
api_work_detail = f"https://pub.orcid.org/v3.0/{orcid_id}/work/"
headers = {"Accept": "application/json"}

# --- Fetch works ---
try:
    resp = requests.get(api_works, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    works = data.get("group", [])

    if works:
        for group in works:
            summary = group.get("work-summary", [])[0]
            put_code = summary.get("put-code")

            title = summary.get("title", {}).get("title", {}).get("value", "No title")
            journal = summary.get("journal-title", {}).get("value", "")
            year = summary.get("publication-date", {}).get("year", {}).get("value", "")
            url = summary.get("url", {}).get("value", f"https://orcid.org/{orcid_id}")

            # Fetch full work description
            description = ""
            if put_code:
                detail_url = api_work_detail + str(put_code)
                d = requests.get(detail_url, headers=headers)
                if d.status_code == 200:
                    j = d.json()
                    description = (
                        j.get("short-description", "") 
                        or j.get("work-description", "") 
                    )

            # --- CLEAN DESCRIPTION SAFELY ---
            description = clean_html(description)
            if len(description) > 500:
                description = description[:500] + "..."

            # --- CARD RENDER ---
            st.markdown(
                f"""
                <div class="paper-card">
                    <div class="paper-title">
                        <a href="{url}" target="_blank">{title}</a>
                    </div>
                    <div class="paper-meta">{journal}<br>{year}</div>
                    <div class="paper-summary">{description}</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:
        st.write("No works found.")

except Exception as e:
    st.error(f"Error fetching ORCID data: {e}")
