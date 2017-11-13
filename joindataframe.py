import pandas as pd
import matplotlib.pyplot as draw
def fun():

    df1=pd.read_csv('C:/Users/LOST/Desktop/niftu.csv',index_col='Date',parse_dates=True,usecols=['Date','Price','Open'],na_values=['nan'],thousands=',')
    dfzinc=pd.read_csv('C:/Users/LOST/Desktop/snp.csv',index_col='Date',parse_dates=True,usecols=['Date','Price','Open'],na_values=['nan'],thousands=',')
    dfzinc=dfzinc.rename(columns={'Price':'sprice','Open':'sopen'})
    df1=df1.join(dfzinc)

    df1 = df1.dropna()
    df1.to_csv('C:/Users/LOST/Desktop/beta.csv')
    print(df1)

if __name__=='__main__':
    fun()



