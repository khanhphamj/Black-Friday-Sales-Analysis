import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html
from components import card_revenue

layout = html.Div([
    dbc.Row([
        dbc.Card(card_revenue.card_revenue_banner,
                 className='text-center bg-danger bg-gradient bg-opacity-80 text-white mb-2')
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label("Product ID", html_for="dropdown"),
            dcc.Dropdown(
                options=[
                    {"label": "Option 1", "value": 1},
                    {"label": "Option 2", "value": 2},
                ],
                placeholder="Chọn...",
            ),
        ], xs=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Category 1'),
                    html.H6('#')
                ], className='h-100 text-center shadow border-start border-warning border-5')
            ]),
        ], xs=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Category 2'),
                    html.H6('#')
                ], className='h-100 text-center shadow border-start border-warning border-5')
            ]),
        ], xs=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Category 3'),
                    html.H6('#')
                ], className='h-100 text-center shadow border-start border-warning border-5')
            ]),
        ], xs=3),
    ], className='mt-2 mb-2 align-items-stretch'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Doanh thu của [Product ID]'),
                    html.H6('(INR)')
                ])
            ], className='text-center shadow border-start border-primary border-5'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Có [Num] khách hàng mua [Product ID] này')
                        ])
                    ], className='h-100 text-center shadow border-start border-primary border-5')
                ])
            ], className='pt-3')
        ], xs=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Bar chart'),
                ])
            ], className='h-100 text-center shadow border-start border-primary border-5')
        ], xs=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Pie chart 1')
                ])
            ], className='text-center shadow border-start border-primary border-5'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Pie chart 2')
                        ])
                    ], className='h-100 text-center shadow border-start border-primary border-5')
                ])
            ], className='pt-3')
        ], xs=3),
    ], className='p-2 align-items-stretch'),
    # content
])
