# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import numpy as np
import pandas as pd
import hiplot as hip
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

color_scale = px.colors.sequential.Jet


def plot_hist(*args, **kwargs):
    return px.histogram(*args, **kwargs)


def scatter_plotly(*args, plotly_width=1200, plotly_height=600, **kwargs):
    fig = px.scatter(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def plot_missing_values(df, _st_):
    import plotly.express as px

    color_scale = [
        [0.0, "rgba(0, 255, 0, 0.25)"],
        [0.5, "rgba(0, 255, 0, 0.25)"],
        [0.5, "rgba(255, 0, 0, 0.75)"],
        [1, "rgba(255, 0, 0, 0.75)"],
    ]

    df_miss_o = df.isnull()

    fig = px.imshow(
        df_miss_o,
        color_continuous_scale=color_scale,
    )
    fig.update(layout_coloraxis_showscale=False)
    _st_.plotly_chart(fig)


def plot_duplicate_rows(df, _st_):
    color_scale = [
        [0.0, "rgba(0, 0, 0, 0.25)"],
        [0.5, "rgba(0, 0, 0, 0.25)"],
        [0.5, "rgba(255, 255, 255, 0.75)"],
        [1, "rgba(255, 255, 255, 0.75)"],
    ]
    color_scale = [
        [0.0, "rgba(255, 0, 0, 0.75)"],
        [0.5, "rgba(255, 0, 0, 0.75)"],
        [0.5, "rgba(0, 255, 0, 0.25)"],
        [1, "rgba(0, 255, 0, 0.25)"],
    ]

    dupl = df.duplicated()
    n_col = len(df.columns)

    df_dupl_o = pd.DataFrame([[i] * n_col for i in dupl])
    df_dupl_o.columns = df.columns

    fig = px.imshow(
        df_dupl_o,
        color_continuous_scale=color_scale,
    )
    fig.update(layout_coloraxis_showscale=False)
    _st_.plotly_chart(fig)


def scatter_matrix_plotly(
    search_data, dimensions, color, plotly_width=1100, plotly_height=600
):
    fig = px.scatter_matrix(
        search_data,
        dimensions=dimensions,
        color=color,
        color_continuous_scale=color_scale,
        # symbol="species",
    )  # remove underscore
    fig.update_traces(diagonal_visible=False, showupperhalf=False)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def parallel_coordinates_plotly(*args, plotly_width=1100, plotly_height=600, **kwargs):
    fig = px.parallel_coordinates(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def parallel_categories_plotly(*args, plotly_width=1100, plotly_height=600, **kwargs):
    fig = px.parallel_categories(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def scatter_3d_plotly(*args, plotly_width=1100, plotly_height=600, **kwargs):
    fig = px.scatter_3d(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def correlation_heatmap(search_data):
    fig, ax = plt.subplots()

    mask = np.triu(np.ones_like(search_data.corr()))
    sns.heatmap(search_data.corr(), cmap="jet", annot=True, square=True, mask=mask)

    return fig
