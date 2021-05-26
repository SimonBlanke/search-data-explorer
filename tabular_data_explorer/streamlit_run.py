# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import sys

from read_search_data import read_search_data
from streamlit_setup import create_streamlit_setup


path = sys.argv[1]
plots = sys.argv[2:]

search_data = read_search_data(path)
create_streamlit_setup(search_data, plots)
