Software needs to be installed
1. Install Python
2. Install Pycharm
-----------------------------------------------------------
3. Install libs needs (open terminal in pycharm to install):

pip install dash dash-bootstrap-components ipywidgets
pip install folium plotly jupyter-dash fontawesome mpld3
pip install pandas numpy matplotlib seaborn squarify sklearn scikit-learn
-----------------------------------------------------------
4. Run project without doing anything

import folium
from folium.plugins import HeatMap

import ipywidgets as widgets
from IPython.display import display, clear_output

import pandas as pd
from pandas.api.types import CategoricalDtype

import numpy as np

import matplotlib

![image](https://github.com/khanhphamj/Black-Friday-Sales-Analysis/assets/120659979/5b588363-fa9d-463d-b1d5-e4377ad8aad3)
<img width="960" alt="image" src="https://github.com/khanhphamj/Black-Friday-Sales-Analysis/assets/120659979/fb24c9ed-82ef-4dc1-a8df-a01f92cc2196">


from matplotlib import pyplot as plt

import ipywidgets as widgets
from IPython.display import display

import seaborn as sns
import squarify
import datetime as dt
from math import sqrt, pow
import seaborn as sns

from sklearn.preprocessing import LabelEncoder,StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots	
import plotly.io as pio
import plotly.offline as py
