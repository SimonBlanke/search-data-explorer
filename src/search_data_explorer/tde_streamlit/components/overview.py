# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import streamlit as st
import numpy as np

from .elements import statistics, create_plotly_chart
from .plots import (
    plot_hist,
)


def score_idx(para_names):
    return para_names.index("score")


def create_title(title):
    def decorator(widget):
        def wrapper(*args, **kwargs):
            st.title(title)
            st.divider()
            st.text("")
            result = widget(*args, **kwargs)
            return result

        wrapper.__name__ = widget.__name__

        return wrapper

    return decorator


class Widgets:
    def __init__(self, search_data):
        self.search_data = search_data
        self.col_names = list(search_data.columns)
        self.para_names = [n for n in self.col_names if n != "score"]

        self.filter = Filter(search_data)

        self.plots_select_dict = {
            "Overview": self.table_overview_widget,
            "2D Scatter": self.scatter_2d_plotly_widget,
            "3D Scatter": self.scatter_3d_plotly_widget,
            "Parallel Coordinates": self.parallel_coordinates_plotly_widget,
            "Parallel Categories": self.parallel_categories_plotly_widget,
            "Scatter Matrix": self.scatter_matrix_plotly_widget,
        }

        self.get_data_types()

    def get_data_types(self):
        data_types = {}
        cat_para_names = []
        num_para_names = []

        for para_name in self.col_names:
            values = self.search_data[para_name].values

            try:
                values * values
                values - values
            except:
                data_types[para_name] = "categorical"
                cat_para_names.append(para_name)

            else:
                data_types[para_name] = "numeric"
                num_para_names.append(para_name)

        # print("\n data_types \n", data_types, "\n")
        self.data_types = data_types
        self.cat_para_names = cat_para_names
        self.num_para_names = num_para_names

    @create_title("Overview")
    def table_overview_widget(self):
        st.subheader("Search data samples")
        sd_sample = self.search_data.sample(n=10, random_state=1)

        st.table(sd_sample)

        col1, col2 = st.columns([1, 1])

        statistics_df = statistics(self.search_data)

        col1.subheader("Search data statistics")
        col1.table(statistics_df)

        plotly_kwargs = {
            "data_frame": self.search_data,
            "x": "score",
            "hover_data": self.col_names,
        }

        create_plotly_chart(col2, plot_hist, plotly_kwargs)
