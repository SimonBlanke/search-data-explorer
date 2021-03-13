# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import plotly.express as px


def parallel_coordinates(*args, **kwargs):
    return px.parallel_coordinates(*args, **kwargs)


def scatter_2d(*args, **kwargs):
    return px.scatter(*args, **kwargs)


def scatter_3d(*args, **kwargs):
    return px.scatter_3d(*args, **kwargs)
