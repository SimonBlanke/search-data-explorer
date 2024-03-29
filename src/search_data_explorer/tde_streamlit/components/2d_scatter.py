# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import streamlit as st
import numpy as np

from .elements import create_plotly_chart
from .plots import (
    scatter_plotly,
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

    @create_title("2D Scatter Plot")
    def scatter_2d_plotly_widget(self):
        col1, col2 = st.columns([1, 2])

        select_para_d_1 = {
            "parameter_l": self.col_names,
            "name": "2D scatter plot parameter 1",
            "_st_": col1,
            "index": 0,
        }
        select_para_d_2 = {
            "parameter_l": self.col_names,
            "name": "2D scatter plot parameter 2",
            "_st_": col1,
            "index": 1,
        }
        select_para_d_3 = {
            "parameter_l": self.col_names,
            "name": "Color Parameter",
            "_st_": col1,
            "index": score_idx(self.col_names),
        }

        scatter2_para1 = select_parameter(**select_para_d_1)
        scatter2_para2 = select_parameter(**select_para_d_2)
        color_para = select_parameter(**select_para_d_3)

        col1.divider()

        set_parameters = [
            item
            for item in self.col_names
            if item not in [scatter2_para1, scatter2_para2, color_para]
        ]

        search_data = self.search_data.copy()

        for set_parameter in set_parameters:
            para_data = search_data[set_parameter].values
            cat_values = np.unique(para_data)
            cat_value = col1.selectbox("Set " + set_parameter, cat_values)
            search_data = search_data[search_data[set_parameter] == cat_value]

        col1.divider()

        search_data_f = self.filter.filter_parameter(col1, search_data)
        plotly_kwargs = {
            "data_frame": search_data_f,
            "x": scatter2_para1,
            "y": scatter2_para2,
            "color": color_para,
        }

        create_plotly_chart(col2, scatter_plotly, plotly_kwargs)
