# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import os


class DataExplorer:
    def __init__(self):
        pass


class ProgressBoard:
    def __init__(self):
        pass

    def open(self, path):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)

        command = "streamlit run " + dname + "/progess_board_script.py " + path
        os.system(command)


class OptimizationPlotter:
    def __init__(self):
        pass

    def open(self, path):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)

        command = "streamlit run " + dname + "/streamlit_run.py " + path
        os.system(command)
