# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import uuid
import numpy as np


def filter_parameter(search_data, col1, key):
    para_names = search_data.columns

    para_names_rem = col1.multiselect(
        label="Remove Parameters:",
        options=para_names,
        key=key + "_remove",
    )

    search_data = search_data.drop(para_names_rem, axis=1)
    para_names = search_data.columns

    para_names_fil = col1.multiselect(
        label="Filter Parameters:",
        options=para_names,
        key=key + "_filter",
    )

    for para_name in para_names_fil:
        para_data = search_data[para_name].values
        min_ = float(np.min(para_data))
        max_ = float(np.max(para_data))
        step = (max_ - min_) / 100

        (lower, upper) = col1.slider(
            "Filter: " + str(para_name),
            min_value=min_,
            max_value=max_,
            value=(min_, max_),
            step=step,
        )
        col1.text("")

        search_data = search_data[
            (search_data[para_name] >= lower) & (search_data[para_name] <= upper)
        ]

    return search_data
