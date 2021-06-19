# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import os
import pandas as pd


class TabularDataExplorer:
    def __init__(self, plots=["2D-Scatter-Plot"]):
        self.plots = plots

    def _run_streamlit(self, path):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)

        arg1 = path + " "
        args = " ".join(self.plots)

        command = "streamlit run " + dname + "/streamlit_run.py " + arg1 + args
        os.system(command)

    def open(self, input=None):
        if isinstance(input, pd.DataFrame):
            df = input
            df.to_csv("df_temp.csv", index=False)
            path = "./df_temp.csv"

            self._run_streamlit(path)

            if os.path.exists(path):
                os.remove(path)

        elif isinstance(input, str):
            path = input
            self._run_streamlit(path)

        elif input is None:
            path = "no_path"
            self._run_streamlit(path)
