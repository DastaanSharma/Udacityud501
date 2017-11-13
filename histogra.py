import pandas as pd
import matplotlib.pyplot as draw
def daily(df):
    df1=df.copy()
    df1[1:]=(df[1:]/df[:-1].values)-1
    df1.ix[0,:]=0
    return df1
def fun():
    dates=pd.date_range('2010-10-30','2017-10-30')
    df=pd.read_csv('C:/Users/LOST/Desktop/fnifty.csv',index_col='Date',usecols=['Date','Price'],parse_dates=True,na_values=['nan'],thousands=',')
    hisu=daily(df)
    hisu.hist(bins=200)
    mean=hisu['Price'].mean()
    print('mean',mean)
    draw.axvline(mean,color='g',linestyle='dashed',linewidth=2)
    std=hisu['Price'].std()
    draw.axvline(std,color='r',linestyle='dashed',linewidth=2)
    draw.axvline(-std, color='r', linestyle='dashed', linewidth=2)

    draw.show()
if __name__=='__main__':
    fun()
