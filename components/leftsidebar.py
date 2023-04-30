import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html

banner_url = "https://www.freepnglogos.com/uploads/abc-png-logo/play-abc-logo-png-22.png"

sidebar_header = dbc.Row(
    [
        dbc.Col(html.Img(src=banner_url, width="50%"), style={'textAlign': 'center'}),
        # dbc.Col(html.H3("ABC Ltd", className="text-center")),
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P("ABC PRIVATE LTD", className="lead text-center",
                       ),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Tổng quan", href="/", active="exact"),
                    dbc.NavLink("Khách hàng", href="/khachhang", active="exact"),
                    dbc.NavLink("Sản phẩm", href="/sanpham", active="exact"),
                    dbc.NavLink("Doanh thu", href="/doanhthu", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)
