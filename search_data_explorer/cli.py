import sys

from search_data_explorer import SearchDataExplorer


def open():
    sde = SearchDataExplorer()
    sde.open(sys.argv[1])
