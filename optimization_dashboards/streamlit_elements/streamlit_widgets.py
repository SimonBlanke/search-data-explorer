# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


from .streamlit_plots import (
    parallel_coordinates_plotly,
    scatter_plotly,
    scatter_3d_plotly,
)
from .pandas_filters import filter_parameter


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


def parallel_coordinates_element(search_data):
    func_name = str(parallel_coordinates_element.__name__)
    st.text("")
    col1, col2 = st.beta_columns(2)

    col1.header("Parallel Corrdinates")
    col1.text("")
    col2.text("")

    search_data_fil = filter_parameter(search_data, col1, func_name)
    color_para = _select_color_para(search_data_fil, col1, func_name)

    fig = parallel_coordinates_plotly(search_data_fil, color=color_para)

    col2.plotly_chart(fig)


def scatter_1d_element(search_data):
    func_name = str(scatter_1d_element.__name__)

    para_names = search_data.columns

    st.text("")
    col1, col2 = st.beta_columns(2)

    col1.header("1D Scatter Plot")
    col1.text("")

    scatter1_para1 = col1.selectbox(
        "1D scatter plot parameter 1",
        para_names,
        index=0,
        key=func_name + "_para1",
    )
    scatter2_para2 = col1.selectbox(
        "2D scatter plot parameter 2",
        para_names,
        index=1,
        key=func_name + "_para2",
    )

    fig = px.scatter(search_data, x=scatter1_para1, y=scatter2_para2)

    col2.plotly_chart(fig)


def scatter_2d_element(search_data):
    func_name = str(scatter_2d_element.__name__)

    para_names = search_data.columns

    st.text("")
    col1, col2 = st.beta_columns(2)

    col1.header("2D Scatter Plot")
    col1.text("")

    scatter2_para1 = col1.selectbox(
        "2D scatter plot parameter 1",
        para_names,
        index=0,
        key=func_name + "_para1",
    )
    scatter2_para2 = col1.selectbox(
        "2D scatter plot parameter 2",
        para_names,
        index=1,
        key=func_name + "_para2",
    )

    color_para = _select_color_para(search_data, col1, func_name)

    fig = scatter_plotly(
        search_data,
        x=scatter2_para1,
        y=scatter2_para2,
        color=color_para,
    )
    col2.plotly_chart(fig)


def scatter_3d_element(search_data):
    func_name = str(scatter_3d_element.__name__)

    para_names = search_data.columns

    st.text("")
    col1, col2 = st.beta_columns(2)

    col1.header("3D Scatter Plot")
    col1.text("")

    scatter3_para1 = col1.selectbox(
        "3D scatter plot parameter 1",
        para_names,
        index=0,
        key=func_name + "_para1",
    )
    scatter3_para2 = col1.selectbox(
        "3D scatter plot parameter 2",
        para_names,
        index=1,
        key=func_name + "_para2",
    )
    scatter3_para3 = col1.selectbox(
        "3D scatter plot parameter 3",
        para_names,
        index=2,
        key=func_name + "_para3",
    )

    color_para = _select_color_para(search_data, col1, func_name)

    fig = scatter_3d_plotly(
        search_data,
        x=scatter3_para1,
        y=scatter3_para2,
        z=scatter3_para3,
        color=color_para,
    )
    col2.plotly_chart(fig)


"""
def _score_statistics(search_data):
    values_ = search_data["score"].values

    mean_ = values_.mean()
    std_ = values_.std()
    min_ = np.amin(values_)
    max_ = np.amax(values_)

    df_data = pd.DataFrame(
        [[mean_, std_, min_, max_]],
        index=["score"],
        columns=["mean", "std", "min", "max"],
    )

    col1, col2 = st.beta_columns(2)

    col1.header("Score statistics")
    col1.text("")
    col2.text("")

    col1.table(df_data)

    def _score_statistics_plot(search_data):
        fig = px.histogram(
            search_data, x="score", nbins=int(len(search_data))
        ).update_layout(width=1000, height=300)
        col2.plotly_chart(fig)

    _score_statistics_plot(search_data)


def _search_data(search_data):
    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(search_data.columns),
                    # fill_color="paleturquoise",
                    align="left",
                ),
                cells=dict(
                    values=search_data.transpose().values.tolist(),
                    # fill_color="lavender",
                    align="left",
                ),
            ),
        ]
    )

    st.plotly_chart(fig)
"""
