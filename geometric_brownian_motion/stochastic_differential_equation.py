import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from collections import deque

N_SIMS = 1000
WINDOW = 50


def gbm_monte_carlo(df):
    #consider only open openings
    prices = df['open']
    live_window = deque(maxlen==WIN DOW)
    
    for price in prices:
        live_window.append(price)

        if len(live_window) < WINDOW:
            continue
        
        mu = np.mean(live_window)
        sigma = np.std(deque)



    

    return None
    
    
    

