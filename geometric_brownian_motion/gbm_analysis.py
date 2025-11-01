import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys
import os
from pathlib import Path
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
from data import gather_data
from gbm_strategy import gbm_monte_carlo

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



def main():
    
    TICKERS = ["AAPL", "AMD", "NVDA", "SPY"]
    WINDOWS = [10, 20, 50, 100, 200]
    START = [2020, 1, 1]
    END = [2025, 1, 1]




    plt.figure()
    for ticker in TICKERS:
        
        if os.path.exists(f"../data/{ticker}.csv"):
            df = pd.read_csv(f"../data/{ticker}.csv")
        
        else:
            print(f"no local {ticker} data, requesting from API...")
            df = gather_data.request(
                ticker =ticker,
                start = START,
                end = END
                )
        
        
        for window in WINDOWS:
            
            res = gbm_monte_carlo(df, WINDOW = window)                                                                                                                                                                                                                                                                                                                                                                                    
            trues, forecasts = res[:,0], res[:, 1]
            delta = abs(trues-forecasts)
            
main()