<H1 align="center">
    Search Data Explorer
</H1>

<br>

<H2 align="center">
    Visualize dataframes via plotly in a streamlit dashboard
</H2>


<br>

## Installation

Coming soon


<br>

## Examples

Visualize the iris dataset:

```python
import plotly.express as px
from search_data_explorer import SearchDataExplorer

iris_dataset = px.data.iris()
iris_dataset.to_csv("iris_dataset.csv", index=False)

sde = SearchDataExplorer()
sde.open("iris_dataset.csv")
```

<br>

Or create your own test data and visualize it:

```python
import pandas as pd
from search_data_explorer import SearchDataExplorer

# create so test dataset for this example
df_array = [[0.5, 6, 50, 0.6], [0.9, 7, 40, 0.7], [0.2, 9, 70, 0.8]]
columns = ["x1", "x2", "x3", "score"]
search_data = pd.DataFrame(df_array, columns=columns)
# save the dataframe to file
search_data.to_csv("./search_data.csv")


sde = SearchDataExplorer()
# the dashboard must read the dataframe from a file
sde.open("./search_data.csv")
```

<br>

The search data that is loaded from file must follow the pattern below. The columns can have any name and some plots can handle data other than numerical.

<table class="table">
<thead class="table-head">
    <tr class="row">
    <td class="cell">first column name</td>
    <td class="cell">another column name</td>
    <td class="cell">bla bla bla</td>
    <td class="cell">...</td>
    </tr>
</thead>
<tbody class="table-body">
    <tr class="row">
    <td class="cell">0.756</td>
    <td class="cell">0.1</td>
    <td class="cell">0.2</td>
    <td class="cell">...</td>
    </tr>
    <tr class="row">
    <td class="cell">0.823</td>
    <td class="cell">0.3</td>
    <td class="cell">0.1</td>
    <td class="cell">...</td>
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




