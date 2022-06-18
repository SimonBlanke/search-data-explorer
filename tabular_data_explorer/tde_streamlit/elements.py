# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


import numpy as np
import pandas as pd


def create_plotly_chart(_st_, plot_func, plot_kwargs):
    fig = plot_func(**plot_kwargs)
    _st_.plotly_chart(fig)


def to_int(number):
    if number.is_integer():
        return int(number)
    else:
        return number


def statistics(search_data):
    search_data_rel = search_data.drop(
        ["eval_time", "iter_time"], axis=1, errors="ignore"
    )

    search_data_num = search_data_rel.select_dtypes(include=[np.number])

    statistics_d = {}

    for col in search_data_num.columns:
        col_np = search_data_num[col].values
        counts_ = np.unique(col_np).shape[0]
        min_ = float(np.min(col_np))
        max_ = float(np.max(col_np))
        mean_ = float(col_np.mean())
        median_ = float(np.median(col_np))

        statistics_d[col] = [
            counts_,
            to_int(min_),
            to_int(max_),
            to_int(mean_),
            to_int(median_),
        ]

    columns = ["uniques", "min", "max", "mean", "median"]

    statistics_df = pd.DataFrame.from_dict(
        statistics_d, orient="index", columns=columns
    )
    return statistics_df
