import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily=df.copy()
    daily[1:]=(df[1:]/df[:-1].values)-1
    daily.ix[0,:]=0
    return daily


def test_run():
    # Read data

    df = pd.read_csv('C:/Users/LOST/Desktop/papa.csv',index_col='Date',thousands=',')
    df.to_csv('C:/Users/LOST/Desktop/papa.csv')


    daily_returns = compute_daily_returns(df)
    
    daily_returns.plot(kind='scatter',x='fnifty',y='ongc')
    beta_fnifty,alpha_fnifty=np.polyfit(daily_returns['fnifty'],daily_returns['ongc'],1)
    plt.plot(daily_returns['fnifty'],beta_fnifty*daily_returns['fnifty']+alpha_fnifty,'-',color='r')

    daily_returns.plot(kind='scatter', x='crude', y='ongc')
    beta_crude, alpha_crude = np.polyfit(daily_returns['crude'], daily_returns['ongc'], 1)

    plt.plot(daily_returns['crude'], beta_crude * daily_returns['crude'] + alpha_crude, '-', color='r')
   # daily_returns.plot(kind='scatter', x='fnifty', y='crude')
    plt.show()

if __name__ == "__main__":
    test_run()