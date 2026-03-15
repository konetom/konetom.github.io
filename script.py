import streamlit as st
import requests

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
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# --- ORCID ID ---
orcid_id = "0000-0003-2311-6092"
orcid_api_works = f"https://pub.orcid.org/v3.0/{orcid_id}/works"
orcid_api_work_details = f"https://pub.orcid.org/v3.0/{orcid_id}/work/"

headers = {"Accept": "application/json"}

# --- Fetch works ---
try:
    resp = requests.get(orcid_api_works, headers=headers)
    resp.raise_for_status()
    data = resp.json()
    works = data.get("group", [])

    if works:
        for work_group in works:
            work_summary = work_group.get("work-summary", [])[0]
            put_code = work_summary.get("put-code")

            title = work_summary.get("title", {}).get("title", {}).get("value", "No title")
            journal = work_summary.get("journal-title", {}).get("value", "")
            year = work_summary.get("publication-date", {}).get("year", {}).get("value", "")

            # URL fallback
            url = work_summary.get("url", {}).get("value", f"https://orcid.org/{orcid_id}")

            # --- Fetch full work description ---
            description = ""
            if put_code:
                detail_url = orcid_api_work_details + str(put_code)
                r_detail = requests.get(detail_url, headers=headers)
                if r_detail.status_code == 200:
                    detail_json = r_detail.json()
                    description = detail_json.get("short-description", "") or \
                                  detail_json.get("work-description", "")

            # --- Render card (1 column only) ---
            st.markdown(
                f"""
                <div class="paper-card">
                    <div class="paper-title">
                        <a href="{url}" target="_blank">{title}</a>
                    </div>
                    <div class="paper-meta">
                        {journal}<br>
                        {year}
                    </div>
                    <div class="paper-summary">
                        {description[:500]}{'...' if len(description) > 500 else ''}
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:
        st.write("No works found on ORCID.")

except requests.exceptions.RequestException as e:
    st.error(f"Error fetching data from ORCID: {e}")
