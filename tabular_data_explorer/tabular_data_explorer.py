# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import os


class TabularDataExplorer:
    def __init__(self):
        pass

    def open(self, path):
        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)

        command = "streamlit run " + dname + "/streamlit_run.py " + path
        os.system(command)
