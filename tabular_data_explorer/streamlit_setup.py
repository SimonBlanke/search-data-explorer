# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import streamlit as st

from toc import Toc
from streamlit_elements.streamlit_widgets import (
    scatter_2d_plotly_widget,
    scatter_3d_plotly_widget,
    parallel_coordinates_plotly_widget,
    parallel_categories_plotly_widget,
    parallel_coordinates_hiplot_widget,
    correlation_heatmap_seaborn_widget,
    scatter_matrix_plotly_widget,
)


plots_select_dict = {
    "2D Scatter (Plotly)": scatter_2d_plotly_widget,
    "3D Scatter (Plotly)": scatter_3d_plotly_widget,
    "Parallel Coordinates (Plotly)": parallel_coordinates_plotly_widget,
    "Parallel Categories (Plotly)": parallel_categories_plotly_widget,
    "Parallel Categories (HiPlot)": parallel_coordinates_hiplot_widget,
    "Correlation Heatmap (Seaborn)": correlation_heatmap_seaborn_widget,
    "Scatter Matrix (Plotly)": scatter_matrix_plotly_widget,
}


plots_default_dict = {
    "2D-Scatter-Plotly": "2D Scatter (Plotly)",
    "3D-Scatter-Plotly": "3D Scatter (Plotly)",
    "Parallel-Coordinates-Plotly": "Parallel Coordinates (Plotly)",
    "Parallel-Categories-Plotly": "Parallel Categories (Plotly)",
    "Parallel-Categories-HiPlot": "Parallel Categories (HiPlot)",
    "Correlation-Heatmap-Seaborn": "Correlation Heatmap (Seaborn)",
    "Scatter-Matrix-Plotly": "Scatter Matrix (Plotly)",
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

    toc = Toc()
    toc.placeholder(sidebar=True)

    for plot_name in plot_names:
        toc.title(plot_name)
        st.components.v1.html(
            """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """
        )
        plots_select_dict[plot_name](search_data)
        for _ in range(5):
            st.write(" ")

    toc.generate()
