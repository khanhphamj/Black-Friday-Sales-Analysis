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
            html.H4('BÁO CÁO CHI TIẾT SẢN PHẨM', id="lb_title")], className='p-1'),
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
                    html.P('Category 1'),
                    html.H3(id='lb_cat1', className="text-danger")
                ], className='h-100 text-center shadow border-start border-warning border-5')
            ]),
        ], xs=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P('Category 2'),
                    html.H3(id='lb_cat2', className="text-danger")
                ], className='h-100 text-center shadow border-start border-warning border-5')
            ]),
        ], xs=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P('Category 3'),
                    html.H3(id='lb_cat3', className="text-danger")
                ], className='h-100 text-center shadow border-start border-warning border-5')
            ]),
        ], xs=3),
    ], className='mt-2 mb-2 align-items-stretch'),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.P('Doanh thu'),
                    html.H3('', id='lb_doanhthu', className="text-danger")
                ])
            ], className='text-center shadow border-start border-success border-5'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.P('Số khách hàng mua sản phẩm'),
                            html.H3('', id='lb_numKH', className="text-danger")

                        ])
                    ], className='h-100 text-center shadow border-start border-success border-5')
                ])
            ], className='pt-3')
        ], xs=3),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Iframe(
                        id='rev-bar-plot',
                        srcDoc=None,  # here is where we will put the graph we make
                        style={"height": "500px", "width": "100%"}),
                ])
            ], className='text-center shadow border-start border-success border-5')
        ], xs=6),
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.Iframe(
                        id='rev-pie1-plot',
                        srcDoc=None,  # here is where we will put the graph we make
                        style={"height": "250px", "width": "100%"}),
                ])
            ], className='text-center shadow border-start border-success border-5'),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardBody([
                            html.Iframe(
                                id='rev-pie2-plot',
                                srcDoc=None,  # here is where we will put the graph we make
                                style={"height": "250px", "width": "100%"}),
                        ])
                    ], className='text-center shadow border-start border-success border-5')
                ])
            ], className='pt-3')
        ], xs=3),
    ], className='p-2 align-items-stretch'),
    # content
])


@callback(
    Output('lb_title', 'children'),
    Output('lb_cat1', 'children'),
    Output('lb_cat2', 'children'),
    Output('lb_cat3', 'children'),
    Output('lb_numKH', 'children'),
    Output('lb_doanhthu', 'children'),
    Output('rev-bar-plot', 'srcDoc'),
    Output('rev-pie1-plot', 'srcDoc'),
    Output('rev-pie2-plot', 'srcDoc'),
    Input("proID_dropdown", "value"),
)
def plot_data(dropdown_val):
    lb_title = [f"BÁO CÁO CHI TIẾT SẢN PHẨM {dropdown_val}"]

    df_product = df[df['Product_ID'] == dropdown_val]

    # Get Category 1, 2, 3 by Product ID
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

    # Number of orders by Product ID
    unique_counts = df.groupby('Product_ID')['User_ID'].nunique()
    count = unique_counts.get(dropdown_val, 0)
    num_orders = [f"{count}"]

    # Tổng doanh thu by Product ID
    revenue_f = df_product['Purchase'].sum()
    revenue = ['{:,.0f} (INR)'.format(revenue_f)]

    # plot charts
    # ---------------------------------------
    fig1, ax1 = plt.subplots(figsize=(6, 4.6))
    age_gender_counts = df_product.groupby(['Age', 'Gender'])['User_ID'].nunique().reset_index()
    male_data = age_gender_counts[age_gender_counts['Gender'] == 'Male']
    female_data = age_gender_counts[age_gender_counts['Gender'] == 'Female']
    ax1.bar(male_data['Age'], male_data['User_ID'], color='cornflowerblue', alpha=1, label='Nam', align='edge',
            width=-0.4)
    ax1.bar(female_data['Age'], female_data['User_ID'], color='orange', alpha=1, label='Nữ', align='edge', width=0.4)
    ax1.set_xlabel('Nhóm tuổi', fontsize=20)
    ax1.set_ylabel('Khách hàng', fontsize=20)
    ax1.legend()
    for index, row in male_data.iterrows():
        ax1.text(row['Age'], row['User_ID'], str(row['User_ID']), ha='right', va='bottom')
    for index, row in female_data.iterrows():
        ax1.text(row['Age'], row['User_ID'], str(row['User_ID']), ha='left', va='bottom')
    html_bar = mpld3.fig_to_html(fig1)
    # ---------------------------------------
    gender_counts = df_product.groupby('Gender')['User_ID'].nunique()
    fig2, ax2 = plt.subplots(1, 1, figsize=(2.5, 2.5))
    colors = ['orange', 'cornflowerblue']
    ax2.pie(gender_counts, autopct='%1.1f%%', colors=colors, wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    ax2.set_title('Tỉ lệ giới tính', fontweight='bold')
    html_pie1 = mpld3.fig_to_html(fig2)

    # ---------------------------------------
    purchase_by_gender = df_product.groupby('Gender')['Purchase'].sum()
    sizes = purchase_by_gender.values
    fig3, ax3 = plt.subplots(1, 1, figsize=(2.5, 2.5))
    ax3.pie([1], radius=0.3, colors=['white'], wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    wedges, texts, autotexts = ax3.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85,
                                       labeldistance=1.1,
                                       wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    centre_circle = plt.Circle((0, 0), 0.68, color='black', fc='white', linewidth=1.25)
    fig3.gca().add_artist(centre_circle)

    revenue_text = 'Doanh thu trung bình:'
    revenue_text1 = 'Nam INR{:,.0f}'.format(purchase_by_gender['Male'] / df['User_ID'].nunique())
    revenue_text2 = 'Nữ INR{:,.0f}'.format(purchase_by_gender['Female'] / df['User_ID'].nunique())

    plt.text(0, 0.3, s=revenue_text, ha='center', va='center', fontsize=9.5)
    plt.text(0, 0.15, s=revenue_text1, ha='center', va='center', fontsize=9.5)
    plt.text(0, 0, s=revenue_text2, ha='center', va='center', fontsize=9.5)

    ax3.set_title('Tỉ lệ doanh thu theo giới tính khách hàng', fontweight='bold')
    html_pie2 = mpld3.fig_to_html(fig3)

    # --------------------------------------
    # return các biến theo thứ tự của các Output đã khai báo ở callback
    return lb_title, product_category1_list, product_category2_list, product_category3_list, \
        num_orders, revenue, html_bar, html_pie1, html_pie2
