import numpy as np
from data import gather_data
import matplotlib.pyplot as plt
from strategies import simple_moving_average_crossover as sma_c



def main():
    
    df = gather_data.request(
        ticker = "AMD",
        start = [2020, 1, 1],
        end = [2025, 1, 1]
        ) 

    df_sigs = sma_c.sma_crossover(df)
   
   
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
        
        
        
    print(dollars, shares, dollars + row['price']*shares)

    
    
    
    
    
    
main() 