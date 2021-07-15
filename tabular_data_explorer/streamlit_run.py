# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import sys

from read_search_data import read_search_data
from streamlit_setup import create_streamlit_setup


def main():
    path = sys.argv[1]
    plots = sys.argv[2:]

    if path == "no_path":
        search_data = None
    else:
        search_data = read_search_data(path)

    create_streamlit_setup(search_data, plots)


if __name__ == "__main__":
    main()
