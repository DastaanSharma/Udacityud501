import pandas as pd

def fun():
    start_date='2017-01-05'
    end_date='2017-01-10'
    dates=pd.date_range(start_date,end_date)
    df1=pd.DataFrame(index=dates)


    dfz=pd.read_csv('C:/Users/LOST/Desktop/Pzinc.csv')


    df1=df1.join(dfz)
    print(df1)

if __name__=='__main__':
    fun()