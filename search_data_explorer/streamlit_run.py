# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import sys
import pandas as pd

from tde_streamlit import app


def read_search_data(path):
    search_data = pd.read_csv(path)
    if len(search_data) == 0:
        print("---> Error: Search data is empty!")
    else:
        return search_data


def main():
    path = sys.argv[1]
    plots = sys.argv[2:]

    if path == "no_path":
        search_data = None
    else:
        search_data = read_search_data(path)

    app(search_data, plots)


if __name__ == "__main__":
    main()
