<H1 align="center">
    Tabular Data Explorer
</H1>

<br>

<H2 align="center">
    Visualize multidimensional data from studies performed by Hyperactive and Gradient-Free-Optimizers.
</H2>



<br>

## Examples

```python
import pandas as pd
from tabular_data_explorer import TabularDataExplorer

# create so test dataset for this example
df_array = [[0.5, 6, 50, 0.6], [0.9, 7, 40, 0.7], [0.2, 9, 70, 0.8]]
columns = ["x1", "x2", "x3", "score"]
search_data = pd.DataFrame(df_array, columns=columns)
# save the dataframe to file
search_data.to_csv("./search_data.csv")


data_explorer = TabularDataExplorer()
# the dashboard must read the dataframe from a file
data_explorer.open("./search_data.csv")
```

The search data that is loaded from file must always follow the pattern below:

<table class="table">
<thead class="table-head">
    <tr class="row">
    <td class="cell">score</td>
    <td class="cell">x1</td>
    <td class="cell">x2</td>
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

Hereby "x1", "x2", ... can be given any name. But "score" is always necessary!



