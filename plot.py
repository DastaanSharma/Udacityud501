import pandas as pd
import matplotlib.pyplot as plot
def plt():
    df=pd.read_csv('C:/Users/LOST/Desktop/lundnifty.csv',thousands=',',index_col='Date')
    print(df['sum'])
    df[['sh']].plot()
    plot.show()
if __name__ == '__main__':
    plt()
