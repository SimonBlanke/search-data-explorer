class Widgets:
    def __init__(self, search_data):
        self.search_data = search_data

        self.plots_select_dict = {
            "Overview": self.table_overview_widget,
            "2D Scatter": self.scatter_2d_plotly_widget,
            "3D Scatter": self.scatter_3d_plotly_widget,
            "Parallel Coordinates": self.parallel_coordinates_plotly_widget,
            "Parallel Categories": self.parallel_categories_plotly_widget,
            "Scatter Matrix": self.scatter_matrix_plotly_widget,
        }
