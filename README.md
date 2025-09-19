# Trading Bot

A simple backtesting framework for a moving average crossover trading strategy using Alpaca historical data.

---

## Features

- **Data Gathering:**  
  Fetches historical stock data using the Alpaca API.

- **Strategy:**  
  Implements a simple moving average (SMA) crossover strategy.

- **Backtesting:**  
  Simulates trades based on generated buy/sell signals.

- **Visualization:**  
  Plots price and moving averages, saving the plot as `signal_plot.png`.

---

## Project Structure

```
trading_bot/
│
├── data/
│   └── gather_data.py
├── strategies/
│   └── simple_moving_average_crossover.py
├── main.py
├── .gitattributes
└── README.md
```

---

## Usage

1. **Set up Alpaca API keys**  
   Place your Alpaca API keys in a file named `alpaca_keys.txt` in the project root, formatted as expected by `gather_data.py`.

2. **Install dependencies**
   - numpy
   - pandas
   - matplotlib
   - alpaca-py

   You can install them with:
   ```
   pip install numpy pandas matplotlib alpaca-py
   ```

3. **Run the bot**
   ```
   python main.py
   ```

   This will:
   - Download historical data for AMD (2020–2025)
   - Apply the SMA crossover strategy
   - Simulate trading
   - Save a plot of price and moving averages
   - Print the final portfolio value

---

## How It Works

- **Data Download:**  
  `gather_data.py` fetches daily price data for a given ticker and date range.

- **Signal Generation:**  
  `simple_moving_average_crossover.py` computes short and long SMAs, generating buy/sell signals when they cross.

- **Backtest Logic:**  
  `main.py` simulates buying $5000 worth of shares on a buy signal and selling all shares on a sell signal. At the end, any remaining shares are sold at the last price.

- **Visualization:**  
  The script saves a plot of the price and moving averages as `signal_plot.png`.

---

## Notes

- The script is for educational and research purposes only.
- Make sure your `alpaca_keys.txt` is formatted correctly for the `get_keys()` function.
- The code assumes the input DataFrame from Alpaca contains an `'open'` column for prices.

---

## Example Output

```
12000.0 0 12000.0
```
Where the numbers represent:  
`[final cash, shares held, total portfolio value]`

---

## License

MIT License