# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import streamlit as st

from .streamlit_widgets import (
    scatter_1d_element,
    scatter_2d_element,
    scatter_3d_element,
    parallel_coordinates_element,
    parallel_categories_element,
)


plots_dict = {
    "1D Scatter Plot": scatter_1d_element,
    "2D Scatter Plot": scatter_2d_element,
    "3D Scatter Plot": scatter_3d_element,
    "Parallel Coordinates Plot": parallel_coordinates_element,
    "Parallel Categories Plot": parallel_categories_element,
}


def create_streamlit_setup(search_data, default_plots=["1D Scatter Plot"]):
    try:
        st.set_page_config(page_title="Tabular Data Explorer", layout="wide")
    except:
        pass

    st.sidebar.title("Tabular Data Explorer")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")

    plot_names = st.sidebar.multiselect(
        label="Select Plots:",
        options=list(plots_dict.keys()),
        default=default_plots,
    )
    for plot_name in plot_names:
        plots_dict[plot_name](search_data)