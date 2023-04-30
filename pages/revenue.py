import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html

layout = html.Div(children=[
    html.H1(children='This is our Revenue page'),
	html.Div([
        "Select a city: ",
        dcc.RadioItems(['New York City', 'Montreal','San Francisco'],
        'Montreal',
        id='analytics-input')
    ]),
	html.Br(),
    html.Div(id='analytics-output'),
])