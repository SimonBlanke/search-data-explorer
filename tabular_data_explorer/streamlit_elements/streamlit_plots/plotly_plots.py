# Author: Simon Blanke
# Email: simon.blanke@yahoo.com
# License: MIT License

import plotly.express as px


color_scale = px.colors.sequential.Jet


def parallel_coordinates_plotly(*args, **kwargs):
    return px.parallel_coordinates(*args, **kwargs, color_continuous_scale=color_scale)


def parallel_categories_plotly(*args, **kwargs):
    return px.parallel_categories(*args, **kwargs, color_continuous_scale=color_scale)


def scatter_plotly(*args, **kwargs):
    return px.scatter(*args, **kwargs, color_continuous_scale=color_scale)


def scatter_3d_plotly(*args, **kwargs):
    return px.scatter_3d(*args, **kwargs, color_continuous_scale=color_scale)


def scatter_1d_matplot(*args, **kwargs):
    from sklearn.gaussian_process import GaussianProcessRegressor

    para_names = search_data.columns.drop("score")

    st.text("")
    col1, col2 = st.beta_columns(2)

    col1.header("1D Scatter Plot")
    col1.text("")

    scatter1_para1 = col1.selectbox(
        "1D scatter plot parameter 1",
        para_names,
        index=0,
    )

    fig1 = px.scatter(
        search_data, x=scatter1_para1, y=search_data["score"]
    ).update_layout(width=1000, height=600)

    x_train_1D = search_data[scatter1_para1].values.reshape(-1, 1)

    gpr = GaussianProcessRegressor()
    gpr.fit(x_train_1D, search_data["score"])

    print("\n x_train_1D \n", x_train_1D)

    min_ = -10
    max_ = 10
    step = 0.1

    x_plot = np.arange(min_, max_, step).reshape(-1, 1)

    mu, sigma = gpr.predict(x_plot, return_std=True)
    mu = mu.reshape(-1, 1)
    sigma = sigma.reshape(-1, 1)

    line_df = {
        "x": x_plot.reshape(
            -1,
        ),
        "bayes fit": mu.reshape(
            -1,
        ),
    }

    y_upper = mu + sigma
    y_lower = mu - sigma

    fig2 = px.line(line_df, x="x", y="bayes fit")

    fig3 = go.Figure(data=fig1.data + fig2.data)

    col2.plotly_chart(fig3)
