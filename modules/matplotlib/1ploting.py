import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,6])
y = np.array([1,7])
plt.plot(x,y , 'o')     #ploting without line...
plt.axis([0,10,0,8])    #gives the axis of the plot..

plt.plot(x,y , label='line')           #ploting of line

plt.plot([2,5,7,3,1] , label='default x')      #default x points

x1 = np.array([1,3,5,7])
y1 = np.array([4,4,8,2])
plt.plot(x1,y1, label='multiple')

plt.legend(title='ploting:')
plt.show()


#if u want individual graphs one by one... u may use plt.show() command after ploting..