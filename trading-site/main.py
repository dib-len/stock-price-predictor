import yfinance as yf
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split

def get_stock_data(ticker, period="1y"):
    stock_data = yf.Ticker(ticker)
    df = stock_data.history(period=period)

    df['Prev Close'] = df['Close'].shift(1)
    df['High-low'] = df['High'] - df['Low']
    df['Open-close'] = df['Open'] - df['Close']
    df['Volume'] = df['Volume']
    df['MA10'] = df['Close'].rolling(window=10).mean()
    df['Next Close'] = df['Close'].shift(-1)

    df.dropna(inplace=True)
    return df

def train_random_forest(df):
    X = ['Prev Close', 'High-low', 'Open-close', 'Volume', 'MA10']
    y = ['Next Close']

    X_train, X_test, y_train, y_test = train_test_split(df[X], df[y], test_size=0.2, random_state=1234567890)

    model = RandomForestRegressor(n_estimators=100, random_state=1234567890)
    model.fit(X_train, y_train)

    return model

def predict_next_close(model, df):
    last_row = df.iloc[-1][['Prev Close', 'High-low', 'Open-close', 'Volume', 'MA10']].values.reshape(1, -1)
    prediction = model.predict(last_row)[0]

    return prediction

# Temporarily testing the model
print(predict_next_close(train_random_forest(get_stock_data("NVDA")), get_stock_data("NVDA")))