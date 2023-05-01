import matplotlib
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import plotly.express as px
import datetime as dt
from math import sqrt, pow
import numpy as np
import pandas as pd
from pandas.api.types import CategoricalDtype
from tabulate import tabulate
from colorama import Fore, Style
import seaborn as sns
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import dash
import dash_bootstrap_components as dbc
from dash import Dash, Input, Output, State, dcc, html

import warnings

warnings.filterwarnings('ignore', category=FutureWarning)

df = pd.read_csv('data/black-friday-sales-eda.csv')
df['Gender'] = df['Gender'].replace(['F', 'M'], ['Female', 'Male'])
df['Marital_Status'] = df['Marital_Status'].replace([0, 1], ['Single', 'Married'])


def home_barchart():
    # Tỉ lệ giới tính và thống kê giới tính theo nhóm tuổi của khách hàng
    fig = plt.figure(figsize=(18, 10))
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
    revenue_text = 'Doanh thu trung bình:\nNam INR{:,.0f}\nNữ: INR{:,.0f}'.format(
        purchase_by_gender['Male'] / df['User_ID'].nunique(), purchase_by_gender['Female'] / df['User_ID'].nunique())
    plt.text(0, 0, s=revenue_text, ha='center', va='center', fontsize=9.5)
    ax3.set_title('Tỉ lệ doanh thu theo giới tính khách hàng', fontweight='bold')

    # plt.show()
    return fig


def exp_chart():
    gender_counts = df.groupby('Gender')['User_ID'].nunique()
    exp_fig = px.pie(gender_counts)
    exp_fig.update_layout()
    return exp_fig
