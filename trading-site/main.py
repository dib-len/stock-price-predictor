import yfinance as yf
import pandas as pd

def get_stock_data(ticker):
    stock_data = yf.Ticker(ticker)
    stock_data = stock_data.history(period="30d")
    stock_data = stock_data[['Close']]
    return stock_data

print(get_stock_data('AAPL'))