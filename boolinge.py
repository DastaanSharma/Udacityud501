import pandas as pd
import matplotlib.pyplot as draw

def fun():
    dates=pd.date_range('2010-10-01','2017-10-31')
    df1=pd.DataFrame(index=dates)
    df=pd.read_csv('C:/Users/LOST/Desktop/fnifty.csv',index_col='Date',parse_dates=True,usecols=['Date','Price'],na_values=['nan'],thousands=',')
    df=df.join(df1)
    df=df.dropna()

    draw.show()
    mean=pd.rolling_mean(df['Price'],window=20)
    std=pd.rolling_std(df['Price'],window=20)
    lower=mean-2*std
    upper=lower+4*std
    ax=df['Price'].plot()
    df['Price'].plot()

   # mean.plot(label='mean',ax=ax)
   # lower.plot(label='lower',ax=ax)
   # upper.plot(label='Upper',ax=ax)
   # draw.show()
    df2=df.copy()

if __name__=='__main__':
    fun()