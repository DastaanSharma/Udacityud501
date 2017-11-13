import nsetools as nse
import pandas as pd
def fun():
    q = nse.get_quote('infy')
    print(q)
if __name__=='__main__':
    fun()
