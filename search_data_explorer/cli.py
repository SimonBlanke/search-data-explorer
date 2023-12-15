import sys

from search_data_explorer import SearchDataExplorer


def open():
    sde = SearchDataExplorer()
    if len(sys.argv) == 2:
        sde.open(sys.argv[1])
    elif len(sys.argv) == 1:
        sde.open()
    else:
        msg = "Number of Arguments invalid"
        raise Exception(msg)
