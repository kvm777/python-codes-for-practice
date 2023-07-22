import matplotlib.pyplot as plt
import numpy as np

x= np.array(['A', 'B', 'C', 'D','E'])
y= np.array([10,35,65,45,25])

plt.subplot(1,2,1)
plt.bar(x,y, width=0.3, color='hotpink')

plt.subplot(1,2,2)
plt.barh(x,y)

plt.show()
