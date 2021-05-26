# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

color_scale = px.colors.sequential.Jet

plotly_width = 1200
plotly_height = 600


def scatter_matrix_plotly(search_data, color):
    fig = px.scatter_matrix(
        search_data,
        # dimensions=["sepal_width", "sepal_length", "petal_width", "petal_length"],
        color=color,
        color_continuous_scale=color_scale,
        # symbol="species",
    )  # remove underscore
    fig.update_traces(diagonal_visible=False, showupperhalf=False)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def parallel_coordinates_plotly(*args, **kwargs):
    fig = px.parallel_coordinates(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def parallel_categories_plotly(*args, **kwargs):
    fig = px.parallel_categories(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def scatter_plotly(*args, **kwargs):
    fig = px.scatter(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def scatter_3d_plotly(*args, **kwargs):
    fig = px.scatter_3d(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def correlation_heatmap(search_data):
    fig, ax = plt.subplots()
    corr = search_data.corr()
    sns.heatmap(
        round(corr, 2), annot=True, ax=ax, cmap="coolwarm", fmt=".2f", linewidths=0.05
    )

    return fig
