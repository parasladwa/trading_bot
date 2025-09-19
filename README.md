# Trading Bot

A simple backtesting framework for a moving average crossover trading strategy using Alpaca historical data.

To be implemented: Buy/sell indicators on visuals, argparse arguments, multiple strategies

---

## Features

- **Data Gathering:**  
  Fetches historical stock data using the Alpaca API.
  `gather_data.py`

- **Strategy:**  
  Implements a simple moving average (SMA) crossover strategy. `simple_moving_average_crossover.py`

  Aiming to implement and test more strategies.

- **Backtesting:**  
  Simulates trades based on generated buy/sell signals. `main`

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
   ```
   pip install numpy pandas matplotlib alpaca-py
   ```

3. **Run the bot**
   ```
   python main.py
   ```
    Can change parameters in `main.py` (dates, ticker, etc).

    This will be improved such that inputs will be taken through CLI

---
![Plot](signal_plot.png)