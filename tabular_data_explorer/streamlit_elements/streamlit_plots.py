# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import numpy as np
import hiplot as hip
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt
import seaborn as sns

color_scale = px.colors.sequential.Jet


def table_plotly(search_data, plotly_width=1200, plotly_height=600):
    df_len = len(search_data)

    headerColor = "#b5beff"
    rowEvenColor = "#e8e8e8"
    rowOddColor = "white"

    fig = go.Figure(
        data=[
            go.Table(
                header=dict(
                    values=list(search_data.columns),
                    fill_color=headerColor,
                    align="center",
                ),
                cells=dict(
                    values=[search_data[col] for col in search_data.columns],
                    # fill_color="lavender",
                    fill_color=[
                        [
                            rowOddColor,
                            rowEvenColor,
                        ]
                        * int((df_len / 2) + 1)
                    ],
                    align=["center"],
                    font=dict(size=13),
                ),
            )
        ]
    )
    fig.update_layout(width=plotly_width, height=plotly_height)
    return fig


def parallel_coordinates_hiplot(search_data, plot_title):
    xp = hip.Experiment.from_dataframe(search_data)
    ret_val = xp.display_st(key=plot_title)


def scatter_matrix_plotly(
    search_data, dimensions, color, plotly_width=1200, plotly_height=600
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


def parallel_coordinates_plotly(*args, plotly_width=1200, plotly_height=600, **kwargs):
    fig = px.parallel_coordinates(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def parallel_categories_plotly(*args, plotly_width=1200, plotly_height=600, **kwargs):
    fig = px.parallel_categories(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def scatter_plotly(*args, plotly_width=1200, plotly_height=600, **kwargs):
    fig = px.scatter(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def scatter_3d_plotly(*args, plotly_width=1200, plotly_height=600, **kwargs):
    fig = px.scatter_3d(*args, **kwargs, color_continuous_scale=color_scale)
    fig.update_layout(autosize=False, width=plotly_width, height=plotly_height)

    return fig


def correlation_heatmap(search_data):
    fig, ax = plt.subplots()

    mask = np.triu(np.ones_like(search_data.corr()))
    sns.heatmap(search_data.corr(), cmap="jet", annot=True, square=True, mask=mask)

    return fig
