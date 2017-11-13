import pandas as pd
import numpy as np
import matplotlib.pyplot as draw
import scipy.optimize as spo

def f(x):
    y=(x-1.5)**2+0.5
   # print('x={},y={}'.format(x,y))
    return y
def run():
    guess=2
    min_result=spo.minimize(f,guess,method='SLSQP',options={'disp':True})
    print('Minima found at')
    print('x={},y={}'.format(min_result.x,min_result.fun))
    xplot=np.linspace(0.5,2.5,21)
    yplot=f(xplot)
    draw.plot(xplot,yplot)
    draw.plot(min_result.x,min_result.fun,'go')
    draw.show()

if __name__=='__main__':
    run()