import pandas as pd


def test_run():

    df = pd.read_csv('C:/Users/LOST/Desktop/data.csv')
    print(df[10:15])


if __name__ == '__main__':

    test_run()
