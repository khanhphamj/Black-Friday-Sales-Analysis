import matplotlib
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
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
import warnings
warnings.filterwarnings('ignore', category=FutureWarning)

df = pd.read_csv('data/black-friday-sales-eda.csv')

df['Gender'] = df['Gender'].replace(['F', 'M'], ['Female', 'Male'])
df['Marital_Status'] = df['Marital_Status'].replace([0, 1], ['Single', 'Married'])

# Số lượng hóa đơn mua hàng
num_users = df['User_ID'].nunique()

# Tổng doanh thu
total_purchase = df["Purchase"].sum()

# Doanh thu trung bình trên một khách hàng
median_purchase = total_purchase / num_users

# Tính tỉ lệ Marital_Status khi groupby User_ID và Marital_Status
num_married = len(df[df['Marital_Status'] == 'Married'].groupby(df['User_ID']))
num_single = len(df[df['Marital_Status'] == 'Single'].groupby(df['User_ID']))
num_users = df['User_ID'].nunique()

married_percent = num_married/num_users*100
single_percent = num_single/num_users*100

#Category sản phẩm nào bán chạy nhất
all_categories = pd.concat([df['Product_Category_1'], df['Product_Category_2'], df['Product_Category_3']])
most_common_value = all_categories.value_counts().nlargest(1)

#Product_ID được mua nhiều nhất
top_10_order = df['Product_ID'].value_counts().sort_values(ascending=False)[:10]
top_1_bestseller_product = top_10_order.nlargest(1).index

# Product_ID nào có doanh thu cao nhất
product_purchase = df.groupby(['Product_ID'])['Purchase'].sum()
total_purchase = product_purchase.sum()

top_10_products = product_purchase.sort_values(ascending=False)[:10]
top_10_percentproduct = (product_purchase/total_purchase).sort_values(ascending=False)[:10]

top_1_bestpurchase_product = top_10_products.nlargest(1).index

