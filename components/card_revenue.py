import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html, callback
from codes import loader, home_chart_modal
from PIL import Image

card_revenue_banner = [
    dbc.CardBody([
        html.H4('BÁO CÁO CHI TIẾT SẢN PHẨM')
    ], className='p-1'),
]