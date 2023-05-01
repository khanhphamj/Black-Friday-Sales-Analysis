import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html
from codes import loader

card_home_banner = [
    dbc.CardBody([
        html.H3('BLACK FRIDAY SALES DASHBOARD', className="m-0")
    ], className='p-3'),
]

card_home_tongDoanhThu = [
    dbc.CardBody([
        html.P('#Tổng doanh thu', className='pt-5'),
        html.H3('{:,.0f} (INR)'.format(loader.total_purchase), className="text-danger")
    ], className="h-50"),
]

card_home_tongUserID = [
    dbc.CardBody([
        html.P('#Số lượng khách hàng', className='pt-5'),
        html.H3(loader.num_users, className="text-danger")
    ]),
]

card_home_married = [
    dbc.CardBody([
        html.P('Khách hàng đã kết hôn'),
        html.H3('{:,.2f} %'.format(loader.married_percent), className="text-danger")
    ]),
]

card_home_single = [
    dbc.CardBody([
        html.P('Khách hàng độc thân'),
        html.H3('{:,.2f} %'.format(loader.single_percent), className="text-danger")
    ]),
]

card_home_doanhThuTB = [
    dbc.CardBody([
        html.P('Doanh thu trung bình trên mỗi khách hàng', className='pt-5'),
        html.H3('{:,.0f} INR'.format(loader.median_purchase), className="text-danger")
    ]),
]

card_home_tiLeGioiTinhtheoTuoi = [
    dbc.CardBody([
        html.P('#Tỉ lệ giới tính và thống kê giới tính '
               'theo nhóm tuổi của khách hàng'),
        html.H3('Chart')
    ]),
]

card_home_productIDMuaNhieuNhat = [
    dbc.CardBody([
        html.P('#Product_ID sản phẩm bán chạy nhất'),
        html.H3(loader.top_1_bestseller_product, className="text-danger")
    ]),
]

card_home_productIDDoanhThuCaoNhat = [
    dbc.CardBody([
        html.P('#Product_ID sản phẩm có doanh thu cao nhất'),
        html.H3(loader.top_1_bestpurchase_product, className="text-danger")
    ]),
]

card_home_catIDBanChayNhat = [
    dbc.CardBody([
        html.P('#Category sản phẩm bán chạy nhất'),
        html.H3(f"{loader.most_common_value.index[0]} ({loader.most_common_value.values[0]:,} đơn hàng)",
                className="text-danger")
    ]),
]
