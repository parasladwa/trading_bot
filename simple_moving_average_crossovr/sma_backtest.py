import os
import pandas as pd
import numpy as np
import sys
from pathlib import Path
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
from data import gather_data
import matplotlib.pyplot as plt
import sma_strategy


def main():

    START = [2020, 1, 1]
    END = [2025, 1, 1]
    TICKER = "SPY"


    if os.path.exists(f"../data/{TICKER}.csv"):
        df = pd.read_csv(f"../data/{TICKER}.csv")
    
    else:
        print(f"no local {TICKER} data, requesting from API...")
        df = gather_data.request(
            ticker = TICKER,
            start = START,
            end = END
            ) 

    df_sigs =sma_strategy.sma_crossover(df)
   
   
    dollars = 10000
    shares = 0
    buy = 5000   
    
    
    prices = np.array(df_sigs['price'], dtype = float)
    short_ma = np.array(df_sigs['short_ma'], dtype = float)
    long_ma = np.array(df_sigs['long_ma'], dtype = float)
    plt.figure()
    plt.plot(prices, color = 'black', )
    plt.plot(short_ma, color = 'red')
    plt.plot(long_ma, color = "blue")
    plt.title("Blue = 200day MA, Red = 50day MA")
    plt.ylabel("price")
    plt.xlabel(f"{START[::-1]} to {END[::-1]}")
    plt.savefig("signal_plot.png")
    plt.close()
    
    
    
     
    for index, row in df_sigs.iterrows():
        
        if row['signal'] == 0:
            continue
        
        #buy (1000USD)
        if row['signal']  > 0 and dollars > buy:
            dollars -= buy
            shares += buy/row['price']
            continue
         
        #sell (all shares)
        if row['signal'] < 0 and shares > 0:
            dollars += shares * row['price']
            shares = 0
            
    if shares > 0:
        dollars += shares * row['price']
        shares = 0
        
        
        
    print((dollars + row['price']*shares)/100., " %")

main()
