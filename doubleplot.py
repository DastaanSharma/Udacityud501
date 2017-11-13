import pandas as pd
import matplotlib.pyplot as mat

def fun():
    df=pd.read_csv('C:/Users/LOST/Desktop/deep2.csv')
    df[['KPrice','DPrice']].plot()
    mat.show()

if __name__=='__main__':
    fun()