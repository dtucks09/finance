import pandas as pd
import numpy as np
import yfinance as yf
import stats

def trends(ticker):
    #import data from yahoo finance API
    ticker_data = yf.Ticker(ticker)
    #select price history from data & create dataframe
    df = pd.DataFrame(ticker_data.history(period='1y'))
    # DEFINE THE FUNCTIONS TO BE USED IN ANALYSIS

    # SIMPLE MOVING AVERAGE
    def roller_sma(series, window):
        rolling_mean = pd.Series.rolling(series, window=window).mean()
        return rolling_mean

    # CALCUALTE THE SMA's
    df['5d_sma'] = roller_sma(df['Close'], 5)
    df['10d_sma'] = roller_sma(df['Close'], 10)
    df['20d_sma'] = roller_sma(df['Close'], 20)
    df['50d_sma'] = roller_sma(df['Close'], 50)
    df['200d_sma'] = roller_sma(df['Close'], 200)
    # If 5d_sma > 20d_sma then 5v20_bull_bear = bullish
    # THIS NEEDS TO BE CLEANED UP INTO A SINGLE FUNCTION
    conditions_sma_5v20 = [
    df['5d_sma'] > df['20d_sma'],
    df['5d_sma'] < df['20d_sma']
    ]

    conditions_sma_10v50 = [
    df['10d_sma'] > df['50d_sma'],
    df['10d_sma'] < df['50d_sma']
    ]

    conditions_sma_Closev200 = [
    df['Close'] > df['200d_sma'],
    df['Close'] < df['200d_sma']
    ]

    choices = [
    'bullish',
    'bearish'
    ]

    df['5v20_trend'] = np.select(conditions_sma_5v20, choices)
    df['10v50_trend'] = np.select(conditions_sma_10v50, choices)
    df['Closev200_trend'] = np.select(conditions_sma_Closev200, choices)

    # CALCULATE THE 14d RSI
    RSI_window_length = 14
    close = df['Close']
    delta = close.diff()
    delta = delta[1:]
    up, down = delta.copy(), delta.copy()
    up[up < 0] = 0
    down[down > 0] = 0
    roll_up1 = up.ewm(span=RSI_window_length).mean()
    roll_down1 = down.abs().ewm(span=RSI_window_length).mean()
    RS = roll_up1 / roll_down1
    df['RSI'] = 100.0 - (100.0 / (1.0 + RS))

    # CALCULATE THE BOLLINGER BANDS

    risk_range = list(
    df['Close'].tail(1).values.tolist() +
    df['5d_sma'].tail(1).values.tolist() +
    df['10d_sma'].tail(1).values.tolist() +
    df['50d_sma'].tail(1).values.tolist() +
    df['200d_sma'].tail(1).values.tolist() +
    df['5v20_trend'].tail(1).values.tolist() +
    df['10v50_trend'].tail(1).values.tolist() +
    df['Closev200_trend'].tail(1).values.tolist() +
    df['RSI'].tail(1).values.tolist()
    )

    risk_range.insert(0, ticker)

    return risk_range
