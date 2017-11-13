import pandas as pd
import matplotlib.pyplot as draw
def fun():
    start='2010-01-01'
    end='2017-10-30'
    dates=pd.date_range(start,end)
    df1=pd.DataFrame(index=dates)

    df2=pd.read_csv('C:/Users/LOST/Desktop/fnifty.csv',index_col='Date', usecols=['Date','Open','Price','High','Low'],parse_dates=True,na_values=['nan'],thousands=',')

    df2=df2.rename(columns={'Open':'open'})
    df1=df1.join(df2)
    df1=df1.dropna()

    df3=pd.read_csv('C:/Users/LOST/Desktop/hind1.csv',index_col='Date',usecols=['Date','Open','Price','High','Low'],parse_dates=True,na_values=['nan'],thousands=',')
    df3=df3.rename(columns={'Open':'nopen','Price':'nprice','High':'nhigh','Low':'nlow'})
    df1=df1.join(df3)
    df1=df1.dropna()
    print(df1)
    df1.to_csv('C:/Users/LOST/Desktop/lundnifty.csv')




if __name__=='__main__':
    fun()
