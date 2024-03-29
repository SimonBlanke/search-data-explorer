# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import numpy as np


class Filter:
    def __init__(self, search_data):
        self.search_data = search_data
        self.col_names = list(search_data.columns)
        self.para_names = [n for n in self.col_names if n != "score"]
        self.get_data_types()

    def get_data_types(self):
        data_types = {}
        cat_para_names = []
        num_para_names = []

        for para_name in self.col_names:
            values = self.search_data[para_name].values

            try:
                values * values
                values - values
            except:
                data_types[para_name] = "categorical"
                cat_para_names.append(para_name)

            else:
                data_types[para_name] = "numeric"
                num_para_names.append(para_name)

        # print("\n data_types \n", data_types, "\n")
        self.data_types = data_types
        self.cat_para_names = cat_para_names
        self.num_para_names = num_para_names

    def filter_parameter(self, _st_, search_data, para_names=None):
        _name_ = "filter_parameter"

        if para_names is None:
            para_names = self.col_names

        para_names_fil = _st_.multiselect(
            label="Filter Parameters:",
            options=para_names,
        )

        search_data = search_data.copy()
        for para_name in para_names_fil:
            para_data = search_data[para_name].values

            _st_.divider()

            if self.data_types[para_name] == "categorical":
                cat_values = np.unique(para_data)
                cat_values_fil = _st_.multiselect(
                    label="filter '" + para_name + "' parameters:",
                    options=cat_values,
                    default=cat_values,
                )

                search_data = search_data[search_data[para_name].isin(cat_values_fil)]

            else:
                min_ = float(np.min(para_data))
                max_ = float(np.max(para_data))
                step = (max_ - min_) / 100

                if step == 0:
                    continue

                col1, col2 = _st_.columns([1, 1])
                lower = col1.number_input(
                    "'" + para_name + "' lower bound:", min_, max_, min_
                )
                upper = col2.number_input(
                    "'" + para_name + "' upper bound:", min_, max_, max_
                )

                search_data = search_data[
                    (search_data[para_name] >= lower)
                    & (search_data[para_name] <= upper)
                ]

        return search_data
