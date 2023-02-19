<H1 align="center">
    Search Data Explorer
</H1>

<br>

<H2 align="center">
    Visualize optimization search-data via plotly in a streamlit dashboard
</H2>

The Search-Data-Explorer is a simple application specialized to visualize search-data generated from [Gradient-Free-Optimizers](https://github.com/SimonBlanke/Gradient-Free-Optimizers) or [Hyperactive](https://github.com/SimonBlanke/Hyperactive). It is designed as an easy-to-use tool to gain insights into multi-dimensional data, as commonly found in optimization.


<br>

## Disclaimer

This project is in an early development stage and is only tested manually. If you encounter bugs or have suggestions for improvements, then please open an issue.


<br>

## Installation

```console
pip install search-data-explorer
```

<br>

## How to use

The Search Data Explorer has a very simple API, that can be explained by the examples below or just execute the command `search-data-explorer` in a command-line to open the Search Data Explorer without executing a python script.


<br>

### search-data requirements

The Search Data Explorer is used by loading the search-data with a few lines of code. The search data that is loaded from file must follow the pattern below. The columns can have any name but must contain the `score`, which is always included in search-data from [Gradient-Free-Optimizers](https://github.com/SimonBlanke/Gradient-Free-Optimizers) or [Hyperactive](https://github.com/SimonBlanke/Hyperactive).

<table class="table">
<thead class="table-head">
    <tr class="row">
    <td class="cell">first column name</td>
    <td class="cell">another column name</td>
    <td class="cell">...</td>
    <td class="cell">score</td>

    </tr>
</thead>
<tbody class="table-body">
    <tr class="row">
    <td class="cell">0.756</td>
    <td class="cell">0.1</td>
    <td class="cell">0.2</td>
    <td class="cell">-3</td>
    </tr>
    <tr class="row">
    <td class="cell">0.823</td>
    <td class="cell">0.3</td>
    <td class="cell">0.1</td>
    <td class="cell">-10</td>
    </tr>
    <tr class="row">
    <td class="cell">...</td>
    <td class="cell">...</td>
    <td class="cell">...</td>
    <td class="cell">...</td>
    </tr>
    <tr class="row">
    <td class="cell">...</td>
    <td class="cell">...</td>
    <td class="cell">...</td>
    <td class="cell">...</td>
    </tr>
</tbody>
</table>

<br>



## Examples

<br>

### Load search-data by passing dataframe

You can pass the search-data directly, if you do not want to save your search-data to disk and just explore it one time after the optimization has finished.

```python
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
```


### Load search-data by passing path to file

If you already have a search-data file on disk you can pass the path to the file to the search-data-explorer.

```python
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
search_data.to_csv("search_data.csv", index=False)


# Open Search-Data-Explorer

sde = SearchDataExplorer()
sde.open("model1.csv")  # pass path to file on disk
```


### Load search-data by browsing for file

You can just open the search-data-explorer without passing a file or path. In this case you can browse for the file via a menu inside the search-data-explorer.

```python
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
search_data.to_csv("search_data.csv", index=False)


# Open Search-Data-Explorer

sde = SearchDataExplorer()
sde.open()  # start without passing anything and use the file explorer within the search-data-explorer
```


