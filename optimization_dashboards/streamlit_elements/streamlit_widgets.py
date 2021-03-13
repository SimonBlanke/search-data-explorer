# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px
import plotly.graph_objects as go


from .streamlit_plots import parallel_coordinates, scatter_2d, scatter_3d
from .pandas_filters import filter_parameter


def _select_color_para(search_data, col1):
    para_names = list(search_data.columns)
    if "score" in para_names:
        color_index = para_names.index("score")
    else:
        color_index = 0

    color_para = col1.selectbox(
        "Color Parameter",
        para_names,
        index=color_index,
    )

    return color_para


def parallel_coordinates_element(search_data):
    st.text("")
    col1, col2 = st.beta_columns(2)

    col1.header("Parallel Corrdinates")
    col1.text("")
    col2.text("")

    search_data_fil = filter_parameter(search_data, col1)
    color_para = _select_color_para(search_data_fil, col1)

    fig = parallel_coordinates(search_data_fil, color=color_para)

    col2.plotly_chart(fig)


def scatter_2d_element(search_data):
    para_names = search_data.columns.drop("score")

    st.text("")
    col1, col2 = st.beta_columns(2)

    col1.header("2D Scatter plot")
    col1.text("")

    scatter2_para1 = col1.selectbox(
        "2D scatter plot parameter 1",
        para_names,
        index=0,
    )
    scatter2_para2 = col1.selectbox(
        "2D scatter plot parameter 2",
        para_names,
        index=1,
    )

    fig = scatter_2d(
        search_data,
        x=scatter2_para1,
        y=scatter2_para2,
        color="score",
    )
    col2.plotly_chart(fig)


def scatter_3d_element(search_data):
    para_names = search_data.columns.drop("score")

    st.text("")
    col1, col2 = st.beta_columns(2)

    col1.header("3D Scatter plot")
    col1.text("")

    scatter3_para1 = col1.selectbox(
        "3D scatter plot parameter 1",
        para_names,
        index=0,
    )
    scatter3_para2 = col1.selectbox(
        "3D scatter plot parameter 2",
        para_names,
        index=1,
    )
    scatter3_para3 = col1.selectbox(
        "3D scatter plot parameter 3",
        para_names,
        index=2,
    )

    fig = scatter_3d(
        search_data,
        x=scatter3_para1,
        y=scatter3_para2,
        z=scatter3_para3,
        color="score",
    )
    col2.plotly_chart(fig)


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


def _1d_scatter(search_data):
    from sklearn.gaussian_process import GaussianProcessRegressor

    para_names = search_data.columns.drop("score")

    st.text("")
    col1, col2 = st.beta_columns(2)

    col1.header("1D Scatter plot")
    col1.text("")

    scatter1_para1 = col1.selectbox(
        "1D scatter plot parameter 1",
        para_names,
        index=0,
    )

    fig1 = px.scatter(
        search_data, x=scatter1_para1, y=search_data["score"]
    ).update_layout(width=1000, height=600)

    x_train_1D = search_data[scatter1_para1].values.reshape(-1, 1)

    gpr = GaussianProcessRegressor()
    gpr.fit(x_train_1D, search_data["score"])

    print("\n x_train_1D \n", x_train_1D)

    min_ = -10
    max_ = 10
    step = 0.1

    x_plot = np.arange(min_, max_, step).reshape(-1, 1)

    mu, sigma = gpr.predict(x_plot, return_std=True)
    mu = mu.reshape(-1, 1)
    sigma = sigma.reshape(-1, 1)

    line_df = {
        "x": x_plot.reshape(
            -1,
        ),
        "bayes fit": mu.reshape(
            -1,
        ),
    }

    y_upper = mu + sigma
    y_lower = mu - sigma

    fig2 = px.line(line_df, x="x", y="bayes fit")

    fig3 = go.Figure(data=fig1.data + fig2.data)

    col2.plotly_chart(fig3)


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