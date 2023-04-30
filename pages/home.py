import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html
from components import  card

layout = html.Div([
    dbc.Row([
        dbc.Card(card.card_home_banner, className='text-center bg-danger bg-gradient bg-opacity-80 text-white')
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Card(card.card_home_tongDoanhThu, className='h-100 text-center shadow border-start border-success border-5')
        ], xs=3),
        dbc.Col([
            dbc.Card(card.card_home_tongUserID, className='h-100 text-center shadow border-start border-success border-5')
        ], xs=3),
        dbc.Col([
            dbc.Card(card.card_home_married, className='text-center shadow border-start border-success border-5'),
            dbc.Row([
                dbc.Col([
                    dbc.Card(card.card_home_single, className='text-center shadow border-start border-success border-5')
                ])
            ], className='pt-1')
        ], xs=3),
        dbc.Col([
            dbc.Card(card.card_home_doanhThuTB, className='h-100 text-center shadow border-start border-success border-5')
        ], xs=3),
    ], className='mt-4 mb-4 align-items-stretch'),
    dbc.Row([
        dbc.Col([
            dbc.Card(card.card_home_tiLeGioiTinhtheoTuoi, className='h-100 text-center shadow border-start border-success border-5')
        ], xs=6),
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card(card.card_home_productIDMuaNhieuNhat, className='text-center shadow border-start border-success border-5')
                ], xs=6),
                dbc.Col([
                    dbc.Card(card.card_home_productIDDoanhThuCaoNhat, className='text-center shadow border-start border-success border-5')
                ], xs=6)
            ], className='pb-1'),
            dbc.Card(card.card_home_catIDBanChayNhat, className='text-center shadow border-start border-success border-5'),
        ], xs=6)
    ], className='p-2 align-items-stretch'),
    # content
])