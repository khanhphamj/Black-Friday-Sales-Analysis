import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html, callback
from codes import loader, home_chart_modal
from PIL import Image

card_home_banner = [
    dbc.CardBody([
        html.H4('BLACK FRIDAY SALES DASHBOARD')
    ], className='p-2'),
]

card_home_tongDoanhThu = [
    dbc.CardBody([
        html.P(children=[
            html.I(className="fa fa-money fa-sm"),
            html.Strong(' Tổng doanh thu'),
        ], className='pt-5'),
        html.H3('{:,.0f} (INR)'.format(loader.total_purchase), className="text-warning")
    ], className="h-50"),
]

card_home_tongUserID = [
    dbc.CardBody([
        html.P(children=[
            html.I(className="fa fa-users fa-sm"),
            html.Strong(' Số lượng khách hàng'),
        ], className='pt-5'),
        html.H3(loader.num_users, className="text-warning")
    ]),
]

card_home_married = [
    dbc.CardBody([
        html.P(children=[
            html.I(className="fa fa-users fa-sm"),
            html.Strong(' Khách hàng đã kết hôn'),
        ]),
        html.H3('{:,.2f} %'.format(loader.married_percent), className="text-warning")
    ]),
]

card_home_single = [
    dbc.CardBody([
        html.P(children=[
            html.I(className="fa fa-user fa-sm"),
            html.Strong(' Khách hàng độc thân'),
        ]),
        html.H3('{:,.2f} %'.format(loader.single_percent), className="text-warning")
    ]),
]

card_home_doanhThuTB = [
    dbc.CardBody([
        html.P(children=[
            html.I(className="fa fa-money fa-sm"),
            html.Strong(' Doanh thu trung bình trên mỗi khách hàng'),
        ], className='pt-5'),
        html.H3('{:,.0f} INR'.format(loader.median_purchase), className="text-warning")
    ]),
]

card_home_tiLeGioiTinhtheoTuoi = [
    dbc.CardBody(html.H6("Tỉ lệ giới tính và thống kê giới tính theo nhóm tuổi của khách hàng",
                         className="card-text")),
    html.Div([
        html.Div([
            dbc.CardImg(src=Image.open("imgs/home-modal1.png"),
                        bottom=True,
                        className="card-image")
        ]),
        html.Div([home_chart_modal.home_modal], className='card-middle')
    ], className='card-container'),
]

card_home_productIDMuaNhieuNhat = [
    dbc.CardBody([
        html.P(children=[
            html.I(className="fa fa-product-hunt fa-sm"),
            html.Strong(' Product_ID bán được nhiều nhất'),
        ]),
        html.H3(loader.top_1_bestseller_product, className="text-warning")
    ]),
]

card_home_productIDDoanhThuCaoNhat = [
    dbc.CardBody([
        html.P(children=[
            html.I(className="fa fa-product-hunt fa-sm"),
            html.Strong(' Product_ID có doanh thu cao nhất'),
        ]),
        html.H3(loader.top_1_bestpurchase_product, className="text-warning")
    ]),
]

card_home_catIDBanChayNhat = [
    dbc.CardBody([
        html.P(children=[
            html.I(className="fa fa-tasks fa-sm"),
            html.Strong(' Category bán chạy nhất'),
        ]),
        html.H3(f"{loader.most_common_value.index[0]} ({loader.most_common_value.values[0]:,} đơn hàng)",
                className="text-warning")
    ]),
]
