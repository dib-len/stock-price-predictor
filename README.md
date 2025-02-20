# Stock Price Predictor

A machine learning powered stock prediction web app that predicts stock prices using **Random Forest Regression**. The backend is built using Python for quick API responses (FastAPI) and ML (sklearn), and SvelteKit for the frontend!

## Features
- Predicts the next day's stock closing price, based on historical data.
- Uses **Random Forest Regression** for *mostly* accurate predictions.
- SvelteKit frontend for a nice modern design and error handling.
- Secure FastAPI backend with `.env`-based CORS handling.
- Live API fetching from **Yahoo Finance (`yfinance`)**.

## **Why Random Forest?**
- Handles complex stock patterns a bit better than simpler models like Linear Regression (which I was originally considering).
- Uses multiple decision trees to predict trends better.
- Avoids overfitting.

Essentially, **Random Forest = Better Accuracy for Stock Prediction** :P

# Example!
Here I checked Apple's stock price:

<img width="721" alt="Screenshot 2025-02-20 at 17 36 33" src="https://github.com/user-attachments/assets/c82fb751-10bd-48b2-85f3-07cd2d5378d2" />

Which seemed to be fairly accurate (for when I had run the prediction)!

<img width="681" alt="Screenshot 2025-02-20 at 17 39 42" src="https://github.com/user-attachments/assets/44ec23f1-5b5a-46ef-9695-d581a9918b44" />


## Building and running

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run the backend
```bash
python main.py
```

### Start the frontend
```bash
npm install
npm run dev
```

Thanks for reading! :)
