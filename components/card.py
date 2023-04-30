import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html
from components import  card

card_home_banner = [
    dbc.CardBody([
        html.H3('BLACK FRIDAY SALES DASHBOARD', className="m-0")
    ], className='p-3'),
]

card_home_tongDoanhThu = [
    dbc.CardBody([
        html.P('#Tổng doanh thu', className='pt-5'),
        html.H4('DT', className="text-info")
    ], className="h-50"),
]

card_home_tongUserID = [
    dbc.CardBody([
        html.P('#Tổng khách hàng đặt hàng', className='pt-5'),
        html.H4('User_ID', className="text-info")
    ]),
]

card_home_married = [
    dbc.CardBody([
        html.P('Đã có gia đình'),
        html.H4('%', className="text-info")
    ]),
]

card_home_single = [
    dbc.CardBody([
        html.P('Độc thân'),
        html.H4('%', className="text-info")
    ]),
]

card_home_doanhThuTB = [
    dbc.CardBody([
        html.P('Doanh thu trung bình trên mỗi hóa đơn', className='pt-5'),
        html.H4('DT', className="text-info")
    ]),
]

card_home_tiLeGioiTinhtheoTuoi = [
    dbc.CardBody([
        html.P('#Tỉ lệ giới tính và thống kê giới tính '
               'theo nhóm tuổi của khách hàng'),
        html.H4('Chart')
    ]),
]

card_home_productIDMuaNhieuNhat = [
    dbc.CardBody([
        html.P('#Product_ID được mua nhiều nhất'),
        html.H4('Product ID', className="text-info")
    ]),
]

card_home_productIDDoanhThuCaoNhat = [
    dbc.CardBody([
        html.P('#Product_ID sản phẩm có doanh thu cao nhất'),
        html.H4('Product_ID', className="text-info")
    ]),
]

card_home_catIDBanChayNhat = [
    dbc.CardBody([
        html.P('#Category sản phẩm bán chạy nhất'),
        html.H4('Cat_ID', className="text-info")
    ]),
]