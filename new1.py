import os
import pandas as pd
import matplotlib.pyplot as draw


def symbol_to_path(symbol, base_dir="data"):

    return os.path.join(base_dir, "{}.csv".format(str(symbol)))


def get_data(symbols, dates):
    """Read stock data (adjusted close) for given symbols from CSV files."""
    df = pd.DataFrame(index=dates)
    if 'fnifty' not in symbols:  # add SPY for reference, if absent
        symbols.insert(0, 'fnifty')

    for symbol in symbols:
        df1=pd.read_csv('C:/Users/LOST/Desktop/{}.csv'.format(symbol),index_col='Date',parse_dates=True,usecols=['Date','Price'],na_values=['nan'],thousands=',')
        df1=df1.rename(columns={'Price':symbol})
        df=df.join(df1)

        df=df.dropna()

    return df


def test_run():
    # Define a date range
    dates = pd.date_range('2010-01-22', '2017-10-30')

    # Choose stock symbols to read
    symbols = ['fnifty','hind1']

    # Get stock data
    df = get_data(symbols, dates)

    df.plot()
    draw.show()




if __name__ == "__main__":
    test_run()