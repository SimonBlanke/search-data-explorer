# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


import pandas as pd
import streamlit as st

from .widgets import Widgets


def app(search_data, plots):
    try:
        st.set_page_config(page_title="Search Data Explorer", layout="wide")
        st.markdown(
            """
                <style>
                    .css-18e3th9 {
                            padding-top: 0rem;
                            padding-bottom: 5rem;
                            padding-left: 5rem;
                            padding-right: 5rem;
                        }
                    .css-1d391kg {
                            padding-top: 0rem;
                            padding-right: 1rem;
                            padding-bottom: 1rem;
                            padding-left: 1rem;
                        }
                </style>
                """,
            unsafe_allow_html=True,
        )
    except:
        pass

    st.sidebar.title("Search Data Explorer")
    st.sidebar.text("")
    st.sidebar.text("")
    st.sidebar.text("")

    if search_data is None:
        uploaded_file = st.sidebar.file_uploader("Load a search-data file:")
        if uploaded_file is not None:
            search_data = pd.read_csv(uploaded_file)

    if search_data is not None:
        create_widgets(search_data)


def create_widgets(search_data):
    widgets = Widgets(search_data)

    plot_names = st.sidebar.multiselect(
        label="Select Widgets:",
        options=list(widgets.plots_select_dict.keys()),
    )

    for plot_name in plot_names:
        widgets.plots_select_dict[plot_name]()

        for _ in range(7):
            st.write(" ")
