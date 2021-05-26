# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import streamlit as st
import plotly.graph_objects as go
import hiplot as hip

from .streamlit_plots import (
    parallel_categories_plotly,
    parallel_coordinates_plotly,
    scatter_plotly,
    scatter_3d_plotly,
    correlation_heatmap,
)
from .pandas_filters import filter_parameter, add_parameters

plotly_width = 1200
plotly_height = 600


def init_columns(plot_title):
    col1, col2 = st.beta_columns([1, 2])

    return col1, col2


def _select_color_para(search_data, col1, key):
    para_names = list(search_data.columns)
    if "score" in para_names:
        color_index = para_names.index("score")
    else:
        color_index = 0

    color_para = col1.selectbox(
        "Color Parameter",
        para_names,
        index=color_index,
        key=key + "_color",
    )

    return color_para


def correlation_heatmap_seaborn_widget(search_data):
    plot_title = "Correlation Heatmap"
    col1, col2 = init_columns(plot_title)

    search_data_f = add_parameters(search_data, col1, plot_title)
    fig = correlation_heatmap(search_data_f)

    col2.pyplot(fig)


def parallel_coordinates_hiplot_widget(search_data):
    plot_title = "Parallel Corrdinates"
    col1, col2 = init_columns(plot_title)

    search_data_fil = filter_parameter(search_data, col1, plot_title)

    xp = hip.Experiment.from_dataframe(search_data_fil)
    ret_val = xp.display_st(key="key1")


def parallel_coordinates_plotly_widget(search_data):
    plot_title = "Parallel Corrdinates"
    col1, col2 = init_columns(plot_title)

    search_data_fil = filter_parameter(search_data, col1, plot_title)
    color_para = _select_color_para(search_data_fil, col1, plot_title)

    fig = parallel_coordinates_plotly(search_data_fil, color=color_para)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    col2.plotly_chart(fig)


def parallel_categories_plotly_widget(search_data):
    plot_title = "Parallel Categories"
    col1, col2 = init_columns(plot_title)

    search_data_fil = filter_parameter(search_data, col1, plot_title)
    color_para = _select_color_para(search_data_fil, col1, plot_title)

    fig = parallel_categories_plotly(search_data_fil, color=color_para)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    col2.plotly_chart(fig)


def scatter_plotly_widget(search_data):
    plot_title = "Scatter Plot"
    col1, col2 = init_columns(plot_title)

    para_names = search_data.columns

    scatter_para1 = col1.selectbox(
        "1D scatter plot parameter 1",
        para_names,
        index=0,
        key=plot_title + "_para1",
    )
    scatter_para2 = col1.selectbox(
        "2D scatter plot parameter 2",
        para_names,
        index=1,
        key=plot_title + "_para2",
    )
    scatter_para3 = col1.selectbox(
        "2D scatter plot color parameter",
        para_names,
        index=2,
        key=plot_title + "_para3",
    )
    fig = px.scatter(search_data, x=scatter_para1, y=scatter_para2, color=scatter_para3)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    col2.plotly_chart(fig)


def scatter_2d_plotly_widget(search_data):
    plot_title = "2D Scatter Plot"
    col1, col2 = init_columns(plot_title)

    para_names = search_data.columns

    scatter2_para1 = col1.selectbox(
        "2D scatter plot parameter 1",
        para_names,
        index=0,
        key=plot_title + "_para1",
    )
    scatter2_para2 = col1.selectbox(
        "2D scatter plot parameter 2",
        para_names,
        index=1,
        key=plot_title + "_para2",
    )

    color_para = _select_color_para(search_data, col1, plot_title)

    fig = scatter_plotly(
        search_data,
        x=scatter2_para1,
        y=scatter2_para2,
        color=color_para,
    )
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    col2.plotly_chart(fig)


def scatter_3d_plotly_widget(search_data):
    plot_title = "3D Scatter Plot"
    col1, col2 = init_columns(plot_title)

    para_names = search_data.columns

    scatter3_para1 = col1.selectbox(
        "3D scatter plot parameter 1",
        para_names,
        index=0,
        key=plot_title + "_para1",
    )
    scatter3_para2 = col1.selectbox(
        "3D scatter plot parameter 2",
        para_names,
        index=1,
        key=plot_title + "_para2",
    )
    scatter3_para3 = col1.selectbox(
        "3D scatter plot parameter 3",
        para_names,
        index=2,
        key=plot_title + "_para3",
    )

    color_para = _select_color_para(search_data, col1, plot_title)

    fig = scatter_3d_plotly(
        search_data,
        x=scatter3_para1,
        y=scatter3_para2,
        z=scatter3_para3,
        color=color_para,
    )
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    col2.plotly_chart(fig)
