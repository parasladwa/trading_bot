import numpy as np
import pandas as pd
import datetime
import matplotlib.pyplot as plt

from alpaca.data.timeframe import TimeFrame
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest




def get_keys():

    path = "../alpaca_keys.txt"
    f = np.loadtxt(path, dtype=str)
    endpoint, key, secret = f[0, 2], f[1, 2], f[2, 2]
    
    return str(endpoint), str(key), str(secret)




    
def request(ticker = "AMZN", start = [2020, 1, 1], end = [2025, 1, 1]):
    
    ENDPT, KEY, SECRET = get_keys()
    client = StockHistoricalDataClient(KEY, SECRET)

    request = StockBarsRequest(
        symbol_or_symbols = ticker,
        timeframe = TimeFrame.Day,
        start = datetime.date(start[0], start[1], start[2]),
        end = datetime.date(end[0], end[1], end[2])
    )

    bars = client.get_stock_bars(request)
    df = bars.df

    
    return df
    
    