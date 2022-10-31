import os
import sys

from search_data_explorer import SearchDataExplorer


here = os.path.dirname(os.path.realpath(__file__))
path2file = os.path.join(here, "test_data.csv")

"""
port = sys.argv[-1]
print("Connect to port:", port)
"""
board = SearchDataExplorer()
board.open(path2file)
