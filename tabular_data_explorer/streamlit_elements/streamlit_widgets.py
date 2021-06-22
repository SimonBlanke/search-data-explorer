# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import streamlit as st

from .streamlit_plots import (
    parallel_categories_plotly,
    parallel_coordinates_plotly,
    parallel_coordinates_hiplot,
    scatter_plotly,
    scatter_3d_plotly,
    correlation_heatmap,
    scatter_matrix_plotly,
    table_plotly,
)
from .pandas_filters import (
    filter_parameter,
    add_parameters_num,
    select_color_para_cat,
    select_color_para_num,
)


def table_overview_widget(search_data):
    col1, col2 = st.beta_columns([1, 1])

    col1.header("First 10 rows")
    col1.dataframe(search_data.head(10))
    col2.header("Last 10 rows")
    col2.dataframe(search_data.tail(10))


def table_plotly_widget(search_data):
    plot_title = "Table"
    col1, col2 = st.beta_columns([1, 2])

    search_data_f = filter_parameter(
        search_data,
        search_data.columns,
        col1,
        plot_title,
    )

    window_size = 10
    search_data_len = len(search_data_f)
    n_pages = max(int(search_data_len / window_size) - 1, 1)

    nth_page = col1.select_slider(
        "Page: ",
        options=list(range(n_pages + 1)),
        value=0,
    )

    # nth_page = col1.radio("Page: ", options=list(range(n_pages)))

    search_data_f = search_data_f[window_size * nth_page : window_size * (nth_page + 1)]

    # fig = table_plotly(search_data_f)
    # col2.plotly_chart(fig)

    col2.dataframe(search_data_f)


def scatter_matrix_plotly_widget(search_data):
    plot_title = "Scatter Matrix"
    col1, col2 = st.beta_columns([1, 2])

    para_names_f = add_parameters_num(search_data, col1, plot_title)
    color_para = select_color_para_cat(search_data, col1, plot_title)

    fig = scatter_matrix_plotly(search_data, dimensions=para_names_f, color=color_para)
    col2.plotly_chart(fig)


def correlation_heatmap_seaborn_widget(search_data):
    plot_title = "Correlation Heatmap"
    col1, col2 = st.beta_columns([1, 2])

    para_names_f = add_parameters_num(search_data, col1, plot_title)
    fig = correlation_heatmap(search_data[para_names_f])

    col2.pyplot(fig)


def parallel_coordinates_hiplot_widget(search_data):
    plot_title = "Parallel Corrdinates"
    col1, col2 = st.beta_columns([1, 2])

    para_names_f = add_parameters_num(search_data, col1, plot_title)
    search_data_f = filter_parameter(search_data, para_names_f, col1, plot_title)

    parallel_coordinates_hiplot(search_data_f, plot_title)


def parallel_coordinates_plotly_widget(search_data):
    plot_title = "Parallel Corrdinates"
    col1, col2 = st.beta_columns([1, 2])

    para_names_f = add_parameters_num(search_data, col1, plot_title)
    search_data_f = filter_parameter(search_data, para_names_f, col1, plot_title)
    color_para = select_color_para_num(search_data_f, col1, plot_title)

    fig = parallel_coordinates_plotly(
        search_data_f, dimensions=para_names_f, color=color_para
    )
    col2.plotly_chart(fig)


def parallel_categories_plotly_widget(search_data):
    plot_title = "Parallel Categories"
    col1, col2 = st.beta_columns([1, 2])

    para_names_f = add_parameters_num(search_data, col1, plot_title)
    search_data_f = filter_parameter(search_data, para_names_f, col1, plot_title)
    color_para = select_color_para_num(search_data_f, col1, plot_title)

    fig = parallel_categories_plotly(
        search_data, dimensions=para_names_f, color=color_para
    )

    col2.plotly_chart(fig)


def scatter_2d_plotly_widget(search_data):
    plot_title = "2D Scatter Plot"
    col1, col2 = st.beta_columns([1, 2])

    para_names = search_data.columns

    scatter2_para1 = col1.selectbox(
        "2D scatter plot parameter 1",
        para_names,
        index=0,
        key=plot_title + "_para1",
    )
    scatter2_para2 = col1.selectbox(
        "2D scatter plot parameter 2",
        para_names,
        index=1,
        key=plot_title + "_para2",
    )

    color_para = select_color_para_cat(search_data, col1, plot_title)

    fig = scatter_plotly(
        search_data,
        x=scatter2_para1,
        y=scatter2_para2,
        color=color_para,
    )

    col2.plotly_chart(fig)


def scatter_3d_plotly_widget(search_data):
    plot_title = "3D Scatter Plot"
    col1, col2 = st.beta_columns([1, 2])

    para_names = search_data.columns

    scatter3_para1 = col1.selectbox(
        "3D scatter plot parameter 1",
        para_names,
        index=0,
        key=plot_title + "_para1",
    )
    scatter3_para2 = col1.selectbox(
        "3D scatter plot parameter 2",
        para_names,
        index=1,
        key=plot_title + "_para2",
    )
    scatter3_para3 = col1.selectbox(
        "3D scatter plot parameter 3",
        para_names,
        index=2,
        key=plot_title + "_para3",
    )

    color_para = select_color_para_cat(search_data, col1, plot_title)

    fig = scatter_3d_plotly(
        search_data,
        x=scatter3_para1,
        y=scatter3_para2,
        z=scatter3_para3,
        color=color_para,
    )

    col2.plotly_chart(fig)
