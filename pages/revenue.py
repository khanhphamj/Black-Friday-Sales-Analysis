from dash import Dash, html, dcc, Input, Output, dash_table, callback  # pip install dash
import dash_bootstrap_components as dbc
import pandas as pd
from matplotlib.gridspec import GridSpec

import matplotlib.pyplot as plt  # pip install matplotlib
import mpld3  # pip install mpld3

layout = html.Div(children=[
    html.H1(children='This is our Revenue page'),

    html.Div(id='rev-output'),
])