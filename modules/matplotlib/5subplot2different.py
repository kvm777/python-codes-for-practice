import matplotlib.pyplot as plt
from matplotlib import gridspec
import numpy as np

x = np.arange(0,10,0.1)

y = np.cos(x)
y1=np.sin(x)
plt.plot(x,y)
plt.plot(x,y1)

plt.title("Trigonometric Graphs",size=20,color='b')
plt.tight_layout(pad=0.5)
plt.show()