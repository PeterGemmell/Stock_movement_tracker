# First we import our packages
import numpy as np
import pandas as pd

# Next we import our Data Source
import yfinance as yf

# Next we import our package for visualising the Data
import  plotly.graph_objs as go

data = yf.download(tickers='SPY', period='1d', interval='1m')

# print(data)
