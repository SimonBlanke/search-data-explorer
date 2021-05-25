# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

color_scale = px.colors.sequential.Jet


def parallel_coordinates_plotly(*args, **kwargs):
    return px.parallel_coordinates(*args, **kwargs, color_continuous_scale=color_scale)


def parallel_categories_plotly(*args, **kwargs):
    return px.parallel_categories(*args, **kwargs, color_continuous_scale=color_scale)


def scatter_plotly(*args, **kwargs):
    return px.scatter(*args, **kwargs, color_continuous_scale=color_scale)


def scatter_3d_plotly(*args, **kwargs):
    return px.scatter_3d(*args, **kwargs, color_continuous_scale=color_scale)


def correlation_heatmap(search_data):
    fig, ax = plt.subplots()
    corr = search_data.corr()
    sns.heatmap(
        round(corr, 2), annot=True, ax=ax, cmap="coolwarm", fmt=".2f", linewidths=0.05
    )

    return fig
