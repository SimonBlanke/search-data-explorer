# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

from widgets import plots_select_dict, plots_default_dict, processing_dict


import pandas as pd
import streamlit as st

from streamlit_elements.toc import Toc


widget_dict = {**plots_select_dict, **processing_dict}
search_data_dict = {}


def create_streamlit_setup(search_data, plots):
    try:
        st.set_page_config(page_title="Tabular Data Explorer", layout="wide")
    except:
        pass

    plots_default = [plots_default_dict[key] for key in plots]

    st.sidebar.title("Tabular Data Explorer")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")

    if search_data is None:
        uploaded_file = st.sidebar.file_uploader("Choose a file")
        if uploaded_file is not None:
            search_data = pd.read_csv(uploaded_file)

    if search_data is not None:
        create_widgets(search_data, plots_default)


def create_widgets(search_data, plots_default):
    plot_names = st.sidebar.multiselect(
        label="Select Plots:",
        options=list(plots_select_dict.keys()),
        default=plots_default,
    )
    proc_names = st.sidebar.multiselect(
        label="Select Processors:",
        options=list(processing_dict.keys()),
        # default=plots_default,
    )

    widget_list = plot_names + proc_names

    search_data_dict["default"] = search_data

    toc = Toc()
    toc.placeholder(sidebar=True)

    for widget in widget_list:
        toc.title(widget)
        st.components.v1.html(
            """<hr style="height:1px;border:none;color:#333;background-color:#333;" /> """,
            height=10,
        )
        ret = widget_dict[widget](search_data_dict)

        if isinstance(ret, tuple):
            search_data_dict[ret[1]] = ret[0]

        for _ in range(7):
            st.write(" ")

    toc.generate()
