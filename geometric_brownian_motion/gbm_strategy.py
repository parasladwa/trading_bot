import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import sys
import os
from pathlib import Path
parent_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(parent_dir))
from data import gather_data

N_SIMS = 1000
WINDOW = 50


def gbm_monte_carlo(df):
    #consider only open openings
    prices = df['open']
    
    print(prices) 



    

    return None
    






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