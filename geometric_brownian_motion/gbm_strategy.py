import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from pathlib import Path
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
from data import gather_data


def gbm_monte_carlo(df, N_SIMS = 1000, WINDOW = 50):
    #consider only open openings
    prices = df['open']
    
    res = np.zeros((len(prices) - WINDOW, 2), dtype=float)
    
    #rolling window
    p = prices.values
    for t in range(WINDOW, len(p)):
    
        window = p[t-WINDOW : t]
        
        log_returns = np.log(window[1:] / window[:-1])
        sigma = np.std(log_returns)
        mu = np.mean(log_returns)  + 0.5* sigma **2
        
        Z = np.random.normal(size = N_SIMS)
        sim_prices = window[-1] * np.exp((mu-0.5*sigma**2) + sigma*Z)
        forecast = np.mean(sim_prices)
        
        #print(window[-3:]) 
        #print(p[t-3:t])
        
        res[t-WINDOW, 0] = prices[t]
        res[t-WINDOW, 1] = forecast

    return res






def testdata():
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
        
    return df

gbm_monte_carlo(testdata())