import numpy as np
from gradient_free_optimizers import RandomSearchOptimizer

from search_data_explorer import SearchDataExplorer


def parabola_function(para):
    loss = para["x"] * para["x"] + para["y"] * para["y"] + para["y"] * para["y"]
    return -loss


search_space = {
    "x": np.arange(-10, 10, 0.1),
    "y": np.arange(-10, 10, 0.1),
    "z": np.arange(-10, 10, 0.1),
}

# generate search-data for this example with gradient-free-optimizers

opt = RandomSearchOptimizer(search_space)
opt.search(parabola_function, n_iter=1000)

search_data = opt.search_data


# Open Search-Data-Explorer

sde = SearchDataExplorer()
sde.open(search_data)  # pass search-data
