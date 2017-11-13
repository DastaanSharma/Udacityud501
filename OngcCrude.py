import pandas as pd
import matplotlib.pyplot as draw
def fun():
    start='2010-01-01'
    end='2017-09-30'
    dates=pd.date_range(start,end)
    df1=pd.DataFrame(index=dates)

    df2=pd.read_csv('C:/Users/LOST/Desktop/data/Ongc.csv',index_col='Date',parse_dates=True,usecols=['Date','Price'],na_values=['nan'])
    df2=df2.rename(columns={'Price':'Ongc'})
  #  df1=df1.join(df2)
   # df1=df1.dropna()

    df4=pd.read_csv('C:/Users/LOST/Desktop/data/Crude.csv',thousands=',',index_col='Date',parse_dates=True,usecols=['Date','Price'],na_values=['nan'])
    df4=df4.rename(columns={'Price':'Crude'})
    df2=df2.join(df4)
    df2=df2.dropna()
    print(df2)
    df2=df2.astype(float)
    df2[['Crude','Ongc']].plot()
    draw.show()
    print(df2)






if __name__=='__main__':
    fun()
