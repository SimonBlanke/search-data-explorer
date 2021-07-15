# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License


from streamlit_elements.streamlit_widgets import (
    scatter_2d_plotly_widget,
    scatter_3d_plotly_widget,
    parallel_coordinates_plotly_widget,
    parallel_categories_plotly_widget,
    parallel_coordinates_hiplot_widget,
    correlation_heatmap_seaborn_widget,
    scatter_matrix_plotly_widget,
    table_plotly_widget,
)


plots_select_dict = {
    "2D Scatter (Plotly)": scatter_2d_plotly_widget,
    "3D Scatter (Plotly)": scatter_3d_plotly_widget,
    "Parallel Coordinates (Plotly)": parallel_coordinates_plotly_widget,
    "Parallel Categories (Plotly)": parallel_categories_plotly_widget,
    "Parallel Categories (HiPlot)": parallel_coordinates_hiplot_widget,
    "Correlation Heatmap (Seaborn)": correlation_heatmap_seaborn_widget,
    "Scatter Matrix (Plotly)": scatter_matrix_plotly_widget,
    "Table (Plotly)": table_plotly_widget,
}


plots_default_dict = {
    "2D-Scatter-Plotly": "2D Scatter (Plotly)",
    "3D-Scatter-Plotly": "3D Scatter (Plotly)",
    "Parallel-Coordinates-Plotly": "Parallel Coordinates (Plotly)",
    "Parallel-Categories-Plotly": "Parallel Categories (Plotly)",
    "Parallel-Categories-HiPlot": "Parallel Categories (HiPlot)",
    "Correlation-Heatmap-Seaborn": "Correlation Heatmap (Seaborn)",
    "Scatter-Matrix-Plotly": "Scatter Matrix (Plotly)",
    "Table-Plotly": "Table (Plotly)",
}
