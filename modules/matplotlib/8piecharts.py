import matplotlib.pyplot as plt
import numpy as np

x=np.array([35,25,60,40])
l = ['A','B','C','D']
myexplode = [0.2,0,0,0]
plt.pie(x, labels=l,explode=myexplode, shadow=True, startangle=90 )
plt.legend(title='my colors:')
plt.show()