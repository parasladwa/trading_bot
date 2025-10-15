import pandas as pd
import numpy as np
import matplotlib.pyplot as plt





def sma_crossover(df, short_period=50, long_period=200):

    

    open = df['open']

    short_ma = open.rolling(window=short_period).mean()
    long_ma = open.rolling(window=long_period).mean() 

    df_ = pd.DataFrame({
        'price' : open,
        'short_ma' : short_ma,
        'long_ma' : long_ma
    })
    
    df_.dropna(subset=['short_ma', 'long_ma'], inplace=True)

    df_['signal'] = 0
    df_.loc[df_['short_ma'] > df_['long_ma'], 'signal'] = 1  # buy
    df_.loc[df_['short_ma'] < df_['long_ma'], 'signal'] = -1 # sell

    
    
    signals = df_['signal'].copy()
    signals = np.array(signals, dtype=int)
    i = 0
    while i < len(signals):
        if signals[i] == 0:
            i += 1
            continue 

        
        curr = signals[i]
        i+=1
        while i+1 < len(signals) and signals[i] == curr:
            signals[i] = 0
            i+=1
        
    df_['signal'] = signals
    
    

    return df_
    
    
    
