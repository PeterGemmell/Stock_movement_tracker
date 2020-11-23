# First we import our packages.
import numpy as np
import pandas as pd

# Next we import our Data Source.
import yfinance as yf

# Next we import our package for visualising the Data.
import plotly.graph_objs as go
# import plotly.graph_objects as go


data = yf.download(tickers='NIO', period='1d', interval='1m')

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
fig.add_trace(go.Candlestick(x=data.index,
                open=data['Open'],
                high=data['High'],
                low=data['Low'],
                close=data['Close'], name = 'market data'))

# Here we Add Titles to our Graph.
fig.update_layout(
    title='Live share price evolution',
    yaxis_title='Stock Price (USD per Share)')

# Defining X-Axes
fig.update_xaxes(
    rangeslider_visible=True,
    rangeselector=dict(
        buttons=list([
            dict(count=1, label="1m", step="minute", stepmode="backward"),
            dict(count=15, label="15m", step="minute", stepmode="backward"),
            dict(count=45, label="45m", step="minute", stepmode="backward"),
            dict(count=1, label="HTD", step="hour", stepmode="todate"),
            dict(count=3, label="3h", step="hour", stepmode="backward"),
            dict(step="all")
        ])
    )
)

# Finally we show our results
fig.show()
