# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import os


class TabularDataExplorer:
    def __init__(self, plots=["2D-Scatter-Plot"]):
        self.plots = plots

    def open(self, path):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)

        arg1 = path + " "
        args = " ".join(self.plots)

        command = "streamlit run " + dname + "/streamlit_run.py " + arg1 + args
        os.system(command)
