# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import importlib.metadata

__version__ = importlib.metadata.version("search-data-explorer")
__license__ = "MIT"


from .search_data_explorer import SearchDataExplorer


__all__ = [
    "SearchDataExplorer",
]
