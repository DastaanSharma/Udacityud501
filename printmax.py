import pandas as pd
def print_max(symbol):
    df=pd.read_csv("C:/Users/LOST/Desktop/{}.csv".format(symbol))
    return df['Range'].max()
def run():
    for symbol in ['data','fortis','coal']:
        print('Max range')
        print(symbol,print_max(symbol))

if __name__ == '__main__':
    run()
