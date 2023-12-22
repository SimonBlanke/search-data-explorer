# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


import pandas as pd
import streamlit as st
import sqlalchemy as sql

from .widgets import Widgets


def read_search_data(path):
    if path.endswith(".csv"):
        search_data = pd.read_csv(path)
    elif path.endswith(".db"):
        dbEngine = sql.create_engine("sqlite:///" + path)
        tables = sql.inspect(dbEngine).get_table_names()
        table = st.sidebar.selectbox("Tables", tables)
        search_data = pd.read_sql_table(table, dbEngine)

    if len(search_data) == 0:
        print("---> Error: Search data is empty!")
    else:
        return search_data


def app(path, plots):
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

    if path == "no_path":
        uploaded_file = st.sidebar.file_uploader("Load a search-data file:")
        if uploaded_file is not None:
            search_data = pd.read_csv(uploaded_file)
    else:
        search_data = read_search_data(path)

    if search_data is not None:
        create_widgets(search_data)


def create_widgets(search_data):
    widgets = Widgets(search_data)

    plot_name = st.sidebar.selectbox(
        label="Select Widget:",
        options=list(widgets.plots_select_dict.keys()),
    )

    widgets.plots_select_dict[plot_name]()

    for _ in range(7):
        st.write(" ")
