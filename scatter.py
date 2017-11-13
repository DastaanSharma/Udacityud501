

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return 'C:/Users/LOST/Desktop/{}.csv'.format(symbol)


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df=pd.DataFrame(index=dates)
    for symbol in symbols:
        df1 = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Price'], na_values=['nan'],thousands=',')
        df1 = df1.rename(columns={'Price': symbol})
        df = df.join(df1)

        df = df.dropna(subset=[symbol])

    return df

def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily=df.copy()
    daily[1:]=(df[1:]/df[:-1].values)-1
    daily.ix[0,:]=0
    return daily


def test_run():
    # Read data
    dates = pd.date_range('2010-07-01', '2017-10-31')  # one month only
    symbols = ['fnifty','ongc','crude']
    df = get_data(symbols, dates)
    df.to_csv('C:/Users/LOST/Desktop/papa.csv')

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
  #  plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")


if __name__ == "__main__":
    test_run()
