import yfinance as yf
import pandas as pd

# Define the stock symbol (e.g., Apple)
stock_symbol = "AAPL"

# Fetch historical data (last 6 months)
stock_data = yf.download(stock_symbol, period="6mo")

# Save to CSV
stock_data.to_csv("stock_data.csv")
print("Stock data saved successfully.")