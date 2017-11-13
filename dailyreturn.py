"""Compute daily returns."""

import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    """Return CSV file path given ticker symbol."""
    return 'C:/Users/LOST/Desktop/{}.csv'.format(symbol)


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'fnifty' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'fnifty')

    for symbol in symbols:
        df_temp = pd.read_csv(symbol_to_path(symbol), index_col='Date',
                parse_dates=True, usecols=['Date', 'Price'], na_values=['nan'],thousands=',')
        df_temp = df_temp.rename(columns={'Price': symbol})
        df = df.join(df_temp)
        if symbol == 'fnifty':  # drop dates SPY did not trade
            df = df.dropna(subset=["fnifty"])

    return df


def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plot stock prices with a custom title and meaningful axis labels."""
    ax = df.plot(title=title, fontsize=12)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()


def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily=df.copy()
    daily[1:]=(df[1:]/df[:-1].values)-1
    daily.ix[0,:]=0
    return daily


def test_run():
    # Read data
    dates = pd.date_range('2010-07-01', '2017-07-31')  # one month only
    symbols = ['fnifty']
    df = get_data(symbols, dates)
    ax=plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")


if __name__ == "__main__":
    test_run()
