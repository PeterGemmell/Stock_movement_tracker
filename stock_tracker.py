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


# We declare figure
fig = go.Figure()

fig.add_trace(go.Scatter(x=data.index, y= data['Middle Band'], line=dict(color='blue', width=.7), name = 'Middle Band'))
fig.add_trace(go.Scatter(x=data.index, y= data['Upper Band'], line=dict(color='red', width=1.5), name = 'Upper Band (Sell)'))
fig.add_trace(go.Scatter(x=data.index, y=data['Lower Band'], line=dict(color='green', width=1.5), name = 'Lower Band (Buy)'))


# Defining our CandleStick
fig.add_trace(go.CandleStick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))

# Here we Add Titles to our Graph.
