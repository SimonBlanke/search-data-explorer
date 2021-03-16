# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import streamlit as st

from .streamlit_sidebar import create_sidebar
from .streamlit_widgets import (
    scatter_1d_element,
    scatter_2d_element,
    scatter_3d_element,
    parallel_coordinates_element,
    parallel_categories_element,
)


def create_streamlit_setup(search_data):
    elements_dict = {
        "1D Scatter Plot": scatter_1d_element,
        "2D Scatter Plot": scatter_2d_element,
        "3D Scatter Plot": scatter_3d_element,
        "Parallel Coordinates Plot": parallel_coordinates_element,
        "Parallel Categories Plot": parallel_categories_element,
    }

    st.set_page_config(page_title="Hyperactive Dashboard", layout="wide")

    st.sidebar.title("Optimization Plotter")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")

    plot_names = create_sidebar(elements_dict)

    for plot_name in plot_names:
        elements_dict[plot_name](search_data)
