import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html, callback
from codes import loader
import pandas as pd
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib.pyplot as plt  # pip install matplotlib
import mpld3  # pip install mpld3

df = pd.read_csv('data/black-friday-sales-eda.csv')

df['Gender'] = df['Gender'].replace(['F', 'M'], ['Female', 'Male'])
df['Marital_Status'] = df['Marital_Status'].replace([0, 1], ['Single', 'Married'])

layout = html.Div([
    dbc.Row([
        dbc.Card(dbc.CardBody([
            html.H4('BÁO CÁO CHI TIẾT SẢN PHẨM')], className='p-1'),
            className='text-center bg-danger bg-gradient bg-opacity-80 text-white mb-2')
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label("Product ID", html_for="dropdown"),
            dcc.Dropdown(
                id='proID_dropdown',
                options=[{'label': x, 'value': x} for x in sorted(df['Product_ID'].unique())],
                placeholder="Chọn...",
            ),
        ], xs=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Category 1'),
                    html.H6(id='lb_cat1')
                ], className='h-100 text-center shadow border-start border-warning border-5')
            ]),
        ], xs=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Category 2'),
                    html.H6(id='lb_cat2')
                ], className='h-100 text-center shadow border-start border-warning border-5')
            ]),
        ], xs=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Category 3'),
                    html.H6(id='lb_cat3')
                ], className='h-100 text-center shadow border-start border-warning border-5')
            ]),
        ], xs=3),
    ], className='mt-2 mb-2 align-items-stretch'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.H4('Doanh thu của [Product ID]'),
                    html.H6('(INR)', id='lb_doanhthu')
                ])
            ], className='text-center shadow border-start border-primary border-5'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.H4('Có [Num] khách hàng mua [Product ID] này',
                                    id='lb_numKH')
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


@callback(
    Output('lb_cat1', 'children'), # output theo thứ tự từ trên xuống của html
    Output('lb_cat2', 'children'),
    Output('lb_cat3', 'children'),
    Input("proID_dropdown", "value"),
)
def plot_data(dropdown_val):
    df_product = df[df['Product_ID'] == dropdown_val]

    product_category1_list = []
    product_category2_list = []
    product_category3_list = []

    if not np.isnan(df_product['Product_Category_1'].iloc[0]):
        product_category1_list = [f"#{df_product['Product_Category_1'].iloc[0]}"]
    else:
        product_category1_list = [f"N/A"]

    if not np.isnan(df_product['Product_Category_2'].iloc[0]):
        product_category2_list = [f"#{df_product['Product_Category_2'].iloc[0]}"]
    else:
        product_category2_list = [f"N/A"]

    if not np.isnan(df_product['Product_Category_3'].iloc[0]):
        product_category3_list = [f"#{df_product['Product_Category_3'].iloc[0]}"]
    else:
        product_category3_list = [f"N/A"]

    return product_category1_list, product_category2_list, product_category3_list
