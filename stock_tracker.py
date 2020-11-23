# First we import our packages.
import numpy as np
import pandas as pd

# Next we import our Data Source.
import yfinance as yf

# Next we import our package for visualising the Data.
import  plotly.graph_objs as go

data = yf.download(tickers='SPY', period='1d', interval='1m')

# print(data)

# Here we will Draw the middle, higher and lower bands. We are defining the bands.
# This code, when executed will create 3 new columns to the dataframe.
data['Middle Band'] = data['Close'].rolling(window=21).mean()
data['Upper Band'] = data['Middle Band'] + 1.96*data['Close'].rolling(window=21).std()
data['Lower Band'] = data['Middle Band'] - 1.96*data['Close'].rolling(window=21).std()

# Our next step is to plot the data and check if we can predict the market movement.
