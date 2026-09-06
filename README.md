# 📈 Basic Algorithmic Trading Simulation

This is a basic algorithmic trading simulation that I built while learning **NumPy and Pandas**.

The main idea was to take what I had learned from my first two Python libraries and actually use them in a small project instead of just studying them.

## What Does It Do?

The program takes **60 days of historical data** for a selected asset and calculates its **5-day Simple Moving Average (SMA)**.

It then compares the closing price with the SMA:

* If the closing price is **below the SMA → BUY**
* If the closing price is **above or equal to the SMA → SELL**

Based on these signals, the program simulates buying and selling using a virtual amount of money provided by the user.

## Assets Available

You can choose from:

* Apple (AAPL)
* Bitcoin (BTC-USD)
* Microsoft (MSFT)
* Amazon (AMZN)
* NVIDIA (NVDA)
* Tesla (TSLA)
* Ethereum (ETH-USD)
* Gold (GC=F)
* S&P 500 ETF (SPY)

## How I Built It

I used **yfinance** to get the historical market data and **Pandas** to clean and work with the data.

The SMA is calculated using:

```python
df['5_day_SMA'] = df['Close'].rolling(window=5).mean()
```

I used **NumPy** to create the BUY/SELL signals:

```python
df['Signal'] = np.where(
    df['Close'] < df['5_day_SMA'],
    'BUY',
    'SELL'
)
```

For the trading part, I used basic **Object-Oriented Programming** to create a portfolio that keeps track of the available cash, shares, and trading history.

Finally, the trading history is converted into a Pandas DataFrame and saved as:

`my_trading_log.csv`

## 🛠️ Technologies Used

* Python
* NumPy
* Pandas
* yfinance
* Object-Oriented Programming
* CSV

## 📚 What I Learned

This project helped me understand how NumPy and Pandas can be used with real-world data. I also got more practice with **OOP, loops, if/else conditions, data cleaning, DataFrames, and CSV files**.

It is a simple project, but it was a good first step toward using Python libraries in practical projects instead of only learning them theoretically.

## ⚠️ Disclaimer

This is an **educational project**, not a real trading system or financial advice. The strategy is intentionally simple and does not account for things like transaction costs, slippage, risk management, or other real-world market factors.

## ▶️ Run the Project

Install the required libraries:

```bash
pip install yfinance numpy pandas
```

Then run the Python file:

```bash
python main.py
```
