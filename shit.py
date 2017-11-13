import pandas as pd
import matplotlib.pyplot as draw
def fun():
    df = pd.read_csv('C:/Users/LOST/Desktop/hind1.csv',thousands=',',index_col='Date')

    df[['close10','close11','close12']].plot()

    draw.show()



if __name__=='__main__':
    fun()