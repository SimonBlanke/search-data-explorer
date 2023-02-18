# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import streamlit as st
import numpy as np

from .elements import statistics, create_plotly_chart
from .plots import (
    scatter_plotly,
    plot_hist,
    scatter_3d_plotly,
    parallel_coordinates_plotly,
    parallel_categories_plotly,
    scatter_matrix_plotly,
)


def select_parameter(parameter_l, name, _st_, index=0):
    _name_ = "select_parameter"
    return _st_.selectbox(
        name,
        parameter_l,
        index=index,
        # key=random_key(_name_),
    )


def select_column(search_data, _st_):
    _name_ = "select_column"

    para_names = list(search_data.columns)
    para_names_f = _st_.multiselect(
        label="Parameters:",
        options=para_names,
        # key=random_key(_name_),
    )
    return para_names_f


class Filter:
    def __init__(self, search_data):
        self.search_data = search_data
        self.col_names = list(search_data.columns)
        self.para_names = [n for n in self.col_names if n != "score"]
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

    def filter_parameter(self, _st_, para_names=None):
        _name_ = "filter_parameter"

        if para_names is None:
            para_names = self.col_names

        para_names_fil = _st_.multiselect(
            label="Filter Parameters:",
            options=para_names,
        )

        search_data = self.search_data.copy()
        for para_name in para_names_fil:
            para_data = search_data[para_name].values

            if self.data_types[para_name] == "categorical":
                cat_values = np.unique(para_data)
                cat_values_fil = _st_.multiselect(
                    label="Filter Parameters:",
                    options=cat_values,
                    default=cat_values,
                )

                search_data = search_data[search_data[para_name].isin(cat_values_fil)]

            else:
                min_ = float(np.min(para_data))
                max_ = float(np.max(para_data))
                step = (max_ - min_) / 100

                if step == 0:
                    continue

                (lower, upper) = _st_.slider(
                    "Filter: " + str(para_name),
                    min_value=min_,
                    max_value=max_,
                    value=(min_, max_),
                    step=step,
                    format="%.5f",
                )
                _st_.text("")

                search_data = search_data[
                    (search_data[para_name] >= lower)
                    & (search_data[para_name] <= upper)
                ]

        return search_data


def score_idx(para_names):
    return para_names.index("score")


def create_title(title):
    def decorator(widget):
        def wrapper(*args, **kwargs):
            st.title(title)
            st.components.v1.html(
                """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
                height=10,
            )
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

        col1.markdown("---")

        search_data_f = self.filter.filter_parameter(col1)
        plotly_kwargs = {
            "data_frame": search_data_f,
            "x": scatter2_para1,
            "y": scatter2_para2,
            "color": color_para,
        }

        create_plotly_chart(col2, scatter_plotly, plotly_kwargs)

    @create_title("3D Scatter Plot")
    def scatter_3d_plotly_widget(self):
        col1, col2 = st.columns([1, 2])

        select_para_d_1 = {
            "parameter_l": self.col_names,
            "name": "3D scatter plot parameter 1",
            "_st_": col1,
            "index": 0,
        }
        select_para_d_2 = {
            "parameter_l": self.col_names,
            "name": "3D scatter plot parameter 2",
            "_st_": col1,
            "index": 1,
        }
        select_para_d_3 = {
            "parameter_l": self.col_names,
            "name": "3D scatter plot parameter 3",
            "_st_": col1,
            "index": 2,
        }
        select_para_d_4 = {
            "parameter_l": self.col_names,
            "name": "Color Parameter",
            "_st_": col1,
            "index": score_idx(self.col_names),
        }

        scatter3_para1 = select_parameter(**select_para_d_1)
        scatter3_para2 = select_parameter(**select_para_d_2)
        scatter3_para3 = select_parameter(**select_para_d_3)
        color_para = select_parameter(**select_para_d_4)

        col1.markdown("---")

        search_data_f = self.filter.filter_parameter(col1)
        plotly_kwargs = {
            "data_frame": search_data_f,
            "x": scatter3_para1,
            "y": scatter3_para2,
            "z": scatter3_para3,
            "color": color_para,
        }

        create_plotly_chart(col2, scatter_3d_plotly, plotly_kwargs)

    @create_title("Scatter Matrix")
    def scatter_matrix_plotly_widget(self):
        col1, col2 = st.columns([1, 2])

        para_names_f = self.add_parameters_num(col1, "scatter_matrix_plotly_widget")
        color_para = self.select_color_para_cat(col1)

        plotly_kwargs = {
            "search_data": self.search_data,
            "dimensions": para_names_f,
            "color": color_para,
        }
        create_plotly_chart(col2, scatter_matrix_plotly, plotly_kwargs)

    @create_title("Parallel Corrdinates")
    def parallel_coordinates_plotly_widget(self):
        col1, col2 = st.columns([1, 2])

        para_names_f = self.add_parameters_num(
            col1, "parallel_coordinates_plotly_widget"
        )

        if "score" not in para_names_f:
            para_names_f_s = para_names_f + ["score"]
        else:
            para_names_f_s = para_names_f

        search_data_f = self.filter.filter_parameter(col1, para_names=para_names_f_s)
        color_para = self.select_color_para_num(
            col1, "parallel_coordinates_plotly_widget"
        )

        plotly_kwargs = {
            "data_frame": search_data_f,
            "dimensions": para_names_f,
            "color": color_para,
        }
        create_plotly_chart(col2, parallel_coordinates_plotly, plotly_kwargs)

    @create_title("Parallel Categories")
    def parallel_categories_plotly_widget(self):
        col1, col2 = st.columns([1, 2])

        para_names_f = self.add_parameters_num(
            col1, "parallel_categories_plotly_widget"
        )
        search_data_f = self.filter.filter_parameter(col1)

        color_para = self.select_color_para_num(
            col1, "parallel_categories_plotly_widget"
        )

        plotly_kwargs = {
            "data_frame": search_data_f,
            "dimensions": para_names_f,
            "color": color_para,
        }
        create_plotly_chart(col2, parallel_categories_plotly, plotly_kwargs)

    def add_parameters_num(self, _st_, key):
        para_names_f = _st_.multiselect(
            label="Parameters:",
            options=self.col_names,
            default=[n for n in self.num_para_names if n != "score"],
            key=key + " add_parameters_num",
        )
        return para_names_f

    def select_color_para_cat(self, col1):
        # print("categorical", categorical)
        if "score" in self.col_names:
            color_index = self.col_names.index("score")
        elif len(self.cat_para_names) != 0:
            color_index = self.col_names.index(self.cat_para_names[0])
        else:
            color_index = 0

        color_para = col1.selectbox(
            "Color Parameter",
            self.col_names,
            index=color_index,
        )

        return color_para

    def select_color_para_num(self, col1, key):
        if "score" in self.col_names:
            color_index = self.col_names.index("score")
        elif len(self.num_para_names) != 0:
            color_index = self.col_names.index(self.num_para_names[0])
        else:
            color_index = 0

        color_para = col1.selectbox(
            "Color Parameter",
            self.col_names,
            index=color_index,
            key=key + " select_color_para_num",
        )

        return color_para
