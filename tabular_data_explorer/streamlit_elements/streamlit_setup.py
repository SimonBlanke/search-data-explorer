# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import streamlit as st

from .streamlit_widgets import (
    scatter_2d_element,
    scatter_3d_element,
    parallel_coordinates_element,
    parallel_categories_element,
    correlation_heatmap_element,
)


plots_select_dict = {
    "2D Scatter Plot": scatter_2d_element,
    "3D Scatter Plot": scatter_3d_element,
    "Parallel Coordinates Plot": parallel_coordinates_element,
    "Parallel Categories Plot": parallel_categories_element,
    "Correlation Heatmap": correlation_heatmap_element,
}


plots_default_dict = {
    "2D-Scatter-Plot": "2D Scatter Plot",
    "3D-Scatter-Plot": "3D Scatter Plot",
    "Parallel-Coordinates-Plot": "Parallel Coordinates Plot",
    "Parallel-Categories-Plot": "Parallel Categories Plot",
    "Correlation-Heatmap": "Correlation Heatmap",
}


def create_streamlit_setup(search_data, plots):
    try:
        st.set_page_config(page_title="Tabular Data Explorer", layout="wide")
    except:
        pass

    plots_default = [plots_default_dict[key] for key in plots]

    st.sidebar.title("Tabular Data Explorer")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")

    plot_names = st.sidebar.multiselect(
        label="Select Plots:",
        options=list(plots_select_dict.keys()),
        default=plots_default,
    )
    for plot_name in plot_names:
        plots_select_dict[plot_name](search_data)