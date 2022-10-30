# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import os
import pandas as pd


class SearchDataExplorer:
    def __init__(self, plots=["Overview"], parameters="all"):
        self.plots = plots
        self.parameters = parameters

    def _run_streamlit(self, path, port):
        if port == "auto":
            port_cmd = ""
        else:
            port_cmd = " --server.port " + str(port)

        abspath = os.path.abspath(__file__)
        dname = os.path.dirname(abspath)

        arg1 = path + " "
        args = " ".join(self.plots)

        command = (
            "streamlit run " + dname + "/streamlit_run.py " + arg1 + args + port_cmd
        )
        os.system(command)

    def open(self, input=None, port="auto"):
        if isinstance(input, pd.DataFrame):
            df = input
            path_tmp = "./df_temp.csv~"

            df.to_csv(path_tmp, index=False)

            self._run_streamlit(path_tmp, port)

            if os.path.exists(path_tmp):
                os.remove(path_tmp)

        elif isinstance(input, str):
            path = input
            self._run_streamlit(path, port)

        elif input is None:
            path = "no_path"
            self._run_streamlit(path, port)
