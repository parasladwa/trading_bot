import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





def gbm_monte_carlo(df):
    #consider only open openings
    print(df.columns)
    prices = df['open']

    #log returns  = (si/ si-1)
    log_returns = np.log(prices[1:] / prices[:-1])

    
    

    return prices
    
    
    

