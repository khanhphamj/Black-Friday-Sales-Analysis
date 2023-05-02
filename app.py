import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html
from pages import home, customer, product, revenue
from components import leftsidebar

# https://fontawesome.com/v4/ link v4
app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP,
                          'https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css'],
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
)
app.title = "Black Friday Sales - ABC Private Ltd"

content = html.Div(id="page-content", className='mt-0 mb-0')
app.layout = html.Div([dcc.Location(id="url"), leftsidebar.sidebar, content])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return home.layout
    elif pathname == "/khachhang":
        return customer.layout
    elif pathname == "/sanpham":
        return product.layout
    elif pathname == "/doanhthu":
        return revenue.layout
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


@app.callback(
    Output("sidebar", "className"),
    [Input("sidebar-toggle", "n_clicks")],
    [State("sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed"
    return ""


@app.callback(
    Output("collapse", "is_open"),
    [Input("navbar-toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True)
