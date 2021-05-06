# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


from .streamlit_elements import create_streamlit_setup


def open(search_data):
    create_streamlit_setup(search_data)
