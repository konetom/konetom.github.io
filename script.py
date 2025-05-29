import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="centered")
# st.title("OS Map Viewer")

cpal = pd.read_csv("r_colors.txt", header=None)[0].tolist()
data = pd.read_csv("data.csv")
dim = int(np.sqrt(data.shape[1] - 1))

st.markdown("<h4 style='font-size: 24px;'>Select Survival Percentage Range</h4>", unsafe_allow_html=True)
selected_range = st.slider("", 1, 100, (1, 50), )
sub_df = data[data["pct"].between(*selected_range)].iloc[:, 1:]
if sub_df.empty:
    st.warning(f"No data found between {selected_range[0]}% and {selected_range[1]}%.")
else:
    meta_mean = sub_df.mean()
    meta_map = meta_mean.values.reshape(dim, dim)

    sns.set_context("paper", font_scale=1)
    sns.set_style("white")
    fig, ax = plt.subplots(figsize=(4, 4))
    h = sns.heatmap(meta_map, cmap=cpal, cbar=False, ax=ax)
    h.invert_yaxis()
    h.axis("off")
    st.subheader(f"Heatmap for Survival Range: {selected_range[0]}% – {selected_range[1]}%")
    st.pyplot(fig)
