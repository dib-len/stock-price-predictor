import yfinance as yf
import pandas as pd

def get_stock_data(ticker, period="1y"):
    stock_data = yf.Ticker(ticker)
    df = stock_data.history(period=period)

    df['Prev Close'] = df['Close'].shift(1)
    df['High-low'] = df['High'] - df['Low']
    df['Open-close'] = df['Open'] - df['Close']
    df['Volume'] = df['Volume']
    df['MA10'] = df['Close'].rolling(window=10).mean()

    df['Next Close Prediction'] = df['Close'].shift(-1)

    df.dropna(inplace=True)
    return df

print(get_stock_data("AAPL"))
