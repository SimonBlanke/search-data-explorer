# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import pandas as pd


def read_search_data(path):
    search_data = pd.read_csv(path)
    if len(search_data) == 0:
        print("---> Error: Search data is empty!")
    else:
        return search_data
