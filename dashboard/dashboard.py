# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import os

# from ..ltm_data_path import ltm_data_path


class Dashboard:
    def __init__(
        self,
        plots=[
            "score_statistics",
            "1d_scatter",
            "2d_scatter",
            "3d_scatter",
            "parallel_coordinates",
        ],
    ):
        self.plots = plots

    def open_search_data_file(self, path):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)

        streamlit_plot_args = " ".join(self.plots)

        command = (
            "streamlit run "
            + dname
            + "/st_script.py "
            + path
            + " "
            + streamlit_plot_args
        )
        os.system(command)

    def open_search_data_path(self, search_data_path, model_name=None, study_name=None):
        pass
