import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html, callback
from codes import loader
import pandas as pd
from matplotlib.gridspec import GridSpec

import matplotlib.pyplot as plt  # pip install matplotlib
import mpld3  # pip install mpld3

df = pd.read_csv('data/black-friday-sales-eda.csv')

df['Gender'] = df['Gender'].replace(['F', 'M'], ['Female', 'Male'])
df['Marital_Status'] = df['Marital_Status'].replace([0, 1], ['Single', 'Married'])

home_modal = html.Div([
    dbc.Button(html.I(className="fa fa-search-plus fa-2x"),
               color="light", className="me-1",
               id="home-open-xl", n_clicks=0),
    dbc.Modal([
        dbc.ModalHeader(
            dbc.ModalTitle("Biểu đồ thống kê tỉ lệ giới tính và thống kê giới tính theo nhóm tuổi của khách hàng"),
            className="text-center"),
        dbc.ModalBody([
            html.Iframe(
                id='home-modal-plot',
                srcDoc=None,  # here is where we will put the graph we make
                style={"height": "600px", "width": "100%"}),
        ]),
    ],
        id="home-modal-xl",
        size="xl",
        is_open=False,
    ),
])


# callback function always after @callback
# id ko dc trùng nhau cho tất cả component
@callback(
    Output("home-modal-xl", "is_open"),
    Input("home-open-xl", "n_clicks"),
    State("home-modal-xl", "is_open"),
)
def toggle_modal(n1, is_open):
    if n1:
        return not is_open
    return is_open


@callback(
    Output('home-modal-plot', 'srcDoc'),
    Input("home-open-xl", "n_clicks"),
)
def home_barchart(input_val):

    # Tỉ lệ giới tính và thống kê giới tính theo nhóm tuổi của khách hàng
    fig = plt.figure(figsize=(10, 6))
    gs = GridSpec(1, 3, figure=fig, width_ratios=[6.3, 2.2, 2.2])

    # ax1 plot
    ax1 = fig.add_subplot(gs[0:3, 0:3])
    age_gender_counts = df.groupby(['Age', 'Gender'])['User_ID'].nunique().reset_index()
    male_data = age_gender_counts[age_gender_counts['Gender'] == 'Male']
    female_data = age_gender_counts[age_gender_counts['Gender'] == 'Female']
    ax1.bar(male_data['Age'], male_data['User_ID'], color='cornflowerblue', alpha=1, label='Nam')
    ax1.bar(female_data['Age'], female_data['User_ID'], color='orange', alpha=1, label='Nữ')
    ax1.set_xlabel('Nhóm tuổi', fontsize=20)
    ax1.set_ylabel('Khách hàng', fontsize=20)
    ax1.legend()
    for index, row in male_data.iterrows():
        ax1.text(row['Age'], row['User_ID'], str(row['User_ID']), ha='center', va='bottom')
    for index, row in female_data.iterrows():
        ax1.text(row['Age'], row['User_ID'], str(row['User_ID']), ha='center', va='bottom')

    # ax2 plot
    ax2 = fig.add_subplot(gs[0, 2:4], aspect=(3))
    gender_counts = df.groupby('Gender')['User_ID'].nunique()
    colors = ['orange', 'cornflowerblue']
    ax2.pie(gender_counts, autopct='%1.1f%%', colors=colors, wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    ax2.set_title('Tỉ lệ giới tính', fontweight='bold')

    # ax3 plot
    ax3 = fig.add_subplot(gs[0, 1:2], aspect=(80))
    purchase_by_gender = df.groupby('Gender')['Purchase'].sum()
    total_purchase = df["Purchase"].sum()
    purchase_ratio = purchase_by_gender / total_purchase
    sizes = purchase_by_gender.values
    colors = ['orange', 'cornflowerblue']
    ax3.pie([1], radius=0.3, colors=['white'], wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    wedges, texts, autotexts = ax3.pie(sizes, colors=colors, autopct='%1.1f%%', startangle=90, pctdistance=0.85,
                                       labeldistance=1.1,
                                       wedgeprops={'edgecolor': 'black', 'linewidth': 1})
    centre_circle = plt.Circle((0, 0), 0.68, color='black', fc='white', linewidth=1.25)
    fig.gca().add_artist(centre_circle)

    revenue_text = 'Doanh thu trung bình:'
    revenue_text1 = 'Nam INR{:,.0f}'.format(purchase_by_gender['Male'] / df['User_ID'].nunique())
    revenue_text2 = 'Nữ INR{:,.0f}'.format(purchase_by_gender['Female'] / df['User_ID'].nunique())

    plt.text(0, 0.3, s=revenue_text, ha='center', va='center', fontsize=9.5)
    plt.text(0, 0.15, s=revenue_text1, ha='center', va='center', fontsize=9.5)
    plt.text(0, 0, s=revenue_text2, ha='center', va='center', fontsize=9.5)

    ax3.set_title('Tỉ lệ doanh thu theo giới tính khách hàng', fontweight='bold')

    # plt.show()
    html_fig = mpld3.fig_to_html(fig)
    return html_fig
