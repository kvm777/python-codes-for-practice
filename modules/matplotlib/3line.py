import matplotlib.pyplot as plt
import numpy as np

'''
linestyle can be written as ls.
dotted can be written as :.
dashed can be written as --.
'''

#linestyle
y = np.array([2,1,4,6,3])
plt.plot(y, linestyle='dotted' , c='k', linewidth=5, label='dotted line' )

y1 = np.array([1,3,5,7,2])
plt.plot(y1, ls="-." , color='#4CAF50',label='dasd_dot') 

# color or c for color indication
# linewidth

plt.legend()
plt.show()