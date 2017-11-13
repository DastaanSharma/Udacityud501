import pandas as pd
import matplotlib.pyplot as mtp

def fun():
    df=pd.read_csv('C:/Users/LOST/Desktop/Banks.csv')
    print(df['Range'].mean())
    

    df['Range'].plot()

    mtp.show()
if __name__=='__main__':
    fun()
,'F','G','H','I','J','K','L','M','N','O','P','Q','R'