# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import streamlit as st


def create_sidebar(elements_dict):
    scatter_plots = st.sidebar.multiselect(
        label="Scatter Plots",
        options=list(elements_dict.keys()),
        default=["Parallel Coordinates Plot"],
    )

    return scatter_plots
